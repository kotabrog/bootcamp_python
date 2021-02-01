from random import randint
import sys

ans = randint(1, 99)

start_str = '''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n'''
input_str = "What's your guess between 1 and 99?"
high_str = "Too high!"
low_str = "Too low!"
not_input_str = "That's not a number."
clear_str = "Congratulations, you've got it!"
special_str = "The answer to the ultimate question of life, "\
              + "the universe and everything is 42."
first_str = "Congratulations! You got it on your first try!"
exit_str = "Goodbye!"

print(start_str)
try_count = 0
while True:
    print(input_str)
    num_str = input()
    if num_str == 'exit':
        print(exit_str)
        sys.exit()
    try_count += 1
    try:
        num = int(num_str)
    except Exception:
        print(not_input_str)
        continue
    if num == ans:
        if ans == 42:
            print(special_str)
        if try_count == 1:
            print(first_str)
        else:
            print(clear_str)
            print('You won in {} attempts!'.format(try_count))
        sys.exit()
    elif num < ans:
        print(low_str)
    else:
        print(high_str)
