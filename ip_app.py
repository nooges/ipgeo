from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def show_ip_info():
    ip_address = request.remote_addr
    hostname = socket.gethostbyaddr(ip_address)[0]

    return 'IP: {}, Hostname: {}'.format(ip_address, hostname)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
