from book import Book
from recipe import Recipe

recipe1 = Recipe('name', 1, 1, ["ingredients", "ingred"], "starter")
recipe2 = Recipe('name2', 1, 1, ["ingredients", "ingred"], "dessert")
# recipe = Recipe('name', 1, 1, ["ingredients", "ingred"], "starter", 'des')
# recipe = Recipe('', 1, 1, ["ingredients", "ingred"], "starter")
# recipe = Recipe(1, 1, 1, ["ingredients", "ingred"], "starter")
# recipe = Recipe('name', 0, 1, ["ingredients", "ingred"], "starter")
# recipe = Recipe('name', 7.2, 1, ["ingredients", "ingred"], "starter")
# recipe = Recipe('name', 'a', 1, ["ingredients", "ingred"], "starter")
# recipe = Recipe('name', 1, -1, ["ingredients", "ingred"], "starter")
# recipe = Recipe('name', 1, "a", ["ingredients", "ingred"], "starter")
# recipe = Recipe('name', 1, 1, "s", "starter")
# recipe = Recipe('name', 1, 1, ["ingredients", ""], "starter")
# recipe = Recipe('name', 1, 1, ["ingredients", 2], "starter")
# recipe = Recipe('name', 1, 1, ["ingredients"], "a")
# recipe = Recipe('name', 1, 1, ["ingredients"], 2)
# recipe = Recipe('name', 1, 1, ["ingredients"], "")
# recipe = Recipe('name', 1, 1, ["ingredients"], "starter", 1)

# book = Book(1)
# book = Book('')
book = Book('name')

book.add_recipe(recipe1)
book.add_recipe(recipe2)
# book.add_recipe(book)

recipe = book.get_recipe_by_name('name')
# recipe = book.get_recipe_by_name('name2')
# recipe = book.get_recipe_by_name('name3')
# recipe = book.get_recipe_by_name(1)
print('---')
print(recipe)
recipes = book.get_recipes_by_types("starter")
print('-- starter --')
for recipe in recipes:
    print(recipe)
recipes = book.get_recipes_by_types("lunch")
print('-- lunch --')
for recipe in recipes:
    print(recipe)
recipes = book.get_recipes_by_types("dessert")
print('-- dessert --')
for recipe in recipes:
    print(recipe)
# recipes = book.get_recipes_by_types("hello")

# print(recipe)
