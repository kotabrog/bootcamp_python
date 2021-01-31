import sys

cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def add_recipe(name, ingredients, meal, prep_time):
    try:
        time = int(prep_time)
    except Exception:
        return 1

    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': time
    }
    return 0


def delete_recipe(name):
    try:
        del cookbook[name]
    except KeyError:
        return 1

    return 0


def print_recipe(name):
    try:
        recipe = cookbook[name]
    except KeyError:
        return 1

    print('Recipe for {}:'.format(name))
    print('Ingredients list: {}'.format(recipe['ingredients']))
    print('To be eaten for {}.'.format(recipe['meal']))
    print('Takes {} minutes of cooking.'.format(recipe['prep_time']))
    print()
    return 0


def print_all():
    if len(cookbook.keys()) == 0:
        print('There is no recipe.\n')
        return
    for key in cookbook.keys():
        print_recipe(key)


def ignore_empty_input():
    s = input()
    while s == '':
        s = input()
    return s


repeat_flag = False
while True:
    if repeat_flag:
        print('This option does not exist, '
              + 'please type the corresponding number.')
        print('To exit, enter 5.')
    else:
        print('Please select an option by typing the corresponding number:')
        print('1: Add a recipe')
        print('2: Delete a recipe')
        print('3: Print a recipe')
        print('4: Print the cookbook')
        print('5: Quit')

    num = input()
    print()
    repeat_flag = False

    if num == '1':
        print('Enter the name of the recipe you want to add:')
        name = ignore_empty_input()
        print('Enter the ingredients, separated by spaces:')
        print('Example: ham bread cheese tomatoes')
        ingredients = ignore_empty_input().split()
        print('Enter the type of meal:')
        meal = ignore_empty_input()
        print('Enter the preparation time in minutes:')
        prep_time = ignore_empty_input()
        while add_recipe(name, ingredients, meal, prep_time):
            print('Please enter a number for the preparation time.')
            print('Enter the preparation time in minutes:')
            prep_time = ignore_empty_input()
        print('Added.\n')
    elif num == '2':
        print('Enter the name of the recipe you want to delete:')
        name = ignore_empty_input()
        if delete_recipe(name):
            print("I don't have that recipe.\n")
        else:
            print('Deleted.\n')
    elif num == '3':
        print("Please enter the recipe's name to get its details:")
        name = ignore_empty_input()
        if print_recipe(name):
            print("I don't have that recipe.\n")
    elif num == '4':
        print_all()
    elif num == '5':
        print('Cookbook closed.')
        sys.exit()
    else:
        repeat_flag = True
