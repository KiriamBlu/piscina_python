

class vector():
	def __init__(self, vector):
		if isinstance(vector, list):
			if len(vector) == 1:
				if not all(isinstance(element, (float)) for element in vector[0]) and len(vector[0]) != 1:
					raise self.notValidInput("Not valid vector input")
				self.shape = tupla(1, len(vector))
				self.values = self.build_vec([vector[0]])
			elif len(vector) > 1:
				if not all(isinstance(element, list) and len(element) == 1 for element in vector):
					raise self.notValidInput("Not valid vector input")
				self.shape = tupla(len(vector[0]), 1)
				self.values = self.build_vec(vector)
			else:
				raise self.notValidInput("Not valid vector input")    
		elif isinstance(vector, tuple):
			if len(vector == 2):
				self.shape[0], self.shape[1]  = vector
				self.values = self.build_empty_vector(self.shape[0], self.shape[1])
		else:
			raise self.notValidInput("Not valid vector input")

	###############################################################################################

	def build_vec(self, listi):
		return [list(val for val in row) for row in listi]

	def build_empty_vector(self, n_row, n_col):
		return [[0] * n_row for nothing in range(n_col)]

	def addVec(self, other)
		result = vector(other.values)
		for y in range(other.shape[0]):
			for x in range(other.shape[1]):
				result.values[y][x] += other[y][x]
		return result

	def subVec(self, other)
		result = vector(other.values)
		for y in range(other.shape[0]):
			for x in range(other.shape[1]):
				result.values[y][x] -= other[y][x]
		return result

	def mulVec(self, other):
		e_vec = vector((self.shape[0], self.shape[1]))
		if isinstance(other, vector) and self.shape == other.shape:
			print((self.shape[0], other.shape[1]))
			for y in range(other.shape[1]):
				for x in range(self.shape[0]):
					e_vec.values[y][x] = sum([self.values[x][k] * other.values[k][y] for k in range(self.shape[0])])
		elif isinstance(other, int)
			for y in range(self.shape[1]):
				e_vec.values[y] = [self.values[y][x] * other for x in range(self.shape[0])]
		else
			raise TypeError("Error not valid multiplication")
		return e_vec

	def dot(self, other):
		multiplayed = self.mulVec(other)
		return sum(elem for elem in multiplayed.values)


	def divVec(self, scalar):
		values = [[val / scalar for val in row] for row in self.values]
		return vector(values)

	def T(self):
		t_vec = [[ self.values[x][y]for x in range(self.shape[1])] for y in range(self.shape[0])]
		return vector(t_vec)


	###############################################################################################

	def __add__(self, other):
		if self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
			raise self.notValidInput("vector not equal shape, sum not valid")
		var = self.addVec(other.values)
		return var

	def __radd__(self, other):
		if self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
			raise self.notValidInput("vector not equal shape, sum not valid")
		var = self.addvec(other.data)
		return var

	def __sub__(self, other):
		if self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
			raise self.notValidInput("vector not equal shape, sub not valid")
		var = self.subvec(other.data)
		return var

	def __rsub__(self, other):
		if self.shape[0] != other.shape[0] or self.shape[1] != other.shape[1]:
			raise self.notValidInput("vector not equal shape, sub not valid")
		var = self.subvec(other.data)
		return var

	def __truediv__(self, scalar):
		if isinstance(scalar, vector):
			if scalar.shape == (1, 1) and scalar.data[0][0] != 0:
				var = self.divVec(scalar.data[0][0])
			else:
				raise self.notValidInput("Illegal div by 0 or not scalar 'vector'")
		elif isinstance(scalar, (int, float)) and scalar == 0:
			raise self.notValidInput("Illegal div by 0")
		elif isinstance(scalar, (int, float)):
				var = self.divVec(float(scalar))
		else:
			raise self.notValidInput("Not valid input for div")
		return var

	def __mul__(self, other):
		if isinstance(other, vector):
			if self.shape[0] != other.shape[1]:
				raise ValueError(f"Invalid vector product: cannot multiply a {self.shape[0]}x{self.shape[1]} vector with a {other.shape[0]}x{other.shape[1]} vector")
			result = self.multvec(other)
		elif isinstance(other, (float, int)):
			result = self.multvec(float(other))
		return result

	def __rmul__(self, other):
		if isinstance(other, vector):
			if other.shape[1] != self.shape[0]:
				raise ValueError(f"Invalid vector product: cannot multiply a {other.n.shape[0]}x{other.shape[1]} vector with a {self.n_cols}x{self.shape[1]} vector")
			result = other.multvec(self)
		elif isinstance(other, (float, int)):
			result = self.multvec(float(other))
		return result



