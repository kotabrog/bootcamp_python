import sys


class GCError(Exception):
    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return "GotCharacter Error\n" + self.text


class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        try:
            if type(first_name) is not str or first_name == '':
                raise GCError("Enter name as str type. However, "
                              + "an empty string will not be accepted.")
            if type(is_alive) is not bool:
                raise GCError('Enter is_alive as str type.')
        except GCError as e:
            print(e)
            sys.exit()
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    '''
    A class representing the Stark family.
    Or when bad things happen to good people.
    '''
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
