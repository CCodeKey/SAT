import socket
from datetime import datetime
meuIp = '10.15.136.12'
PORT = 12365
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((meuIp, PORT))
while True:
    data, address = server_socket.recvfrom(1024)
    data_e_hora_atuais = datetime.now()
    print(f"SERVER | {address} | {data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')} | -> {data.decode()} ")