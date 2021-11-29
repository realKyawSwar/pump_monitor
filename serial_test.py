import serial
from time import sleep
from functools import reduce
from operator import xor


# ser = serial.Serial('COM7', baudrate=9600, bytesize=7,
#                     parity=serial.PARITY_EVEN, stopbits=2, timeout=0.5)
# cmd = bytearray(b'@00RE004501000156*\x0D')
# ser.write(cmd)
# sleep(0.3)
# line = ser.readline()
# print(line)
# ser.close()


def calculate_checksum(cmd: str) -> str:
    # b'@00RE004501000156*\\r'
    listy = [ord(i) for i in list(cmd)]
    chksum = hex(reduce(xor, map(int, listy)))[2:]
    complete = ''.join((cmd, chksum, r'*\r'))
    final = bytes(complete, encoding="raw_unicode_escape")
    # final = bytes(complete, encoding="utf-8")
    return bytearray(final)


cmd = '@00RE0045440001'
lol = calculate_checksum(cmd)
print(lol)
