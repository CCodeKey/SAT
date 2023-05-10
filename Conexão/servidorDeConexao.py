import socket

ipDoCliente1 = '10.15.136.12' 
ipDoCliente2 = '10.15.136.12' 
ipDoCliente3 = '10.15.136.12' 
ipDoCliente4 = '10.15.136.12' 
ipDoCliente5 = '10.15.136.12' 
ipDoCliente6 = '10.15.136.12' 

PORT = 12365  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('... SAT iniciado ...')
print()
while True:
    msg = input(str("> "))
    print()
    message = msg.encode()
    client_socket.sendto(message, (ipDoCliente1, PORT))