# DNAMM Main file
from dna import *
from mm import *
from helperFunctions import *

def main():
    ## Generate key

    ## Encrypt plaintext
    # Convert to DNA
    inputText = "Hello World!"
    print("Text to be encrypted: {}\n".format(inputText))

    test = DNA(inputText)
    firstRule = test.getFirstRule()

    print(f"DNA before Moore Machine: {test}")

    # Create DNAMM
    mm = MooreMachine()
    mm.generate()

    # Use DNAMM to further encrypt DNA
    output = mm.getOutput(test.getDna())
    print(f"DNA after Moore Machine: {output}")
    print()

    binMM = mm.encodeCols(mm.getCols())
    print(f"Binary encoded MM: {binMM}")

    dnaMM = DNA().bin_to_dna(binMM, 1)
    print(f"DNA encoded MM: {dnaMM}")
    print()

    decodedMM = DNA().dna_to_bin(dnaMM, 1)
    print(f"Decoded MM: {decodedMM}")

    reverseMM = mm.getReverseOutput(output)
    print(f"DNA after reverse Moore Machine: {reverseMM}")
    print()
    decodedDNA = DNA().dna_to_bin(reverseMM, firstRule)
    print(f"Decoded Binary: {decodedDNA}")

    decodedASCII = binToAscii(decodedDNA)
    print(f"Decoded ASCII: {decodedASCII}")

    ## Decrypt ciphertext
    # Convert to ASCII

    return None # End main()

if __name__ == "__main__":
    main()