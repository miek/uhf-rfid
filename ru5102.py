import crcmod
import serial
import struct

class RU5102:
    def __init__(self, dev='/dev/ttyUSB0', baud=57600):
        self.ser = serial.Serial(dev, baud)
        self.crc_func = crcmod.predefined.mkPredefinedCrcFun('crc-16-mcrf4xx')

    def send_command(self, cmd, addr=0x0):
        length = 4
        packet = struct.pack('BBB', length, addr, cmd)
        crc = self.crc_func(packet)
        packet = packet + struct.pack('<H', crc)
        self.ser.write(packet)

        response_length = ord(self.ser.read())
        response = self.ser.read(response_length)
        print(response)

if __name__ == "__main__":
    reader = RU5102()
    reader.send_command(0x1)
