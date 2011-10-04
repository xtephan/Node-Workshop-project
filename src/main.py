'''
Created on 15 Sep 2011

@author: xtephan
'''
import sys
from server.echoserver import EchoServer
from server.logserver import LogServer

if __name__ == '__main__':
    

    #---------------------------------------- 
    # Which Server do you want to start?
    #---------------------------------------- 
    isRunning = False
    for arg in sys.argv: 
        
        #Initiate echo server
        if arg=="echo":
            EchoServer().run()
            isRunning=True
        
        # Initiate log server
        if arg=="log":
            LogServer().run()
            isRunning=True
       
    
    if not isRunning:
        print( "Usage: python3 main.py [server]\n * echo - for echo server \n * log - for log server" )
    
    pass