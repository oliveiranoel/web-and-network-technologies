import argparse
import json
import os
import platform
import sys

import requests
import serial

import logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def setupSerialConnection(serial_port):
    """
    Creates a Serial connection.
    For macos/linux, the serial connection is opened and read automatically.
    For Windows, you must pass the serial port as a parameter.
    """
    if platform.system() == "Windows":
        com = serial_port
        log.debug("Got serial connection port from parameter for macos/linux.")
    else:
        com = os.popen('ls /dev/cu.usb*').read().strip()
        log.debug("Got serial connection port from os for macos/linux.")

    if com:
        log.info("Serial connection created!")
        return serial.Serial(com, baudrate=115200)
    else:
        log.error("No serial connection available. Please plugin your micro:bit!")
        raise SystemError("No serial connection available")


def loop(com, server):
    """
    Listener to serial connection. Reads the first to bits.
    - Send a DELETE Request to '/rooms', when serial communication message is 'rr'
    - Send a POST Request to '/room', when serial communication message is 'nr'
    - Send a POST Request to '/temperature', when serial communication message is something else e.g. number of temperature
    """
    server_url = 'http://' + server

    while True:
        # read two bits from serial connection sent by microbit
        msg = com.read(2).decode('ASCII')
        log.info("Read 2 bits from serial connection: %s", msg)

        if msg == 'rr':
            endpoint = '/rooms'
            url = server_url + endpoint
            response = requests.delete(url=url)
            log.info("Sent DELETE request to '/rooms'.")

            if not response.ok:
                raise SystemError("webservice not responding correctly")
        elif msg == 'nr':
            endpoint = '/room'
            url = server_url + endpoint
            response = requests.post(url=url)
            log.info("Sent POST request to '/room'.")

            if not response.ok:
                raise SystemError("webservice not responding correctly")
        else:
            content = {"temperature": int(msg)}
            endpoint = '/temperature'
            url = server_url + endpoint
            response = requests.post(url=url, json=content)
            log.info("Sent POST request to '/temperature' with data: %s", content)

            if not response.ok:
                raise SystemError("webservice not responding correctly")


def parse_arguments():
    parser = argparse.ArgumentParser()
    # optional arguments
    parser.add_argument(
        "-s",
        "--server",
        default="127.0.0.1:8080",
        help="The server address.")
    parser.add_argument(
        "--serial",
        default="/dev/cu.usbmodem1102",
        help="The serial port address.")

    args = parser.parse_args()
    log.info("Arguments parsed: %s", )
    return args.server, args.serial


if __name__ == "__main__":
    try:
        server, serial_port = parse_arguments()
        client_serial = setupSerialConnection(serial_port)
        loop(client_serial, server)
    except KeyboardInterrupt as ki:
        sys.exit(0)
    except serial.SerialException as se:
        log.error(se)
        sys.exit(1)
    except ValueError as e:
        log.error(e)
        sys.exit(1)
    except ConnectionRefusedError as e:
        log.error(e)
        sys.exit(1)
