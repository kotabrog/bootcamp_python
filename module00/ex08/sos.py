import sys
import itertools

morse_table = {
    'A': '.-', 'a': '.-',
    'B': '-...', 'b': '-...',
    'C': '-.-.', 'c': '-.-.',
    'D': '-..', 'd': '-..',
    'E': '.', 'e': '.',
    'F': '..-.', 'f': '..-.',
    'G': '--.', 'g': '--.',
    'H': '....', 'h': '....',
    'I': '..', 'i': '..',
    'J': '.---', 'j': '.---',
    'K': '-.-', 'k': '-.-',
    'L': '.-..', 'l': '.-..',
    'M': '--', 'm': '--',
    'N': '-.', 'n': '-.',
    'O': '---', 'o': '---',
    'P': '.--.', 'p': '.--.',
    'Q': '--.-', 'q': '--.-',
    'R': '.-.', 'r': '.-.',
    'S': '...', 's': '...',
    'T': '-', 't': '-',
    'U': '..-', 'u': '..-',
    'V': '...-', 'v': '...-',
    'W': '.--', 'w': '.--',
    'X': '-..-', 'x': '-..-',
    'Y': '-.--', 'y': '-.--',
    'Z': '--..', 'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}

argv = sys.argv
if len(argv) == 1:
    sys.exit()
text_list = [text.split() for text in argv[1:]]
word_list = list(itertools.chain(*text_list))
try:
    morse_list = [' '.join([morse_table[c] for c in w]) for w in word_list]
    print(' / '.join(morse_list))
except Exception:
    print('ERROR')