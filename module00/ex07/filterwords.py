from string import punctuation
import sys

argv = sys.argv
if len(argv) != 3:
    print('ERROR')
else:
    try:
        n = int(argv[2])
    except Exception:
        print('ERROR')
        sys.exit()
    table = str.maketrans("", "", punctuation)
    word_list = [word.translate(table) for word in argv[1].split()]
    word_list = [word for word in word_list if len(word) > n]
    if len(word_list) == 0:
        print('ERROR')
    else:
        print(word_list)
