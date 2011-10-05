'''
Created on Oct 5, 2011
@author:  Stefan Fodor
'''

import socket
from configurations import *

class EchoServer():
    '''
    Echo server. 
    Will return the same value as the one received
    '''


    def __init__(self):
        
        print("Starting Echo Server...")
        
    
    '''
    Start running the server
    '''
    def run(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = CONFIG['echo_server_ip'] 
        port = CONFIG['echo_server_port']  
        s.bind((host,port))
        s.listen(5)
        
        while True:
            conn, addr = s.accept()
            data = conn.recv(1000000)
            print('I received--' + str(data,'utf-8') + '--')
        
        #conn.send(data)
        conn.close()

