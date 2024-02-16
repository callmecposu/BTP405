import socket

def run():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 3003)
    client_socket.connect(server_address)
    
    filename = input('Enter the filename to transfer: ')

    try:
        file = open(filename, 'rb')
        print(file)
    except:
        print('Error opening the file.\nExiting...')
        return
    
    # send the filename length
    client_socket.send(len(filename).to_bytes(4, byteorder='big'))

    # send the filename
    client_socket.send(filename.encode())

    # send the file size
    file_bytes = file.read()
    client_socket.send(len(file_bytes).to_bytes(4, byteorder='big'))

    #send the file bytes
    client_socket.send(file_bytes)

    data = client_socket.recv(1024)

    print('Response: ', data.decode())

    client_socket.close()

if __name__ == '__main__':
    run()