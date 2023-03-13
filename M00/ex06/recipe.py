class Recipe():
	def __init__(self, ingredients, meal, preptime):
		self.ingredients = ingredients
		self.meal = meal
		self.preptime = preptime


class cookbook:
	def __init__(self):
		self.recipes = {
			"bocadillo": Recipe(["jamón", "pan", "queso", "tomate"], "almuerzo", 10),
			"tarta": Recipe(["harina", "azúcar", "huevos"], "postre", 60),
			"ensalada": Recipe(["aguacate", "rúcula", "tomates", "espinacas"], "almuerzo", 15)
		}

	def add_recipe(self, name, ingredients, meal, prep_time):
		self.recipes[name] = Recipe(ingredients, meal, prep_time)
		print(f"Receta '{name}' agregada al libro de cocina.")

	def add_manual_recipe(self):
		name = input("Ingresa el nombre de la receta: ")
		ingredients = []
		while True:
			ingredient = input("Ingresa un ingrediente (o presiona Enter para finalizar): ")
			if not ingredient:
				break
			ingredients.append(ingredient)
		meal = input("Ingresa el tipo de comida: ")
		prep_time = int(input("Ingresa el tiempo de preparación (en minutos): "))
		self.add_recipe(name, ingredients, meal, prep_time)

	def delete_recipe(self, name):
		if name in self.recipes:
			del self.recipes[name]
			print(f"Receta '{name}' eliminada del libro de cocina.")
		else:
			print(f"La receta '{name}' no existe en el libro de cocina.")

	def get_recipe(self, name):
		recipe = self.recipes.get(name)
		if recipe:
			print(f"Receta: {name}")
			print(f"Ingredientes: {recipe.ingredients}")
			print(f"Tipo de comida: {recipe.meal}")
			print(f"Tiempo de preparación: {recipe.preptime} minutos")
		else:
			print(f"La receta '{name}' no existe en el libro de cocina.")

	def print_cookbook(self):
		print("Recetas en el libro de cocina:")
		for name, recipe in self.recipes.items():
			print(f"Nombre: {name}")
			print(f"Ingredientes: {recipe.ingredients}")
			print(f"Tipo de comida: {recipe.meal}")
			print(f"Tiempo de preparación: {recipe.preptime} minutos")
			print("\n")

if __name__ == "__main__":
	Cookbook = cookbook()
	while True:
		print("List of available options:\n\t1: Add a recipe\n\t2: Delete a recipe\n\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit")
		try:
			selec = int(input("Please select an option: "))
			if selec == 1:
				Cookbook.add_manual_recipe()
			elif selec == 2:
				recipe_name = input("Enter the name of the recipe to delete: ")
				Cookbook.delete_recipe(recipe_name)
			elif selec == 3:
				recipe_name = input("Enter the name of the recipe to print: ")
				recipe = Cookbook.get_recipe(recipe_name)
				if recipe is not None:
					print(recipe.name)
					print("Ingredients: {}".format(", ".join(recipe.ingredients)))
					print("Meal: {}".format(recipe.meal))
					print("Preparation time: {} minutes".format(recipe.preptime))
				else:
					print("Recipe not found")
			elif selec == 4:
				for recipe_name, recipe in Cookbook.recipes.items():
					print(recipe_name)
					print("Ingredients: {}".format(", ".join(recipe.ingredients)))
					print("Meal: {}".format(recipe.meal))
					print("Preparation time: {} minutes".format(recipe.preptime))
			elif selec == 5:
				break
			else:
				print("Invalid option selected")
	
		except ValueError:
			print("Please enter a valid option")




