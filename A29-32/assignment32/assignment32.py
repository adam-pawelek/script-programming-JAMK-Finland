import sys


if len(sys.argv) < 2:
	print("not enough arguments")
	quit()


try:
	file = open(sys.argv[1],'r')
except IOError:
	print ("That file does not exist try again")
	quit()
print(file.read())
file.close()