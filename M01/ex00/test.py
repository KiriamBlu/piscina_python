from recipe import Recipe
from book import Book

if __name__ == "__main__":
    r1 = Recipe("Pasta Carbonara", "3", 30, ["pasta", "bacon", "eggs", "cheese", "pepper"], "A classic Italian dish", "lunch")
    r2 = Recipe("Tiramisu", "2", 45, ["ladyfingers", "mascarpone", "eggs", "sugar", "coffee", "cocoa powder"], "A classic Italian dessert", "dessert")
    r3 = Recipe("Gazpacho", "1", 10, ["tomatoes", "pepper", "cucumber", "garlic", "bread", "olive oil", "vinegar"], "A refreshing Spanish soup", "starter")
    
    b = Book("My Recipe Book")
    
    b.add_recipe(r1)
    b.add_recipe(r2)
    b.add_recipe(r3)
    
    starters = b.get_recipes_by_types("starter")
    lunches = b.get_recipes_by_types("lunch")
    desserts = b.get_recipes_by_types("dessert")
    
    print("Starters:")
    for s in starters:
        print(s)
    print("Lunches:")
    for l in lunches:
        print(l)
    print("Desserts:")
    for d in desserts:
        print(d)
    
    r = b.get_recipe_by_name("Pasta Carbonara")
    print("Pasta Carbonara recipe:")
    print(r)
    
    try:
        b.add_recipe(r1)
    except ValueError as e:
        print(e)
        
    