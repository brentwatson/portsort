import socket


def start():
    port = 0
    base = 10000
    sorted = []
    finished = False
    while not finished:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', base + port))
            try:
                data = sock.recv(16)
                if data == b'done':
                    finished = True
            except socket.timeout:
                pass
            sorted.append(port)
        except ConnectionRefusedError:
            pass
        finally:
            port += 1
            sock.close()

    return sorted
