'''
Created on 15 Sep 2011

@author: xtephan
'''

import socket
from configurations import *

class EchoServer2():
    '''
    Echo server. 
    Will return the same value as the one received
    '''


    def __init__(self):
        
        print("Starting Echo Server...")
        
        #Binds the server to the given port.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind( (CONFIG['echo_server_ip'], CONFIG['echo_server_port'])  )
    
        #Queue up to five requests before turning clients away.
        self.socket.listen(5)
    
        #what to replay?
        self.go_back=CONFIG['echo_server_sendBack']
    
    
    def set_replay(self,value):
        self.go_back=value
    
    '''
    Start running the server
    '''
    def run(self):
    
        while True:
            
            request, client_address = self.socket.accept()
            
            #Turn the incoming and outgoing connections into files.
            input = request.makefile('rb', 0)
            output = request.makefile('wb', 0)
            l = True
            
            try:
                
                while l:
                    
                    l = input.readline().strip()
                    
                    #log received message
                    #FIXME: fix this 
                    print("I received--" + str(l,'utf-8')  + "--end")
            
                    if l:
                        
                        if self.go_back:
                            output.write( l[::-1] + bytes('\r\n','utf-8') )
                
                    else:
                        #Shut down reads and writes
                        request.shutdown(2) 
            
            except socket.error:
            #network error
                pass

