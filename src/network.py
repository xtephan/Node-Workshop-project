'''
Created on 15 Sep 2011

@author: xtephan
'''

import socket

class Network():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.IPaddress="";
        self.PORT=0;
    
    
    
    def setIPaddress(self,value):
        self.IPaddress = value;
        
    def setPort(self,value):
        self.PORT = value;
    
    
        
    def create_server(self):
        '''
        Create the server. Binds the socket.
        '''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        '''Bind the socket to a port, and bid it listen for connections.'''
        self.sock.bind( (self.IPaddress, self.PORT) )
        self.sock.listen(1)
        
        
    def good_receive(self):
        
        
        request, clientAddress = sock.accept()
        print(“Received request from”, clientAddress)
        request.send(bytes(‘-=SuperSimpleSocketServer 3000=-\n’, ‘utf-8’))
        request.send(bytes(‘Go away!\n’, ‘utf-8’))
        
        
        return ""
    
    
    def close_server(self):
        self.sock.close()    