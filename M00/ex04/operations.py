from sys import argv as arg
import re


def format_float(num):
	if isinstance(num, (float, int)):
		if re.match(r'^\d+\.\d+$', str(num)):
			return "{:.2f}".format(float(num))
		else:
			return str(num)
	else:
		return "ERROR"


arg.pop(0)

if len(arg) == 2 and arg[0].isdigit() and arg[1].isdigit():
	info = {"Sum": float(arg[0]) + float(arg[1]),
			"Difference": float(arg[0]) - float(arg[1]),
			"Product": float(arg[0]) * float(arg[1]),
			"Quotient": ("ERROR" if float(arg[1])==0 else float(arg[0]) / float(arg[1])),
			"Remainder": ("ERROR" if float(arg[1])==0 else float(arg[0]) % float(arg[1]))}
	for key, value in info.items():
		print(key + ": " + format_float(value))
else:
	print("Usage: python operations.py <number1> <number2>")
