#Imports library
import socket

#Creates instance of 'Socket'
s = socket.socket()

hostname = '127.0.0.1' #Server IP/Hostname
port = 8000 #Server Port

s.connect((hostname,port)) #Connects to server

while True:
    x = input("Digita il tuo nome: ") #Gets the message to be sent
    s.send(x.encode()) #Encodes and sends message (x)