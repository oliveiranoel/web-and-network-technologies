import argparse
import socket
import sys


def setup(act_host, act_port):
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind to the port
    serversocket.bind((act_host, act_port))

    # queue up to 5 requests
    serversocket.listen(5)
    return serversocket


def run(act_serversocket):
    while True:
        # establish a connection to the client.py
        clientsocket,addr = act_serversocket.accept()
        print("Got a connection from {}".format(addr))

        data = clientsocket.recv(1024)
        print(int(data))
        clientsocket.send(data.upper())
        clientsocket.close()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--port",
        default="9999",
        help="tcp port of the server host. Default: 9999")

    args = parser.parse_args()
    return int(args.port)


if __name__ == '__main__':
    try:
        port = parse_arguments();
        server_socket = setup("", port)
        print("Server is running on port {}".format(port))
        run(server_socket)
    except KeyboardInterrupt as e:
        sys.exit(0)
    except ValueError as e:
        print(e)
        sys.exit(1)