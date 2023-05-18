
import socket
import cv2
import pickle
import struct

from Master.main import mainMaster



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
print("host name", host_name)
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = (host_ip, port)
server_socket.bind(socket_address)
server_socket.listen(5)
print("LISTENING AT:", socket_address)

while True:
    client_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)

        while(vid.isOpened()):
            img, frame = vid.read()
            
            
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)

            mainMaster(frame)
            
            cv2.imshow('TRANSMITTING VIDEO', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
