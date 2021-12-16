from typing import Literal


def Solution(file_content):
    hex = file_content[0].strip()
    binary_str = hex_to_bin_str(hex)

    packet_dict = get_packet_details(binary_str)[0]
    sum = get_version_sum(packet_dict)
    return sum

def get_version_sum(packet_dict):
    sum=packet_dict["packet_version"]
    # print(sum, packet_dict)
    for sub_packet_dict in packet_dict["sub_packets"]:
        sum+=get_version_sum(sub_packet_dict)
    return sum

def get_packet_details(binary_str):
    current_index = 0
    packet_version = int(binary_str[current_index:current_index+3], 2)
    current_index+=3

    type_id = int(binary_str[current_index:current_index+3], 2)
    current_index+=3

    literal_value = -1
    length_type_id = -1
    if type_id == 4:
        literal_value = ""
        groups = []
        while current_index+5 <= len(binary_str):
            groups.append(binary_str[current_index:current_index+5])
            current_index+=5
            if binary_str[current_index-5] == "0":
                break
        for packet in groups:
            literal_value+=packet[1:]
        literal_value = int(literal_value, 2)
        packet = {
            "packet_version": packet_version,
            "type_id": type_id,
            "sub_packets": [],
            "num_sub_packets": 0,
            "literal_value": literal_value,
            "length": current_index
        }
        return packet, current_index
    else:
        length_type_id = int(binary_str[current_index], 2)
        current_index+=1

        if length_type_id == 0:
            sub_packets = []
            total_length = int(binary_str[current_index:current_index+15], 2)
            current_index+=15
            final_index = current_index+ total_length 
            while current_index < final_index:
                sub_packet, index = get_packet_details(binary_str[current_index:])
                sub_packets.append(sub_packet)
                current_index+=index
            packet = {
                "packet_version": packet_version,
                "type_id": type_id,
                "sub_packets": sub_packets,
                "num_sub_packets": len(sub_packets),
                "literal_value": literal_value,
                "length": current_index

            }
            return packet, current_index
        else:
            num_sub_packets = int(binary_str[current_index:current_index+11], 2)
            current_index+=11
            sub_packets = []

            for _ in range(num_sub_packets):
                sub_packet, index = get_packet_details(binary_str[current_index:])
                sub_packets.append(sub_packet)
                current_index+=index

            packet = {
                "packet_version": packet_version,
                "type_id": type_id,
                "sub_packets": sub_packets,
                "num_sub_packets": num_sub_packets,
                "literal_value": literal_value,
                "length": current_index

            }
            return packet, current_index



def hex_to_bin_str(hex):
    hex_repr = {
        "0" : "0000",
        '1' : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111",
    }
    binary = ""
    for value in hex:
        binary+=hex_repr[value]
    
    return binary