import sys
from random import randint


def _shuffle_index(size):
    shuffle_indexes = []
    while len(shuffle_indexes) != size:
        num = randint(0, size - 1)
        if num not in shuffle_indexes:
            shuffle_indexes.append(num)
    return shuffle_indexes


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if type(text) is not str or type(sep) is not str:
        split_text = ['ERROR']
    else:
        split_text = [word for word in text.split(sep) if word != '']
        if len(split_text) == 0:
            pass
        elif option == 'ordered':
            split_text.sort()
        elif option == 'unique':
            split_text = list(dict.fromkeys(split_text))
        elif option == 'shuffle':
            shuffle_indexes = _shuffle_index(len(split_text))
            split_text = [t[0] for t in
                          sorted(list(zip(split_text, shuffle_indexes)),
                          key=lambda t: t[1])]
        elif option:
            split_text = ['ERROR']
    for word in split_text:
        yield word


if __name__ == '__main__':
    # text = "Le Lorem Ipsum est simplement du faux texte."
    # text = 1
    # text = "Le Lorem Le Lorem"
    text = "Le Lorem    Le   Lorem  Le"
    # text = " "
    sep = ' '
    # sep = 1
    # option = 'ordered'
    # option = 'unique'
    # option = 'shuffle'
    # option = 'ordere'
    for word in generator(text, sep):
        print(word)
    # for word in generator(text, sep, option):
    #     print(word)
