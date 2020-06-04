import socket

HOST = '192.168.1.37' # IP do meu PC
PORT = 65433

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello Word ')
        data = s.recv(1024)

    print('Recebido: ', repr(data))
