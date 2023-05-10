# DNAMM Main file
from dna import *
from mm import *
from helperFunctions import *

def main():
    ## Generate key

    ## Encrypt plaintext
    # Convert to DNA
    inputText = input("Enter text to be encrypted: ")
    print("Text to be encrypted: {}\n".format(inputText))

    print("Starting Encryption...\n")
    
    test = DNA(inputText)
    firstRule = test.getFirstRule()
    print(f"DNA before Moore Machine: {test}\n")

    # Create DNAMM
    mm = MooreMachine()
    mm.generate()
    print(f"Generated Moore Machine: \n{mm}")

    # Use DNAMM to further encrypt DNA
    outputMM = mm.getOutput(test.getDna())
    print(f"DNA after Moore Machine: {outputMM}\n")

    # Encode the Moore Machine into DNA
    binMM = mm.encodeCols(mm.getCols())
    print(f"Binary Encoded Moore Machine: {binMM}")

    dnaMM = DNA().bin_to_dna(binMM, 1)
    print(f"DNA Encoded Moore Machine: {dnaMM}\n")
    
    # Decryption...
    print("Starting Decryption...\n")

    # Decode the Moore Machine
    decodedMM = DNA().dna_to_bin(dnaMM, 1)
    print(f"Decoded MM: {decodedMM}\n")

    # Create Moore Machine from decoded Moore Machine
    mm2 = MooreMachine()
    mm2.generateFromCols(mm2.decodeCols(decodedMM))
    print(f"Generated Moore Machine: \n{mm2}")

    # Use Moore Machine to decrypt DNA
    reverseMM = mm2.getReverseOutput(outputMM)
    print(f"DNA after reversing the Moore Machine: {reverseMM}\n")

    # Decode DNA back to binary based on the rules used to encode it
    decodedDNA = DNA().dna_to_bin(reverseMM, firstRule)

    # Convert binary to ASCII
    decodedASCII = binToAscii(decodedDNA)
    print(f"Decoded ASCII: {decodedASCII}")

    return None # End main()

if __name__ == "__main__":
    main()