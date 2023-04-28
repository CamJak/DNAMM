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
    def dna_to_bin(self, bin, rule):
        rules = [
            {"A": "01", "C": "11", "T": "00", "G": "10"},
            {"A": "00", "C": "10", "T": "01", "G": "11"},
            {"A": "00", "C": "01", "T": "10", "G": "11"},
            {"A": "01", "C": "00", "T": "11", "G": "10"},
            {"A": "10", "C": "11", "T": "00", "G": "01"},
            {"A": "11", "C": "01", "T": "10", "G": "00"},
            {"A": "11", "C": "10", "T": "01", "G": "00"},
            {"A": "10", "C": "00", "T": "11", "G": "01"}
        ]

        # Convert DNA to bin
        out = '0b'
        for i in range(0, len(bin), 1):
            out = int(out + rules[rule][bin[i:i+1]], 2)
        return out

    # DNA EXOR

    # DNA ADD

    # DNA SUB