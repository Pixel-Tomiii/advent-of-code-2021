import math
import time

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

def sum_of(values):
    total = 0
    for x in values:
        total += x
    return total

def product(values):
    start = values.pop(0)
    for x in values:
        start *= x
    return start

def minimum(values):
    val = math.inf
    for x in values:
        if x < val:
            val = x
    return val

def maximum(values):
    val = -math.inf
    for x in values:
        if x > val:
            val = x
    return val

def greater_than(values):
    x, y = values
    return 1 if x > y else 0

def less_than(values):
    x, y = values
    return 1 if x < y else 0

def equal_to(values):
    x, y = values
    return 1 if x == y else 0

func_map = {
    0:sum_of,
    1:product,
    2:minimum,
    3:maximum,
    5:greater_than,
    6:less_than,
    7:equal_to,
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

    if not bin_str:
        return
    
    # Read packet version.
    bin_str, packet_version = read(bin_str, 3)
    version_total += int(packet_version, 2)
##    print('\t' * depth + f"PACKET: {packet_version} -> {int(packet_version, 2)}", file=log)

    # Read operator.
    bin_str, op = read(bin_str, 3)
##    print('\t' * depth + f"OPERATOR: {op} -> {int(op, 2)}", file=log)
    op = int(op, 2)

    # Read numbers from operator.
    if op == 4:
##        print('\t' * depth + f"READING VALUES", file=log)
        
        values = []
        cont = "1"
        
        while int(cont, 2) != 0:
            bin_str, cont = read(bin_str, 1)
            bin_str, num = read(bin_str, 4)

            values.append(num)
##        print('\t' * depth + f"LENGTH OF PACKET: {3 + 3 + (5 * len(values))}", file=log)
        values = "".join(values)
        return int(values, 2), bin_str

    # Reading sub packets.
    else:
        func = func_map[op]
        
        bin_str, length_type_ID = read(bin_str, 1)
##        print('\t' * depth + f"LENGTH TYPE: {length_type_ID}", file=log)

        if length_type_ID == "0":
##            print('\t' * depth + f"READING LENGTH", file=log)
            bin_str, packets_length = read(bin_str, 15)
            packets_length = int(packets_length, 2)
            original = len(bin_str)

            values = []

##            print('\t' * depth + f"TOTAL LENGTH: {packets_length}", file=log)
            # Reading a sub packet.
            while original - len(bin_str) < packets_length:
##                print('\t' * depth + f"ORIGINAL: {original} VS {len(bin_str)}", file=log)
                value, bin_str = read_packets(bin_str, depth=depth+1)
                values.append(value)

            return func(values), bin_str
            
                
        else:
##            print('\t' * depth + f"READING SUB PACKETS", file=log)
            bin_str, num_packets = read(bin_str, 11)
            num_packets = int(num_packets, 2)
##            print('\t' * depth + f"NUMBER OF SUB PACKETS: {num_packets}", file=log)
            values = []
            while num_packets > 0:
                value, bin_str = read_packets(bin_str, depth=depth+1)
                values.append(value)
                num_packets -= 1

            return func(values), bin_str



##log = open("log.txt", "w")
bin_str = bin(inp)
start = time.time()
result(read_packets(bin_str))
end = time.time()
##log.close()

print(f"Time taken: {round((end - start) * 1000)}ms")
            
