'''
Created on 15 Sep 2011

@author: xtephan
'''

from server.echoserver import EchoServer

class Server():
    '''
    classdocs
    '''

    def hello(self):
        '''
        Return hello
        '''
        print("Hello world! I am the server class")
        
        
    def echo_server(self,ip,port):
        
        es = EchoServer(ip,port)
        
        es.run()
        #FIXME: put no replay
