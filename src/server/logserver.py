'''
Created on Sep 20, 2011

@author: xtephan
'''

class LogServer():
    '''
    Receives logs from the Stelarris
    and saves them in a DB
    '''


    def parsePackage(self,package):
        '''
        Returns a list containing the sensor number and value read
        '''
        
        ret    = package.split( '#' )
        
        ret[0] = int( ret[0]   )
        ret[1] = int( ret[1],2 ) #convert from binary to decimal
        
        return ret
    
    
    def sanity(self):
        return 4