'''
Created on Sep 20, 2011

@author: xtephan
'''

#===============================================================================
# Importing needed modules and library
#===============================================================================
import socket
import sys

from configurations import *

try:
    import pymysql 
except Exception:
    print("Error loading pymysql library. Use https://github.com/petehunt/PyMySQL")
    sys.exit(0)


#===============================================================================
# Receives logs from the Stelarris and saves them in a DB
#===============================================================================
class LogServer():


    #===========================================================================
    # Init the class
    # Bind the log server
    #===========================================================================
    def __init__(self):
        
        print("Starting Log Server...")
        
        self.error_msg = ""
        
        try:
            #Binds the server to the given port.
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind( (CONFIG['log_server_ip'], CONFIG['log_server_port'])  )
        
            #Queue up to five requests before turning clients away.
            self.socket.listen(5)
            
        except Exception:    
            print( "Error while creating the server" )
            sys.exit(0)
            
        
        try:
            self.mysql_connection()
        except Exception:    
            print( "Error while connecting to the DB" )
            sys.exit(0)
            
    #===============================================================================
    # Start running the server
    #===============================================================================
    def run(self):
    
        while True:
            
            request, client_address = self.socket.accept()
            
            #Turn the incoming and outgoing connections into files.
            input = request.makefile('rb', 0)
            self.net_file_out = request.makefile('wb', 0)
            
            package = True
            
            try:
                
                while package:
                    
                    package = input.readline().strip()
                                        
                    #log received message
                    print("I received--" + str(package,'utf-8')  + "--end")
                    
                    #start working
                    self.do_your_job( str(package,'utf-8')  )
            
                    if not package:
                        request.shutdown(2) 
            
            except socket.error:
            #network error
                pass

    
    
    
    #===============================================================================
    # Does all the dirty work
    #===============================================================================
    def do_your_job(self, package):
        
        if not self.checkSanity(package):
            print( "[ERROR]: " + self.error_msg )
            self._net_output_("[ERROR]: " + self.error_msg)

        self.save_to_DB( self.parsePackage(package) )
        
     
    #==========================================================================
    # Connect to the database 
    #==========================================================================
    def mysql_connection(self):
        DBconn = pymysql.connect( 
                                      host   = CONFIG['db_server_ip']       , 
                                      port   = CONFIG['db_server_port']     , 
                                      user   = CONFIG['db_server_user']     , 
                                      passwd = CONFIG['db_server_password'] , 
                                      db     = CONFIG['db_server_database'] )
        
        self.DBcur = DBconn.cursor()
        
        
    #===========================================================================
    # Save received data to the DB
    #===========================================================================
    def save_to_DB(self,data):
        #INSERT INTO `logs` (`sensor nr`, `value`, `date time`, `id`) VALUES
        #-> (1, 990, '2011-09-20 11:17:08', 2);
        
        try: 
            self.DBcur.execute( "INSERT INTO log2(sensor_nr,val,dt,id) VALUES(%s,%s,NOW(),%s)", (data[0],data[1],"NULL") )
        except Exception:
            print("[!!] Error while trying to add data into DB for " + data[0] + " -- " + data[1])
            
            
    #===========================================================================
    # Parse the package and returns a list containing 
    # the sensor number and value read
    #===========================================================================
    def parsePackage(self,package):
        
        ret    = package.split( '#' )
        
        ret[0] = int( ret[0]   )
        ret[1] = int( ret[1],2 ) #convert from binary to decimal
        
        return ret
    
    #===========================================================================
    # Check is the package has the expected format and data
    # sanity != acurate 
    #===========================================================================
    def checkSanity(self,package):
        
        if len(package) != 12:
            self.error_msg = "Unexpected package length"
            return False
        
        if int(package[0]) not in range(1,5):
            self.error_msg = "Unknown sensor id"
            return False
        
        if package[1] != "#":
            self.error_msg = "Unexpected package format"
            return False
        
        for ch in package[2:]:
            if ch not in ["0","1"]:
                self.error_msg = "Unexpected sensor value format"
                return False
            
        return True
    
    
    #===========================================================================
    # Sends messages through the network
    #===========================================================================
    def _net_output_(self,msg):
        
        if not CONFIG['log_server_sendBack']:
            return 
        
        if msg and msg[-1] != '\n':
            msg += '\r\n'

        try:
            self.net_file_out.write( bytes( msg + '\r\n','utf-8') )  
        except socket.error:
            print("Network error!!")
        
    #===========================================================================
    # Used to check the sanity of the class in unittests
    #===========================================================================
    def sanity(self):
        return 4