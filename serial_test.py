import serial
from time import sleep
from functools import reduce
from operator import xor
import json
# ser = serial.Serial('COM7', baudrate=9600, bytesize=7,
#                     parity=serial.PARITY_EVEN, stopbits=2, timeout=0.5)
# cmd = bytearray(b'@00RE004501000156*\x0D')
# ser.write(cmd)
# sleep(0.3)
# line = ser.readline()
# print(line)
# ser.close()


def ser_obj():
    return serial.Serial('COM7', baudrate=9600, bytesize=7,
                         parity=serial.PARITY_EVEN, stopbits=2, timeout=0.5)


def calculate_checksum(cmd: str) -> str:
    """[create command string--> b'@00RE004501000156*\\r']

    [convert string input to list and integer elements.
    Perform XOR/sum on elements in the list and convert result to hex.
    Hex string is then added back to input string together with *cr.
    resultant string is then converted to bytes and then bytearray. ]

    Arguments:
        cmd {str} -- [constructed after reading connfig.json]

    Returns:
        str -- [bytearray]
    """
    listy = [ord(i) for i in list(cmd)]
    chksum = hex(reduce(xor, map(int, listy)))[2:]
    complete = ''.join((cmd, chksum, r'*\r'))
    final = bytes(complete, encoding="raw_unicode_escape")
    return bytearray(final)


with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)
command_list = [calculate_checksum(f"@00RE00{i}0001") for i in data.keys()]
print(command_list)
# print(data[i]['type'])
