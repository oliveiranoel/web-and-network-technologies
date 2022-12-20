import json
import os
import sys

import requests
import serial


def setupSerialConnection():
    # open serial port on macos/linux
    com = os.popen('ls /dev/cu.usb*').read()
    if com:
        return com
    else:
        return serial.Serial('/dev/cu.usbmodem14102',
                             baudrate=115200)


def loop(com):
    server_url = 'http://172.20.10.12:8080'

    while True:
        msg = com.read(2)  # read msg sent by the microbit

        if msg == 'rr':
            endpoint = '/room'
            response = requests.delete(url=server_url + endpoint)

            if not response.ok:
                raise SystemError("webservice not responding correctly")
        elif msg == 'nr':
            endpoint = '/room'
            response = requests.post(url=server_url + endpoint)
        else:
            content = {"temperature": int(msg)}
            payload = json.dumps(content).encode('utf8')
            endpoint = '/temperature'
            response = requests.post(url=server_url + endpoint,
                                     data=payload)
            if not response.ok:
                raise SystemError("webservice not responding correctly")


if __name__ == "__main__":
    try:
        client_serial = setupSerialConnection()
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
