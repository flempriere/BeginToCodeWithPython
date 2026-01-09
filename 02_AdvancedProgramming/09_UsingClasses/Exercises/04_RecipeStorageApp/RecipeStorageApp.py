# Exercise 9.4 Recipe Storage App
#
# A simple recipe storage app that stores recipes
# as a list of ingedients and a list of steps

import pickle

import BTCInput


class Recipe:
    """
    Represent a cooking recipe.

    Attributes
    ----------
    name : str
        Recipe name

    ingredients : dict[str, list[str]]
        Ingredients required for the recipe. Ingredients are stored
        as a dictionary in the format `ingredients[ingredient] = ["description", ...]`

    steps: list[str]
        Ordered list of instructions/steps to prepare the recipe.

    Example
    -------
    >>> Recipe("Omelette", {"eggs" : [2], "milk": ["1 cup"]}, ["Beat eggs", "Add milk", "Cook on pan"])
    """

    def __init__(self, name, ingredients, steps):
        """
        Create a new Recipe instance

        Parameters
        ----------
        name : str
            Name of the Recipe
        ingredients : dict[str, list[str]]
            Ingredients required for the recipe. Ingredients are stored
            as a dictionary in the format `ingredients[ingredient] = ["description", ...]`
            e.g. `ingredients["Brown Onion"] = ["1 Medium, diced"]`
        steps : list[str]
            Ordered list of instructions/steps to prepare the recipe.
        """
        self.name = name
        self.ingredients = ingredients
        self.steps = steps


def get_ingredients():
    """
    Gets a dictionary of ingredients from the user.

    Ingredients are processed
    as key, value pairs of ingredients and descriptions such as their quantity
    or how they are to be prepared.

    Supports duplicates for an ingredient. If a duplicate is detected the
    user will be prompted if they wish to overwrite the existing key, value
    pair, add the description to the pair or ignore the current entry

    Returns
    -------
    dict[str, list[str]]
        Dictionary of Ingredient, description pairs. The dictionary is
        keyed by ingredients and the descriptions are stored as a list
        of strings

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered
    """
    ingredients = {}
    while True:
        ingredient = BTCInput.read_text("Enter next ingredient or . to stop: ")
        if ingredient == ".":
            break
        if ingredient in ingredients:
            print("That ingredient is already included!")
            duplicate_choice = BTCInput.read_int_ranged(
                "Overwrite (2), append (1) or forget (0)?: ", min_value=0, max_value=2
            )
            if duplicate_choice == 0:
                continue  # ignore this entry and move to the next
            elif duplicate_choice == 1:
                pass  # for append behave normally
            elif duplicate_choice == 2:
                del ingredients[ingredient]  # remove existing ingredients
            else:
                raise ValueError(
                    "Invalid value "
                    + str(duplicate_choice)
                    + "encountered resolving duplicate ingredient"
                )
        ingredient_description = BTCInput.read_text("Enter quantity and description: ")
        if ingredient in ingredients:
            ingredients[ingredient].append(ingredient_description)
        else:
            ingredients[ingredient] = [ingredient_description]

    return ingredients


def get_steps():
    """
    Gets the steps for the recipe from the user.

    Steps are entered and stored as an ordered list.

    Returns
    -------
    list[str]
        list of strings containing the ordered steps to follow for a recipe
    """
    steps = []
    while True:
        step = BTCInput.read_text("Enter next recipe step or . to stop: ")
        if step == ".":
            break
        steps.append(step)
    return steps


def new_recipe():
    """
    Add a new recipe to the recipe database.

    A recipe consists of a name, dictionary of ingredients and a list of steps
    The user is prompted for the name, ingredients and the steps

    Returns
    -------
    None

    See Also
    --------
    Recipe : Class responsible for storing recipe information
    """
    print("Add New Recipe")
    name = BTCInput.read_text("Enter the recipe name: ")

    print("Enter ingredients")
    ingredients = get_ingredients()
    print("Enter Steps")
    steps = get_steps()
    recipe = Recipe(name, ingredients, steps)
    recipes.append(recipe)


def save_recipes(file_name):
    """
    Saves the Recipes to the given file

    Recipes are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file to store the recipes data in

    Returns
    -------
    None

    Raises
    ------
        An Exception is raised if the file could not be saved

    See Also
    --------
    load_recipes : load recipes from a pickled file
    """
    print("Save Recipes")
    with open(file_name, "wb") as out_file:
        pickle.dump(recipes, out_file)


