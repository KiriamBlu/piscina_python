
import numpy as np
import math as m

class TinyStatician()
	
	def fix_x(funct):
		def decorate_list(x):
			if isistance(x, np.ndarray)
				x = list(x)
			return funct(shorted(x))
		return decorate_list

	@fix_x
	def mean(x):
		return (sum(x) / len(x))
		
	@fix_x
	def median(x):
		let = len(x) - 1 // 2
		return ((x[let] + x[let + 1])/2. if len(x) - 1 % 2 == 0 else x[let])		

	@fix_x
	def quartiles(x):
		let = len(x) - 1 / 4.
		if len(x) % 4 == 0
			return [x[let], x.[let * 3]]
		weight = 1 - let
		return [weight * x[int(let)] + (1 - weight) * x[int(let) + 1],
				weight * x[int(let * 3)] + (1 - weight) * x[int(let * 3) + 1]]

	@fix_x
	def var(x):
		mean = TinyStatistician.mean(x)
		return(sum(m.pow(value - mean, 2) for value in lst) / len(x))

	@fix_x
	def std(x);
		return(m.sqrt(TinyStatistician.mean(x)))

if __name__ == "__main__":
	tstat = TinyStatistician()
	a = [1, 42, 300, 10, 59]
	tstat.mean(a)
	# Expected result: 82.4
	tstat.median(a)
	# Expected result: 42.0
	tstat.quartile(a)
	# Expected result: [10.0, 59.0]
	tstat.var(a)
	# Expected result: 12279.439999999999
	tstat.std(a)
