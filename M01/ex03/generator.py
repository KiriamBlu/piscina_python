import random

def generator(text, sep=" ", option=None):
	'''	
	Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
	option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
	'''
	if not all(chars.isprintable() for chars in text):
		raise TypeError("")
	dicty = text.split(sep)
	while len(dicty) > 0:
		var = range(len(dicty))
		helper = get_word(var, dicty, option)
		dicty.pop(int(helper["index"]))
		yield helper["name"]

def get_word(var, listy, option):
	name = None
	index = 0
	if option == None:
		name = listy[0]
		index = 0
	elif option == "shuffle":
		#Elige una palabra aleatoria
		name = random.choice(listy)
		index = listy.index(name)
	elif option == "ordered":
		#Elige la primera palabra en orden alfabético
		name = min(listy)
		index = listy.index(name)
	elif option == "unique":
		#Elige la primera palabra que no ha sido seleccionada antes
		name = list(set(listy))[0]
		index = listy.index(name)
	else:
		raise TypeError("No valid option")
	return {"name" : f"{name}", "index" : f"{index}"}

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
	print(word)