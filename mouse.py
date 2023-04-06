import serial
import serial.tools.list_ports
import random
import time
import sys

from termcolor import colored

class ArduinoMouse:
    def __init__(self):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 1
        self.serial_port.port = self.find_serial_port()
        try:
            self.serial_port.open()
        except serial.SerialException:
            print(colored('[Error]', 'red'), colored('Colorant is already open or the serial port is being used by another app.', 'white'))
            time.sleep(5)
            sys.exit()

    def find_serial_port(self):
        port = next((port for port in serial.tools.list_ports.comports() if "Arduino" in port.description), None)
        if port is not None:
            return port.device
        else:
            print(colored('[Error]', 'red'), colored('Unable to find serial port or the Arduino device is with different name. Please check its connection and try again.', 'white'))
            time.sleep(5)
            sys.exit()

    def move(self, x, y):
        x = x + 256 if x < 0 else x
        y = y + 256 if y < 0 else y
        self.serial_port.write(b"M" + bytes([int(x), int(y)]))
        
    def click(self):
        self.serial_port.write(b"C")
        time.sleep(0.01)

    def close(self):
        self.serial_port.close()

    def __del__(self):
        self.close()
