from sys import argv as arg

arg.pop(0)
strs = [ar[::-1] for ar in arg[::-1]]
result = "".join([var.swapcase() for args in strs for var in args])
print(result)
