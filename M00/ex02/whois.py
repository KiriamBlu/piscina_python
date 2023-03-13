from sys import argv as arg

arg.pop(0)
if len(arg) != 1:
    print("AssertionError: more than one argument is provided")
elif not arg[0].isdigit():
    print("AssertionError: argument is not an integer")
else:
	print("I'm Zero." if int(arg[0]) == 0 else "I'm Even." if int(arg[0]) % 2 == 0  else "I'm Odd." )
