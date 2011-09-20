'''
Created on 15 Sep 2011

@author: xtephan
'''

from server.server  import Server 


IP   = "127.0.0.1"
PORT = 1666

if __name__ == '__main__':
    
    srv = Server()
    
    srv.hello()
    
    #echo server. will replay everything you say
    #srv.echo_server(IP, PORT)
    
    
    
    
    pass