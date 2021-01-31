from collections import Counter
from string import punctuation


def text_analyzer(text=None, *args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.

    Parameters
    ----------
    text : str, default None
        Target text.

    Notes
    -----
    If there are two or more arguments, "ERROR" will be printed.
    If the argument is not of type string, "ERROR" will also be printed.
    If there is no text passed to the function,
    the user is prompted to give one.
    """
    if text is None:
        print('What is the text to analyse?')
        text = input()
    if type(text) is not str or len(args) > 0:
        print('ERROR')
    else:
        text_counter = Counter('upper' if c.isupper()
                               else 'lower' if c.islower()
                               else 'space' if c.isspace()
                               else 'punctuation' if c in punctuation
                               else 'none' for c in text)
        print('The text contains {} characters:\n'.format(len(text))
              + '- {} upper letters\n'.format(text_counter['upper'])
              + '- {} lower letters\n'.format(text_counter['lower'])
              + '- {} punctuation marks\n'.format(text_counter['punctuation'])
              + '- {} spaces'.format(text_counter['space']))
