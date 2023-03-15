

class GotCharacter():
	def __init__(self, name, is_alive=True):
		if isinstance(name, str):
			self.name = name
			self.is_alive = is_alive
		else:
			raise TypeError("Got characer only can be instanciated by name")

class Stark(GotCharacter):
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name, is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"
		#{"first_name": "Arya", "is_alive": True, "family_name": "Stark", "house_words": "Winter is Coming"}

	def print_house_words(self):
		print(self.house_words)

	def die(self):
		self.is_alive = False


arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)


