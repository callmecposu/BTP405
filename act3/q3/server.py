import socket 
import pickle
from threading import Thread
import datetime

connections = []

def readMessage(client_sock):
    # read the messages length
    msg_len = int.from_bytes(client_sock.recv(4), byteorder='big')
    # read the pickled message
    raw_msg = client_sock.recv(msg_len)
    # unpickle the message
    msg = pickle.loads(raw_msg)
    return msg

def sendMessage(connection, msg):
    # pickle the message
    raw_msg = pickle.dumps(msg)
    # send the pickled messages length
    connection.send(len(raw_msg).to_bytes(4, byteorder='big'))
    # send the pickled message
    connection.send(raw_msg)

def serve(client_sock, client_addr):
    # read the user name length
    username_len = int.from_bytes(client_sock.recv(4), byteorder='big')
    # read the username
    username = client_sock.recv(username_len).decode()
    print(f'{client_addr} connected with a \'{username}\' username')
    # notify the chat that user has connected
    for connection in connections:
        sendMessage(connection, {'sender': 'Server', 'content': f'{username} entered the chat', 'timestamp': datetime.datetime.now()})
    # start reading messages from the client
    msg = readMessage(client_sock)
    while msg['content'] != '!q':
        # send the message among the other connections
        for connection in connections:
            sendMessage(connection, msg)
        msg = readMessage(client_sock)
    # notify the chat that user has disconnected
    for connection in connections:
        sendMessage(connection, {'sender': 'Server', 'content': f'{username} left the chat', 'timestamp': datetime.datetime.now()})
    # close the connection
    client_sock.close()
    # remove the connection from the memory
    connections.remove(client_sock)
    


def run():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.bind(('localhost', 3003))
    print('Server now listening on port 3003...')
    serv_sock.listen(1)
    
    while True:
        client_sock, client_addr = serv_sock.accept()
        print(f'{client_addr} has connected to the server!')
        connections.append(client_sock)
        t = Thread(target=serve, args=[client_sock, client_addr])
        t.start()
        
if __name__ == '__main__':
    run()