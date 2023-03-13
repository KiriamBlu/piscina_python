import sys
import string


args = sys.argv[1:]
if len(args) == 2 and isinstance(args[0], str) and args[1].isdigit():
    sentence = args[0]
    length = int(args[1])
    words = sentence.translate(str.maketrans('', '', string.punctuation)).split()
    long_words = [word for word in words if len(word) >= length]
    print(long_words)
else:
    print("ERROR")