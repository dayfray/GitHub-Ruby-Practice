# Author: Day Fray
# stuffguy@stuff.com


# this small program will ask you your name, and then it will print it back to you, saying hello
# once you complete the function for asking your name

def what_name(name):

	if len(name) > 0:
		return name


	else:
		name = "world"
		return name

	print "Hello " + name + "!"

print "Hello " + what_name(raw_input("Hello, and what is your name? "))