def load_recipes(file_name):
    """
    Loads the recipes from the given file

    recipes are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file where the recipes data is stored

    Returns
    -------
    None
        Recipes are loaded into the global recipes list

    Raises
    ------
    An Exception is raised if the file could not be loaded

    See Also
    --------
    save_recipes : save recipes as a pickled file
    """
    print("Load Recipes")
    global recipes
    with open(file_name, "rb") as in_file:
        recipes = pickle.load(in_file)


def list_recipes(recipes):
    """
    Prints the recipe names in a given list

    Parameters
    ----------
    recipes : list[Recipe]
        list of recipes to display

    Returns
    -------
    None
    """
    print("List Recipes")
    if len(recipes) == 0:
        print("No recipes found")
        return
    for recipe in recipes:
        print("-", recipe.name)


def filter_recipe_by_name(search_name):
    """
    Finds and returns recipes whose name contains a search name

    Parameters
    ----------
    search_name : str
        name to search for, search is conducted as a substring search

    Returns
    -------
    list[Recipe]
        list of recipes whose name contains `search_name` as a substring
    """
    results = []
    search_name = search_name.strip().lower()
    for recipe in recipes:
        if recipe.name.strip().lower().find(search_name) != -1:
            results.append(recipe)
    return results


def find_recipe_by_name():
    """
    Prints all recipes matching a user-specified search

    Returns
    -------
    None
        Matches are printed to standard output

    See Also
    --------
    filter_recipe_by_name : returns a list containing recipes which match a name
    find_recipe_by_ingredient : find recipes containing a user-prompted ingredient
    """
    print("Find Recipe by Name")
    results = filter_recipe_by_name(BTCInput.read_text("Enter recipe name: "))
    list_recipes(results)


def filter_recipe_by_ingredient(search_ingredient):
    """
    Find and return a list of all recipes which contain a given ingredient

    Parameters
    ----------
    search_ingredient : str
        ingredient to search for

    Returns
    -------
    list[Recipe]
        list of Recipes containing `search_ingredient`

    Warnings
    --------
    search matching is exact on `search_ingredient`, for example if a recipe
    had the ingredient dictionary,

    `{"Bread" : ["sliced"], "chicken thighs" : ["large"]}`

    1. `filter_recipes_by_ingredient("Bread")` would match
    2. `filter_recipes_by_ingredient("bread")` would not match
    3. `filter_recipes_by_ingredient("chicken")` would not match
    """
    results = []
    for recipe in recipes:
        if search_ingredient in recipe.ingredients:
            results.append(recipe)
    return results


def find_recipe_by_ingredient():
    """
    Find and display all recipe that contain a user-specified ingredient

    Returns
    -------
        None

    Warnings
    --------
        This function uses `filter_recipe_by_ingredient` under the hood
        and so relies on exact matching for the passed ingredient

    See Also
    --------
    `filter_recipe_by_ingredient` : returns a list of all recipes matching
    a search ingredient
    `find_recipe_by_name` : finds recipes matching a name rather than ingredient
    """
    print("Find Recipe by Ingredient")
    results = filter_recipe_by_ingredient(
        BTCInput.read_text("Enter search ingredient: ")
    )
    list_recipes(results)


def run_find_recipe_menu():
    """
    Provides a looping menu interface allowing the user
    to search for recipes

    The user can find recipes either by
    1. Find Recipe by Name
        - Matches against a provided user-provided substring in the name
    2. Find Recipe by Ingredient
        - Peforms an exact match against a user-provided ingredient

    Returns
    -------
    None

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered
    """
    find_recipe_menu = """Find Recipes
1. Find Recipe by Name
2. Find Recipe by Ingredient
3. Return to Main Menu

Enter your command: """

    while True:
        command = BTCInput.read_int_ranged(find_recipe_menu, min_value=1, max_value=3)
        if command == 1:
            find_recipe_by_name()
        elif command == 2:
            find_recipe_by_ingredient()
        elif command == 3:
            break
        else:
            raise ValueError(
                "Unexpected command id "
                + str(command)
                + " encountered in find recipe menu"
            )


