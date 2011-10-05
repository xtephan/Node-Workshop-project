'''
Created on Oct 5, 2011
@author:  Stefan Fodor
'''

import socket
from configurations import *

class Order():
    
    #===========================================================================
    # Constructor
    #===========================================================================
    def __init__(self,message):
        
        self.sConnect()
        self.sendmsg(message)
    

    #===========================================================================
    # Connect to given host
    #===========================================================================
    def sConnect(self):
        
        
        #open the socket
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.sock.connect( (CONFIG['host_ip'],CONFIG['host_port']) )
            
            print("Connected to " + CONFIG['host_ip'] + ":" + str(CONFIG['host_port']) )
           
       
        except Exception:
            print("Something when wrong")
            

    #===========================================================================
    # Sending data
    #===========================================================================
    def sendmsg(self,message):
        
        #reconstruct msg
        msg=""
        
        for thisMessage in message:
            msg += thisMessage
        
        print("Sending--" + msg)
        
        self.sendNormal(msg)
    
    #===========================================================================
    # ship it over the wire. Converts string->binary    
    #===========================================================================
    def sendNormal(self, message, new_line=False):
        
        if new_line:
            message += "\n"
        
        sent=self.sock.send( bytes(message,'utf-8') )
        
        if sent == 0:
                raise RuntimeError("socket connection broken")
