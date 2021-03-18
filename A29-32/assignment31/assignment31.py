

#Add user a possibility to add new items to a file.

print ("Now you could add animals names to the file animals.txt")

file = open("animals.txt",'a')

choice = 0

while True:
	print("To add animal name to file write 1 to exit write 0")	
	try:
		choice = int(input())
	except:
		print("You shoudl write 0 or 1 try again")
	if choice != 0 and choice !=1:
		print("You shoudl write 0 or 1 try again")

	if choice == 0:
		break
	if choice == 1:
		print("Enetr name of animal that you want to add to the file")
		try:
			name = input()
			file.write(name + "\n")
		except:
			print ('This is not a string')



file.close()


file = open("animals.txt",'r')




#Exercise 29
try:
	file = open("animals.txt",'r')
	myList = file.readlines()
finally:
	file.close()

myList.sort()

for i in myList:
	print(i.strip())
