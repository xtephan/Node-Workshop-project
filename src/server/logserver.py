'''
Created on Sep 20, 2011

@author: xtephan
'''

#===============================================================================
# Receives logs from the Stelarris and saves them in a DB
#===============================================================================
class LogServer():


    #===========================================================================
    # Init the class
    #===========================================================================
    def __init__(self):
        self.error_msg = ""


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
    # Used to check the sanity of the class in unittests
    #===========================================================================
    def sanity(self):
        return 4