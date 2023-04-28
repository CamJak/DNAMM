# Helper functions for the main programs

def asciiToBin(ascii):
    # Convert ASCII to binary string
    bin = ""
    for i in ascii:
        bin += format(ord(i), '08b')
    return bin

def binToDec(bin):
    # Convert binary string to decimal
    return int(bin, 2)