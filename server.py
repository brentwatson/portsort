import select
import socket


def create_socket(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    return server_socket


def start(unsorted):
    base = 10000
    sockets = [create_socket(base + port) for port in unsorted]

    connections = 0
    while connections < len(unsorted):
        readable, _, _ = select.select(sockets, [], [])
        server = readable[0]
        connection, address = server.accept()
        connections += 1
        connection.sendall(b'done' if connections == len(unsorted) else b'next')

    connection.close()
