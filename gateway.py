import sys
import socket
import serial


def setupSocket(act_host, act_port):
    s = socket.socket()
    s.connect((act_host, act_port))
    return s


def setupSerialConnection():
    # open serial port on macos/linux
    com = serial.Serial('/dev/cu.usbmodem1102',
                        baudrate=115200)

    # open serial port on windows
    # com = serial.Serial('COM5')
    print(com.name)  # check which port was really used
    return com


def run(act_socket, act_message):
    act_socket.send(bytes(act_message, "utf-8"))

    # Receive data from the server and shut down
    received = str(act_socket.recv(1024), "utf-8")
    print("Sent:     {}".format(act_message))
    print("Received: {}".format(received))


def loop(com):
    while True:
        msg = com.read(2)  # read msg sent by the microbit
        # 'msg' will be in bytes. You have to compare byte with a byte. Use bytestring b'...'.
        print(int(msg))
        run(client_socket, str(int(msg)))
        client_socket.close()

        # byte syntax see https://docs.python.org/3/library/stdtypes.html?highlight=byte#bytes
        # https://realpython.com/lessons/defining-literal-bytes-object


if __name__ == "__main__":
    try:
        hostname = socket.gethostname()
        print(hostname)
        IPAddr = socket.gethostbyname(hostname)
        print(IPAddr)
        client_serial = setupSerialConnection()
        client_socket = setupSocket("172.20.10.2", 9999)
        loop(client_serial)
    except KeyboardInterrupt as ki:
        sys.exit(0)
    except serial.SerialException as se:
        print(se)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except ConnectionRefusedError as e:
        print(e)
        sys.exit(1)
