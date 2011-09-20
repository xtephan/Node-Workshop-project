'''
CopyLeft Stefan Fodor @ 2011
Created on 15 Sep 2011
'''

def xxxx():
    print("dede")
    
    '''
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Bind the socket to a port, and bid it listen for connections.
sock.bind((hostname, port))
sock.listen(1)
print(“Waiting for a request.”)
#Handle a single request.
request, clientAddress = sock.accept()
print(“Received request from”, clientAddress)
request.send(bytes(‘-=SuperSimpleSocketServer 3000=-\n’, ‘utf-8’))
request.send(bytes(‘Go away!\n’, ‘utf-8’))
request.shutdown(2) #Stop the client from reading or writing anything.
print(“Have handled request, stopping server.”)
sock.close()
'''