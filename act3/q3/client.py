import socket
import pickle
import datetime
from threading import Thread
import select

active = True

def receiver(sock):
    global active
    # a receiver function that updates the stdout with new messages
    while active:
        ready,_,_ = select.select([sock],[],[])
        if ready and active:
            # read the message length
            msg_len = int.from_bytes(sock.recv(4), byteorder='big')
            # read the message
            raw_msg = sock.recv(msg_len)
            # unpickle the message
            msg = pickle.loads(raw_msg)
            formatted_timestamp = msg['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            print(f'\n({formatted_timestamp}) {msg['sender']}: {msg['content']}\n')

def sender(sock, username):
    global active
    # a sender function that sends new messages to the server
    while True:
        content = input()
        msg = {'sender': username, 'content': content, 'timestamp': datetime.datetime.now()}
        # pickle the message
        raw_msg = pickle.dumps(msg)
        # send the message length
        sock.send(len(raw_msg).to_bytes(4, byteorder='big'))
        # send the message
        sock.send(raw_msg)
        if content == '!q':
            active = False
            break

def run():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('localhost', 3003))
    print('Successfully connected to the server!')
    # ask the user for their username
    username = input('Enter your username: ')
    # send the username length to the server
    client_sock.send(len(username).to_bytes(4, byteorder='big'))
    # send the username to the server
    client_sock.send(username.encode())
    # create receiver thread
    receiver_thread = Thread(target=receiver, args=[client_sock])
    sender_thread = Thread(target=sender, args=[client_sock, username])
    receiver_thread.start()
    sender_thread.start()
    sender_thread.join()
    receiver_thread.join()
    client_sock.close()

if __name__ == '__main__':
    run()

    