import random
from helperFunctions import *

class DNA:
    def __init__(self, ASCII):
        self.__dna = self.ascii_to_dna(ASCII)

    def __str__(self):
        return self.__dna

    # BIN to DNA
    def bin_to_dna(self, bin, rule):
        rules = [
            {"01": "A", "11": "C", "00": "T", "10": "G"},
            {"00": "A", "10": "C", "01": "T", "11": "G"},
            {"00": "A", "01": "C", "10": "T", "11": "G"},
            {"01": "A", "00": "C", "11": "T", "10": "G"},
            {"10": "A", "11": "C", "00": "T", "01": "G"},
            {"11": "A", "01": "C", "10": "T", "00": "G"},
            {"11": "A", "10": "C", "01": "T", "00": "G"},
            {"10": "A", "00": "C", "11": "T", "01": "G"}
        ]

        # Check if bin is odd and add a 0 to the front
        if len(bin) % 2 != 0:
            bin = "0" + bin

        # Convert bin to DNA
        out = ""
        for i in range(0, len(bin), 2):
            out += rules[rule][bin[i:i+2]]

        return out

    # Encrypt ASCII to DNA
    def ascii_to_dna(self, ASCII):
        out = ""
        char1 = asciiToBin(ASCII[0])
        rule = binToDec(char1)%8
        for char in ASCII:
            bin = asciiToBin(char)
            out += self.bin_to_dna(bin, rule)
            rule = (rule+1)%8
        return out

    # DNA to BIN
    def dna_to_bin(self, dna):
        rule = {"A": "00", "C": "10", "T": "01", "G": "11"}

        # Convert DNA to bin
        out = ""
        for char in dna:
            out += rule[char]
        out = int(out, 2)
        return out

    # DNA EXOR
    def dna_exor(self, other):
        out = ""
        for i in range(len(self.__dna)):
            bin1 = self.dna_to_bin(self.__dna[i])
            bin2 = self.dna_to_bin(other.__dna[i])
            out_bin =  bin1 ^ bin2
            out_dna = self.bin_to_dna(format(out_bin, 'b'), 1)
            out += out_dna
        return out

    # DNA ADD
    def dna_add(self, other):
        out = ""
        for i in range(len(self.__dna)):
            bin1 = self.dna_to_bin(self.__dna[i])
            bin2 = self.dna_to_bin(other.__dna[i])
            out_bin =  bin1 + bin2
            out_dna = self.bin_to_dna(format(out_bin, 'b')[-2:], 1)
            out += out_dna
        return out

    # DNA SUB
    def dna_sub(self, other):
        out = ""
        for i in range(len(self.__dna)):
            bin1 = self.dna_to_bin(self.__dna[i])
            bin2 = self.dna_to_bin(other.__dna[i])
            out_bin =  bin1 - bin2
            bin_str = str(bin(out_bin & 0b111)[2:])[-2:]
            out_dna = self.bin_to_dna(bin_str, 1)
            out += out_dna
        return out