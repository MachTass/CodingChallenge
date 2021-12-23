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
        length = int("".join(packet[1:16]),2)
        sub_packets = packet[16:16+length]
        while(True):
            if any(bit == '1' for bit in sub_packets):
                sub_packets = parse_packet(sub_packets)
            else:
                return packet[16+length:]
    else:
        number_of_sub_packets = int("".join(packet[1:12]),2)
        sub_packets = packet[12:]
        for i in range(number_of_sub_packets):
            sub_packets = parse_packet(sub_packets)
        return sub_packets


def parse_packet(packet):
    print(f"Parsing packet: {''.join(packet)}")
    version_number = int("".join(packet[:3]), 2)
    global version_number_sum
    version_number_sum += version_number
    version_id = int("".join(packet[3:6]), 2)
    if version_id == 4:
        return parse_literal_packet(packet[6:len(packet)])
    else:
        return parse_operator_packet(packet[6:len(packet)])

with open("transmission.txt") as file:
    for line in file:
        binary = list(bin(int('1'+line, 16))[3:])
        parse_packet(binary)

print(version_number_sum)