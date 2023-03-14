
class Recipe():
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		try:
			if isinstance(name, str) and cooking_lvl.isdigit() and isinstance(ingredients, list) and all(isinstance(i, str) for i in ingredients) and isinstance(recipe_type, str):
				self.name = name
				self.cooking_lvl = cooking_lvl
				self.cooking_time = cooking_time
				self.ingredients = ingredients
				self.description = description
				self.recipe_type = recipe_type
			else:
				raise TypeError("Invalid argument types")
		except TypeError as e:
			print(e)

	def __str__(self):
		"""Return the string to print with the recipe info"""
		"""Your code here"""
		txt = f"{self.name} ({self.recipe_type} - level {self.cooking_lvl})\n"
		txt += f"Ingredients: {', '.join(self.ingredients)}\n"
		txt += f"Cooking time: {self.cooking_time} minutes\n"
		txt += f"Description: {self.description}\n"
		return txt