def run_view_recipe_menu(recipe):
    """
    Provides a looping menu interface allowing the user
    to view the details of a specific recipe

    View Options are

    1. List ingredients
        - Shows all the ingredients in a recipe
    2. View All Steps
        - Shows all the steps in a recipe
    3. Step through Recipe
        - Allows the user to interactively step through a recipe
        one step at a time

    Parameters
    ----------
    recipe : Recipe
        recipe to view

    Returns
    -------
    None

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered
    """
    header = "Current Recipe: " + recipe.name + "\n"
    view_recipe_menu = (
        header
        + """View Recipe
1. List Ingredients
2. View All Steps
3. Step through Recipe
4. Return to Main Menu

Enter your command: """
    )
    while True:
        command = BTCInput.read_int_ranged(
            prompt=view_recipe_menu, min_value=1, max_value=4
        )
        if command == 1:
            print("Ingredients")
            for ingredient in recipe.ingredients:
                print(ingredient, "-", recipe.ingredients[ingredient])
        if command == 2:
            print("View all Steps")
            for step in recipe.steps:
                print("-", step)
        if command == 3:
            print(
                "Step through Recipe"
            )  # waits for user confirmation before printing next step
            for step in recipe.steps:
                print("-", step)
                go_to_next = BTCInput.read_text("Next step? (Q - Quit): ")
                if go_to_next.strip().upper() == "Q":
                    return
        if command == 4:
            break


def view_recipes():
    """
    Provide a prompt for the user to select a recipe to view

    Reports the number of successful matches. For each match
    (if any) the user is then prompted if they wish to view
    the recipe in which case they are taken to the view
    recipe menu

    See Also
    --------
    `run_view_recipe_menu` - provides options for viewing a specific recipe
    """
    print("View Recipe")
    results = filter_recipe_by_name(BTCInput.read_text("Enter recipe to view: "))
    if len(results) == 0:
        print("No recipe found matching that name")
    else:
        print("Found", len(results), "matches")
    for recipe in results:
        print("Recipe: ", recipe.name)
        command = BTCInput.read_int_ranged(
            "View this recipe? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if command == 1:
            run_view_recipe_menu(recipe)


def edit_recipe():
    """
    Provides a prompt to the user to select a recipe to edit

    Reports the number of successful matches. For each match
    (if any) the user is prompted if they want to edit the recipe
    in which case they are provided the options to edit the name,
    ingredients or steps

    Returns
    -------
    None

    Warnings
    --------

    Edits are performed in-place and live, they cannot be rolled back

    See Also
    --------
    filter_recipe_by_name : gives a list of recipes matching a name
    """
    print("Edit Recipe")
    results = filter_recipe_by_name(BTCInput.read_text("Enter recipe to edit: "))
    if len(results) == 0:
        print("No recipe found matching that name")
    else:
        print("Found", len(results), "matches")
    for recipe in results:
        print("Recipe:", recipe.name)
        command = BTCInput.read_int_ranged(
            "Edit this recipe? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if command == 0:
            continue
        new_name = BTCInput.read_text("Enter new name or . to leave unchanged: ")
        if new_name != ".":
            recipe.name = new_name
        should_edit_ingredients = BTCInput.read_int_ranged(
            "Edit ingredients? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if should_edit_ingredients:
            recipe.ingredients = get_ingredients()
        should_edit_steps = BTCInput.read_int_ranged(
            "Edit steps? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if should_edit_steps:
            recipe.steps = get_steps()


def remove_recipe():
    """
    Remove a recipe from the database

    Prompts the user to select a recipe to match.
    Reports the number of successful matches. For each match
    (if any) the user is prompted if they want to remove the recipe

    Returns
    -------
    None

    See Also
    --------
    filter_recipe_by_name : gives a list of recipes matching a name
    """
    print("Remove Recipe")
    results = filter_recipe_by_name(BTCInput.read_text("Enter recipe to remove: "))
    if len(results) == 0:
        print("No recipe found matching that name")
    else:
        print("Found", len(results), "matches")
    for recipe in results:
        print("Recipe:", recipe.name)
        command = BTCInput.read_int_ranged(
            "View this recipe? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if command == 1:
            recipes.remove(recipe)


file_name = "recipes.pickle"

try:
    load_recipes(file_name)
except:  # noqa: E722
    print("Failed to load recipe file")
    recipes = []

menu = """Recipe Storage

1. Add a New Recipe
2. List Recipes
3. Find Recipe Menu
4. View Recipe
5. Edit Recipe
6. Remove Recipe
7. Exit the Program

Enter your command: """

while True:
    command = BTCInput.read_int_ranged(prompt=menu, min_value=1, max_value=7)
    if command == 1:
        new_recipe()
    elif command == 2:
        list_recipes(recipes)  # type: ignore
    elif command == 3:
        run_find_recipe_menu()
    elif command == 4:
        view_recipes()
    elif command == 5:
        edit_recipe()
    elif command == 6:
        remove_recipe()
    elif command == 7:
        try:
            save_recipes(file_name)
        except:  # noqa: E722
            print("Failed to save recipes")
        break
    else:
        raise ValueError("Unexpected command id " + str(command))
