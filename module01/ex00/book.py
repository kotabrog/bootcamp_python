import sys
import datetime
from typing import Dict
from recipe import Recipe


class BookError(Exception):
    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return "Book Error\n" + self.text


class Book:
    def __init__(self, name: str):
        try:
            if type(name) is not str or name == '':
                raise BookError("Enter name as str type. However, "
                                + "an empty string will not be accepted.")
        except BookError as e:
            print(e)
            sys.exit()

        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = self.last_update
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""

        if type(name) is not str:
            print(BookError('Give str type to "get_recipe_by_name".'))
            sys.exit()
        for value in self.recipes_list.values():
            for recipe in value:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(BookError('{} is not in the book'.format(name)))
        sys.exit()

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """

        if recipe_type != 'starter' and recipe_type != 'lunch'\
           and recipe_type != 'dessert':
            print(BookError('recipe_type can be "starter", '
                            + '"lunch" or "dessert".'))
            sys.exit()
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""

        if type(recipe) is not Recipe:
            print(BookError('recipe type must be Recipe.'))
            sys.exit()
        self.recipes_list[recipe.recipe_type].append(recipe)
