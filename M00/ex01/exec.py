from sys import argv as arg

arg.pop(0)
result = "".join([var.swapcase() for args in [ar[::-1] for ar in arg[::-1]] for var in args])
print(result)
