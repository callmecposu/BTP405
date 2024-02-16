import socket
import pickle

def run():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_addr = ('localhost', 3003)
    serv_sock.bind(serv_addr)
    serv_sock.listen()

    print('Now listening at port 3003...')

    while True:
        client_sock, client_addr = serv_sock.accept()
        print('Connected to: ', client_addr)

        # read filename length
        filename_len = int.from_bytes(client_sock.recv(4), byteorder='big')
        print('Filename length: ', filename_len)

        # read filename
        filename = client_sock.recv(filename_len).decode()
        print('Filename: ', filename)

        # read the file size
        filesize = int.from_bytes(client_sock.recv(4), byteorder='big')
        print('File Size: ', filesize)

        # read the file bytes
        raw = b''
        file_bytes = client_sock.recv(filesize)
        raw += file_bytes

        data = pickle.loads(raw)
        print('Deserialized object: ', data)

        # specify the path to save a file
        file_path = input('Enter the path where to save the received file: ')
        try:
            out_file = open(file_path, 'wb')
            pickle.dump(data, out_file)
            out_file.close()
        except:
            print('Error saving the file.\nExiting...')
            client_sock.close()
            serv_sock.close()
            return

        client_sock.sendall('We good!'.encode())

        client_sock.close()

        print(f'Client {client_addr} disconnected!')

if __name__ == "__main__":
    run()