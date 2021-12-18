
def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file if line.rstrip() != ""]
    return lines
  
def result(result):
    """Displays the result"""
    print(f"Result found: {result}")

inp = get_data()[0]
mapping = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111"
        }

def bin(hexadecimal):
    bin_str = []
    
    for char in hexadecimal:
        bin_str.append(mapping[char])

    while bin_str[-1] == "0000":
        bin_str.pop(-1)

    return "".join(bin_str)

def read(bin_str, bits):
    return bin_str[bits:], bin_str[:bits]
    
def read_packets(bin_str, version_total=0, depth=0):

    if len(bin_str) < 6:
        return version_total, ""
    
    # Read packet version.
    bin_str, packet_version = read(bin_str, 3)
    version_total += int(packet_version, 2)
    print('\t' * depth + f"PACKET: {packet_version} -> {int(packet_version, 2)}", file=log)

    # Read operator.
    bin_str, op = read(bin_str, 3)
    print('\t' * depth + f"OPERATOR: {op} -> {int(op, 2)}", file=log)

    # Read numbers from operator.
    if int(op, 2) == 4:
        print('\t' * depth + f"READING VALUES", file=log)
        
        values = []
        cont = "1"
        
        while int(cont, 2) != 0:
            bin_str, cont = read(bin_str, 1)
            bin_str, num = read(bin_str, 4)

            values.append(num)
        print('\t' * depth + f"LENGTH OF PACKET: {3 + 3 + (5 * len(values))}", file=log)

        # Skip remaining 0s.
##        remaining = 4 - ((3 + 3 + (5 * len(values))) % 4)
##        print('\t' * depth + f"REMAINING VALUES: {remaining}", file=log)
##        bin_str, trash = read(bin_str, remaining)

    # Reading sub packets.
    else:
        bin_str, length_type_ID = read(bin_str, 1)
        print('\t' * depth + f"LENGTH TYPE: {length_type_ID}", file=log)

        if length_type_ID == "0":
            print('\t' * depth + f"READING LENGTH", file=log)
            bin_str, packets_length = read(bin_str, 15)
            packets_length = int(packets_length, 2)
            original = len(bin_str)

            print('\t' * depth + f"TOTAL LENGTH: {packets_length}", file=log)
            # Reading a sub packet.
            while original - len(bin_str) < packets_length:
                print('\t' * depth + f"ORIGINAL: {original} VS {len(bin_str)}", file=log)
                total, bin_str = read_packets(bin_str, depth=depth+1)
                version_total += total
                
        else:
            print('\t' * depth + f"READING SUB PACKETS", file=log)
            bin_str, num_packets = read(bin_str, 11)
            num_packets = int(num_packets, 2)
            print('\t' * depth + f"NUMBER OF SUB PACKETS: {num_packets}", file=log)
            while num_packets > 0:
                total, bin_str = read_packets(bin_str, depth=depth+1)
                version_total += total
                num_packets -= 1

    return version_total, bin_str

log = open("log.txt", "w")
bin_str = bin(inp)
print(bin_str)
result(read_packets(bin_str))
log.close()
            
