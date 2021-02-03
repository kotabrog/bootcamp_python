from typing import List
import sys


class RecipeError(Exception):
    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return "Recipe Error\n" + self.text


class Recipe:
    def __init__(self, name: str,
                 cooking_lvl: int,
                 cooking_time: int,
                 ingredients: List[str],
                 recipe_type: str,
                 description: str = ""):
        try:
            if type(name) is not str or name == '':
                raise RecipeError("Enter name as str type. However, "
                                  + "an empty string will not be accepted.")
            if type(cooking_lvl) is not int \
               or cooking_lvl < 1 or 5 < cooking_lvl:
                raise RecipeError("Enter cooking_lvl as int type "
                                  + "and between 1 and 5.")
            if type(cooking_time) is not int or cooking_time < 0:
                raise RecipeError("Enter cooking_time as int type "
                                  + "and no negative numbers")
            if type(ingredients) is not list or len(ingredients) == 0:
                raise RecipeError("Enter ingredients as list of str type"
                                  + "and is not empty.")
            for element in ingredients:
                if type(element) is not str or element == "":
                    raise RecipeError("The material type must be str "
                                      + "and not an empty string.")
            if recipe_type != 'starter' and recipe_type != 'lunch'\
               and recipe_type != 'dessert':
                raise RecipeError('recipe_type can be "starter", '
                                  + '"lunch" or "dessert".')
            if type(description) is not str:
                raise RecipeError('description type must be str')
        except RecipeError as e:
            print(e)
            sys.exit()
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        text = 'name: {}\n'.format(self.name)\
                + 'cooking_lvl: {}\n'.format(self.cooking_lvl)\
                + 'cooking_time: {}\n'.format(self.cooking_time)\
                + 'ingredients: {}\n'.format(self.ingredients)\
                + 'recipe_type: {}\n'.format(self.recipe_type)\
                + 'description: {}'.format(self.description)
        return text
