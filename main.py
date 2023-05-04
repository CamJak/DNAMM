# DNAMM Main file
from dna import *

def main():
    ## Generate key

    ## Encrypt plaintext
    # Convert to DNA
    inputText = "Hello World!"
    test = DNA(inputText)
    # Create DNAMM
    # Use DNAMM to further encrypt DNA

    ## Decrypt ciphertext
    # Convert to ASCII

    print("Text to be encrypted: {}\n".format(inputText))
    print("Text as DNA: {}\n".format(test))

    return None # End main()

if __name__ == "__main__":
    main()