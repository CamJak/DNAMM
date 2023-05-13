# DNAMM Main file
from dna import *
from mm import *
from helperFunctions import *
import sys
from argparse import ArgumentParser

def encrypt(filename, output, key=None, verbose=False):
    if output == None:
        output = filename + ".dna"
    if key == None:
        key = filename + ".key"

    with open(filename, "r") as f:
        inputText = f.read()

        if verbose:
            print(f"Text to be encrypted: {inputText}\n")

        dna = DNA(inputText)
        firstRule = dna.getFirstRule()

        if verbose:
            print(f"DNA before Moore Machine: {dna}\n")
        
        mm = MooreMachine()
        mm.generate()

        if verbose:
            print(f"Generated Moore Machine: \n{mm}")

        outputMM = mm.getOutput(dna.getDna())

        if verbose:
            print(f"DNA after Moore Machine: {outputMM}\n")

        binMM = mm.encodeCols(mm.getCols())

        if verbose:
            print(f"Binary Encoded Moore Machine: {binMM}")

        dnaMM = DNA().bin_to_dna(binMM, 1)
        
        if verbose:
            print(f"DNA Encoded Moore Machine: {dnaMM}\n")
        
        with open(output, "w") as f:
            f.write(dnaMM + outputMM)
        
        with open(key, "w") as f:
            f.write(str(firstRule))
        
        if verbose:
            print(f"Encrypted file saved to {output}")
            print(f"Key file saved to {key}")

def encrypt_text(output, key=None, verbose=False):
    if output == None:
        print("Error: No output file specified. Exiting...")
        sys.exit(1)
    if key == None:
        key = output + ".key"

    inputText = input("Enter text to be encrypted: ")

    if verbose:
        print()
        print(f"Text to be encrypted: {inputText}\n")

    dna = DNA(inputText)
    firstRule = dna.getFirstRule()

    if verbose:
        print(f"DNA before Moore Machine: {dna}\n")
    
    mm = MooreMachine()
    mm.generate()

    if verbose:
        print(f"Generated Moore Machine: \n{mm}")

    outputMM = mm.getOutput(dna.getDna())

    if verbose:
        print(f"DNA after Moore Machine: {outputMM}\n")

    binMM = mm.encodeCols(mm.getCols())

    if verbose:
        print(f"Binary Encoded Moore Machine: {binMM}")

    dnaMM = DNA().bin_to_dna(binMM, 1)
    
    if verbose:
        print(f"DNA Encoded Moore Machine: {dnaMM}\n")
    
    with open(output, "w") as f:
        f.write(dnaMM + outputMM)
    
    with open(key, "w") as f:
        f.write(str(firstRule))
    
    if verbose:
        print(f"Encrypted file saved to {output}")
        print(f"Key file saved to {key}")

def decrypt(input, output, key, verbose=False):
    if output == None:
        output = input + ".txt"
    if key == None:
        print("Error: No key file specified. Exiting...")
        sys.exit(1)

    with open(input, "r") as f:
        data = f.read()
        dnaMM = data[0:16]
        inputText = data[16:]

        if verbose:
            print(f"DNA Encoded Moore Machine: {dnaMM}\n")
            print(f"DNA to be decrypted: {inputText}\n")

        decodedMM = DNA().dna_to_bin(dnaMM, 1)
        firstRule = int(open(key, "r").read())

        if verbose:
            print(f"Decoded MM: {decodedMM}\n")
        
        mm = MooreMachine()
        mm.generateFromCols(mm.decodeCols(decodedMM))

        if verbose:
            print(f"Generated Moore Machine: \n{mm}")

        reverseMM = mm.getReverseOutput(inputText)

        if verbose:
            print(f"DNA after reversing the Moore Machine: {reverseMM}\n")

        decodedDNA = DNA().dna_to_bin(reverseMM, firstRule)

        decodedASCII = binToAscii(decodedDNA)
        
        with open(output, "w") as f:
            f.write(decodedASCII)
        
        if verbose:
            print(f"Decoded ASCII: {decodedASCII}\n")
            print(f"Decrypted file saved to {output}\n")

def demo():
    inputText = input("Enter text to be encrypted: ")

    print()
    print("Text to be encrypted: {}\n".format(inputText))

    print("Starting Encryption...\n")
    
    dna = DNA(inputText)
    firstRule = dna.getFirstRule()

    print(f"DNA before Moore Machine: {dna}\n")

    mm = MooreMachine()
    mm.generate()
    print(f"Generated Moore Machine: \n{mm}")

    # Use DNAMM to further encrypt DNA
    outputMM = mm.getOutput(dna.getDna())
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
    print(f"Decoded ASCII: {decodedASCII}\n")

def main():

    parser = ArgumentParser()
    parser.add_argument("-D", "--demo", dest="demo", help="Run demo", action="store_true")
    parser.add_argument("-d", "--decrypt", dest="decrypt", help="Decrypt file", action="store_true")
    parser.add_argument("-e", "--encrypt", dest="encrypt", help="Encrypt file", action="store_true")
    parser.add_argument("-i", "--input", dest="input", help="File to be encrypted or decrypted")
    parser.add_argument("-k", "--key", dest="key", help="Key file")
    parser.add_argument("-o", "--output", dest="output", help="Output file")
    parser.add_argument("-v", "--verbose", dest="verbose", help="Verbose output", action="store_true")
    args = parser.parse_args()

    if args.encrypt and not args.decrypt:
        print("Encrypting...\n")
        encrypt(args.input, args.output, args.key, args.verbose)
        print("Done!")
    elif args.decrypt and not args.encrypt:
        print("Decrypting...\n")
        decrypt(args.input, args.output, args.key, args.verbose)
        print("Done!")
    elif args.demo:
        print("Running demo...\n")
        demo()
    elif args.input == None:
        print("Encrypting...\n")
        encrypt_text(args.output, args.key, args.verbose)
        print("Done!")
    else:
        parser.print_help()

    return None # End main()

if __name__ == "__main__":
    main()