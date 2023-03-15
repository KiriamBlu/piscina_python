import datetime
import recipe

class Book():
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.datetime.now()
		self.creation_time = datetime.datetime.now()
		self.recipes = {"starter": [], "lunch": [], "dessert": []}

	def get_recipe_by_name(self, name):
		"""Imprime la receta con el nombre name y devolver la instancia"""
		for recipes_list in self.recipes.values():
			for recipe in recipes_list:
				if recipe.name == name:
					return recipe
		return None

	def get_recipes_by_types(self, recipe_type):
		"""Devuelve todas las recetas dado un recipe_type"""
		if recipe_type in ["starter", "lunch", "dessert"]:
			return [element for element in self.recipes[recipe_type]]
		else:
			return []

	def add_recipe(self, recipe):
		"""Añade una receta al libro y actualiza last_update"""
		if self.get_recipe_by_name(recipe.name):
			raise ValueError(f"Recipe '{recipe.name}' already exists in the book.")
		else:
			self.recipes[recipe.recipe_type].append(recipe)
			self.last_update = datetime.datetime.now()
