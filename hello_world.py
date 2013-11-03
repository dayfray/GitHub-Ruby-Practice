

def what_name(name):

	if len(name) > 0:
		return name

	else:
		name = "world"
		return name

	print "Hello " + name + "!"

print "Hello " + what_name(raw_input("Hello, and what is your name? "))
