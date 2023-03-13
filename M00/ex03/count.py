import string as string
from sys import argv as arg

def text_analyzer(args=None):
	"""
    This function receives a string and analyzes it to count the number of characters, upper and lower case letters,
    punctuation marks and spaces. If no string is provided as argument, the user will be prompted to input a text.

    Args:
        args (str, optional): The string to be analyzed. Defaults to None.

    Returns:
        None
    """
	if not args:
		print("What is the text to analyze?")
		args = input()
	if not isinstance(args, str):
		print("AssertionError: argument is not an string")
	else:
		info = {"TotalChars": len(args),
				"UpperChars": sum(1 for c in args if c.isupper()),
				"LowerCase": sum(1 for c in args if c.islower()),
				"PuncMarcs": sum(1 for c in args if c in string.punctuation),
				"Spaces": sum(1 for c in args if c.isspace())}
		print("The text contains " + str(info["TotalChars"]) + " character(s):")
		print("- " + str(info["UpperChars"]) + " upper letter(s)")
		print("- " + str(info["LowerCase"]) + " lower letter(s)")
		print("- " + str(info["PuncMarcs"]) + " punctuation mark(s)")
		print("- " + str(info["Spaces"]) + " space(s)")


if __name__ == "__main__":
	text_analyzer(arg[0])