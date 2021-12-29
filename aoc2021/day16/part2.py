from functools import reduce

message = ''

hex_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        for char in line.strip('\n'):
            message += hex_map[char]
        
def parse_literal(packet: str) -> tuple:
    chunk_size = 5
    index = 0
    finished = False
    literal_binary = ''
    while not finished:
        if (packet[index] == '0'):
            finished = True
        literal_binary += packet[index+1: index+chunk_size]
        index += chunk_size
    return (int(literal_binary, 2), index)

def parse_operator(packet: str) -> tuple:
    # Get the type of operator
    op_type = int(packet[0], 2)
    if (op_type == 0):
        # 15-bit case
        length_of_sub_packets = int(packet[1:16], 2)
        packet_list = []
        remaining_message = packet[16:]
        fin_index = 16
        while (fin_index - 16) < length_of_sub_packets:
            pack, index = parse_packet(remaining_message)
            fin_index += index
            remaining_message = packet[fin_index:]
            packet_list.append(pack)
    elif (op_type == 1):
        # 11-bit case
        num_of_sub_packets = int(packet[1:12], 2)
        packet_list = []
        remaining_message = packet[12:]
        fin_index = 12
        for _ in range(num_of_sub_packets):
            pack, index = parse_packet(remaining_message)
            fin_index += index
            remaining_message = packet[fin_index:]
            packet_list.append(pack)
    return (packet_list, fin_index)

def version_and_type(packet: str) -> tuple:
    # First 3 bits are version number
    version = int(packet[:3], 2)
    # Next 3 are the packet type
    type_id = int(packet[3:6], 2)
    # print(f'Version, Type ID: {(version, type_id)}')
    return (version, type_id)

def parse_packet(packet: str) -> tuple:
    version, type_id = version_and_type(packet)
    if (type_id == 4):  # If packet is literal, parse literal
        value, fin_index = parse_literal(packet[6:])
    else:   # Otherwise, it is an operator
        value, fin_index = parse_operator(packet[6:])
    # Add 6 to finishd index to take into account that the input packet started at 6
    return ({ 'version': version, 'type': type_id, 'value': value }, fin_index+6)

parsed_packets, total_parsed = parse_packet(message)

def evaluate(packet: dict) -> int:
    # Determine operation
    op = packet['type']
    vals = convert_to_list(packet)
    if (op == 0):   # Sum packets in values
        return sum(vals)
    elif (op == 1):   # Product of packets
        return reduce((lambda x, y: x * y), vals)
    elif (op == 2):   # Minimum of packets
        return min(vals)
    elif (op == 3):   # Maximum of packets
        return max(vals)
    elif (op == 5):   # Greater than
        return int(vals[0] > vals[1])
    elif (op == 6):   # Less than
        return int(vals[0] < vals[1])
    elif (op == 7):   # Equals
        return int(vals[0] == vals[1])

    return 0

def convert_to_list(packet: dict) -> list:
    value = packet.get('value')
    vals = []
    if (isinstance(value, dict)):
        if (value.get('type') == 4):
            vals.append(value.get('value'))
        else:
            vals.append(evaluate(value))
    elif (isinstance(value, list)):
        for p in value:
            if (p.get('type') == 4):
                vals.append(p.get('value'))
            else:
                vals.append(evaluate(p))
    return vals


print(parsed_packets)
print(evaluate(parsed_packets))
