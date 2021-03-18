

#NameError
print ("This is IndexError example \n")
try:
	print("Trying to add +1 to not defined variable")
	x+= 1

except NameError:
	print("Result: NameError: name 'x' is not defined")






#IndexError
print("\nThis is IndexError example \n")

myList = [1,2,3]
try:
	for i in range(4):
		print(myList[i])
except IndexError:
	print("List have 3 elemnts trying to read 4 elemnt")
	print("Result: IndexError list index out of range")




#KeyError

print ("\nThis is KeyError example\n")


responsibilities = {
	'Adam': "Cooking",
	'Pawel': "Washing",
	'Piotr': "Shoping",
}

try:
	print (responsibilities['Zosia'])
except KeyError:
	print ("Trying to get result from the key that is not in the Dictionary")
	print("Result: KeyError: 'Zosia' ")





