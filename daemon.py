#! /usr/bin/python3

import json
import socket
import result
import BeautifulSoup

class TCPDaemon(object):
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('', 9090))
        self.sock.listen(1)

    def get_message(sock):
        result = b''
        while True:
            date = sock.recv(1024)
            if not data:
                break
            result += data
        return result.upper()

def get_url_info(self, url):
    print('Incoming url: {}'.format(url))
    response = requests.get(url.strip())
    soup = BeautifulSoup(response.text, 'lxml')
    d = {}
    


    def loop_forever(self):
        while True:
            sock, addr = self.sock.accept()
            print("Get message...")
            result = self.get_message(sock)
            print("End get message...")
            sock.send(result)
            sock.close()

if __name__=="__main__":


