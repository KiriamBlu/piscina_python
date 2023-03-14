from sys import argv
import string

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', ' ': '/'
}

try:
    argv.pop(0)
    string = ""
    for i, select in enumerate(argv):
        for j, char in enumerate(select):
            if char.upper() not in morse_dict:
                raise TypeError("ERROR: " + char)
            elif char != ' ':
                string = string + str(morse_dict[char.upper()]) + " "
            else:
                string = string + " " + str(morse_dict[char]) + " "
            if j == len(select) - 1 and i != len(argv) - 1:
                string = string + " / "

    print(string)
except TypeError as e:
    print(e)
