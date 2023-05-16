# DNAMM
Project implementing a DNA Moore Machine in Python for CYEN 480.

## Usage
```bash
python3 main.py [-h] [-D] [-d] [-e] [-i INPUT] [-k KEY] [-o OUTPUT] [-v]
```

## Arguments
| Argument | Description |
| --- | --- |
| -h, --help | Show this help message and exit |
| -D, --demo | Run the Demo |
| -d, --decrypt | Decrypt the input file |
| -e, --encrypt | Encrypt the input file |
| -i INPUT, --input INPUT | Input file |
| -k KEY, --key KEY | Key file |
| -o OUTPUT, --output OUTPUT | Output file |
| -v, --verbose | Print verbose information |

## Examples
### Demo
```bash
python3 main.py -D
```

### Encrypt
```bash
python3 main.py -e -i input.txt -k key.key -o output.dna
```
Here the -k argument is optional. If not provided, the program will output the key to a file using the name provided in the -i argument.

### Decrypt
```bash
python3 main.py -d -i input.dna -k key.key -o output.txt
```

## Authors
* **[Cameron Thomas](https://github.com/CamJak)**
* **[Blake Perrin](https://github.com/BlakePerrin13)**
* **[William Wilson]**

## Credits
The inspiration for this project came from [this paper](https://www.sciencedirect.com/science/article/abs/pii/S0140366422000457).
