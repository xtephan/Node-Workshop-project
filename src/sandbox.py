'''
CopyLeft Stefan Fodor @ 2011
Created on 15 Sep 2011
'''

print("hello")

'''
ERT="asd"


conn = pymysql.connect(host='127.0.0.1', port=3306, user='john_doe', passwd='loremipsum', db='node_workshop')
insert into sandbox(`lorem`) values(`ipsum`);
'''
'''
'''
Created on Dec 3, 2010

@author: xtephan
'''
from tkinter import *
import time
from tkinter.messagebox import showerror
import socket
import _thread
from client_lobby import Client_Lobby

#from time import localtime, strftime

default_encoding = 'utf-8'
buffer_size      = 1024

#date_time = strftime("[ %d-%b-%Y %H:%M:%S ] ",localtime())


class Client():
    

    def sConnect(self,hostaddr,port, username):
  
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.sock.connect( (hostaddr,port) )
            print("Connected")
        
            s=str(self.sock.recv(1024).strip())
       
            self.sock.send( bytes(username,'utf-8') )
            
            #s=str(self.sock.recv(1024).strip())
       
            s=self.recvNormal()
            print("I have received %s" %s)
       

        except Exception:
            print("You are stupid!")
            
    
    
    #returns the received text without  the b'' shit
    #this is more of a work-around    
    def recvNormal(self):
        
        thisReqName= str( self.sock.recv(buffer_size).strip() )
        return thisReqName[2:-1]        
    
            
    #sends a response. Converts string->binary    
    def sendNormal(self, message, new_line=True):
        
        if new_line:
            message += "\n"
        
        self.sock.send( bytes(message,default_encoding) )
        
    
#    def quit_interface(self):
#        self.sock.close()
#        self.inf.quit()

#TODO: create new window
    def waitMessages(self):
        
        while True:
            
            rec = self.recvNormal().split("#")
            
            if rec[0] == "LOBBYALL":
                self.lobby.update_users(rec[1:])
            
            elif rec[0] == "LOBBYMSG" : 
                self.lobby.append_to_conv(rec[1],rec[2])
                
            elif (rec[0] == "LOBBYSTS") and ( rec[1] != self.username):
                
                if rec[2] == "on" :
                    self.lobby.update_users( [rec[1]] )
                else :
                    self.lobby.update_users( [rec[1]], True)
                    
            elif (rec[0] == "TO") and (rec[1] == self.username) :
                
                if rec[3] in self.lobby.privates.keys() :
                    self.lobby.privates[ rec[3] ].append_to_conv(rec[4])
                else :
                    self.lobby.start_private2(rec[3],rec[4])
            

    def startLobby(self):
        
            
        self.lobby = Client_Lobby()
        self.lobby.init(self.sock,self.username)
        self.lobby.start()
    
    
    def connect_btncall(self):
        
        self.txtlbl = "Connecting"
        

        if(self.ip_input.get() == ""):
            showerror("No information","Please fill out the IP address")
        elif(self.port_input.get() == ""):
            showerror("No information","Please fill out the port number")
        elif(self.usr_input.get() == ""):
            showerror("No information","Please fill out the nickname")
        else: 
            for x in range(3):
                self.txtlbl += "."
                self.var.set(self.txtlbl)
                time.sleep(1)
                self.inf.update()
            
            self.sConnect( self.ip_input.get().strip(), 
                           int(self.port_input.get().strip()), 
                           self.usr_input.get().strip()              )
    
            self.username = self.usr_input.get().strip()
            self.startLobby()
            
            time.sleep(2)

            _thread.start_new_thread(self.waitMessages,())
            
            self.sendNormal("ALL",False)  #ask for all the users when connecting
            
            
            '''
            self.startPrivateChat("mimi")
                
            #give the GUI time to init it's self
            time.sleep(2)
            
            _thread.start_new_thread(self.waitMessages,())
            '''

    def __init__(self):

        self.inf = Tk()
        self.inf.title("Chat 1.0")
        self.inf.resizable(0,0)
        
        self.var = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()

        self.inf_size = Canvas(width=250, height=170)
        self.inf_size.pack()

        self.info_lbl = Label(text="Connection information")
        self.info_lbl.pack()
        self.info_lbl.place(x=5,y=5)

        self.ip_lbl = Label(text="IP addr :")
        self.ip_lbl.pack()
        self.ip_lbl.place(x=5,y=40)

        self.port_lbl = Label(text="Port :")
        self.port_lbl.pack()
        self.port_lbl.place(x=5,y=70)

        self.usr_lbl = Label(text="User :")
        self.usr_lbl.pack()
        self.usr_lbl.place(x=5,y=100)
        
        self.ip_input = Entry(textvariable=self.var3)
        self.ip_input.pack()
        self.ip_input.place(x=60,y=40)
        self.var3.set("localhost")
        
        self.port_input = Entry(width=10,textvariable=self.var2)
        self.port_input.pack()
        self.port_input.place(x=60,y=70)
        self.var2.set("6969")
        
        self.usr_input = Entry()
        self.usr_input.pack()
        self.usr_input.place(x=60,y=100)
        
        self.btn_conn = Button(textvariable=self.var4,bd=1, command=self.buttonConDis)
        self.btn_conn.pack()
        self.btn_conn.place(x=130,y=130)
        self.var4.set("Connect")
        
        self.conn_lbl = Label(textvariable=self.var, fg="grey")
        self.conn_lbl.pack()
        self.conn_lbl.place(x=5, y=135)
        
    
    def disconnect(self):
        self.sendNormal("DISC", False)

    
    def buttonConDis(self):
        
        if ( self.var4.get() == "Connect" ) :
            self.connect_btncall()
            self.var4.set("Disconnect")
        else :
            self.disconnect()
            #self.prv_ch.root.destroy()
            self.var4.set("Connect")

 
    def start_interface(self):
        self.inf.mainloop()
'''