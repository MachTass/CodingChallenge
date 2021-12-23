version_number_sum = 0

def parse_literal_packet(packet):
    while(True):
        group = packet[:5]
        del packet[:5]
        if group[0] == '0':
            break
        elif group[0] == '1':
            continue

    return packet


def parse_operator_packet(packet):
    length_type_id = packet[0]

    if length_type_id == '0':
        length = int("".join(packet[1:16]), 2)
        parse_packet(packet[16:(16+length)])
    else:
        length = int("".join(packet[1:12]), 2)
        del packet[:12]

        for _ in range(length):
            packet = parse_packet(packet)

    return packet


def parse_packet(packet):
    #repeat this until the remaining packet is only 0s
    while any(bit == '1' for bit in packet):
        print(f"parsing packet: {''.join(packet)}")
        version_number = int("".join(packet[:3]), 2)
        global version_number_sum
        version_number_sum += version_number
        id = int("".join(packet[3:6]), 2)
        if id == 4:
            packet = parse_literal_packet(packet[6:len(packet)])
        else:
            packet = parse_operator_packet(packet[6:len(packet)])

with open("transmission-text-operator.txt") as file:
    for line in file:
        binary = list(bin(int('1'+line, 16))[3:])
        parse_packet(binary)

print(version_number_sum)
