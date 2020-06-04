import socket

HOST = '192.168.1.37' # IP do meu PC
PORT = 65433

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Esperando conexao em {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn: # para encerrar conexão
            print('Conectado por ', addr)
            while True:
                data = conn.recv(1024) # receber os dados em 1024 bytes
                if not data:
                    break
                conn.sendall(b'Server ' + data)
