

class Evaluator():
	def __init__(self):
		pass
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		else:
			return sum( len(word) * float(coef) for word, coef in zip(words, coefs))

	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			return -1
		else:
			return sum( len(elems) * float(coefs[y]) for y, elems in enumerate(words))


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))