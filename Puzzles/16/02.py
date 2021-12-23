from functools import reduce
from operator import mul

global version_number_sum

def parse_literal_packet(packet):
    packet_copy = packet[:]
    binary_number = ""
    while(True):
        group = packet[:5]
        del packet[:5]
        binary_number += "".join(group[1:5])
        if group[0] == '0':
            return packet, int(binary_number, 2)


def parse_operator_packet(packet):
    length_type_id = packet[0]
    values = []

    if length_type_id == '0':
        length = int("".join(packet[1:16]),2)
        sub_packets = packet[16:16+length]
        while(True):
            if any(bit == '1' for bit in sub_packets):
                sub_packets, value = parse_packet(sub_packets)
                values.append(value)
            else:
                return packet[16+length:], values
    else:
        number_of_sub_packets = int("".join(packet[1:12]),2)
        sub_packets = packet[12:]
        for _ in range(number_of_sub_packets):
            sub_packets, value = parse_packet(sub_packets)
            values.append(value)
        return sub_packets, values


def parse_packet(packet):
    version_number = int("".join(packet[:3]), 2)
    global version_number_sum
    version_number_sum += version_number
    version_id = int("".join(packet[3:6]), 2)
    if version_id == 4:
        return parse_literal_packet(packet[6:len(packet)])
    else:
        result, values = parse_operator_packet(packet[6:len(packet)])
        if version_id == 0:
            print(f"Sum of {values}: {sum(values)}")
            return result, sum(values)
        elif version_id == 1:
            print(f"prod of {values}: {reduce(mul, values, 1)}")
            return result, reduce(mul, values, 1)
        elif version_id == 2:
            print(f"Min of {values}: {min(values)}")
            return result, min(values)
        elif version_id == 3:
            print(f"Max of {values}: {max(values)}")
            return result, max(values)
        elif version_id == 5:
            if values[0] > values[1]:
                print(f"{values[0]} is larger than {values[1]}")
                return result, 1
            print(f"{values[0]} is not larger than {values[1]}")
            return result, 0
        elif version_id == 6:
            if values[0] < values[1]:
                print(f"{values[0]} is smaller than {values[1]}")
                return result, 1
            print(f"{values[0]} is not smaller than {values[1]}")
            return result, 0
        elif version_id == 7:
            if values[0] == values[1]:
                print(f"{values[0]} is equal to {values[1]}")
                return result, 1
            print(f"{values[0]} is not equal to {values[1]}")
            return result, 0


with open("transmission.txt") as file:
    for line in file:
        global version_number_sum
        version_number_sum = 0
        binary = list(bin(int('1'+line, 16))[3:])
        result, value = parse_packet(binary)
        print(f"Final value: {value}")
        print(f"Version number sum: {version_number_sum}")