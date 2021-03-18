myList = []

print ("Instruction ")
print ( "write + to add something to the list")
print ( "write - to add something to the list")
print ("x to end program") 

exitLoop = 0

while (exitLoop == 0):
	print ("write + , -  or x")
	job = input()
	if job != 'x':
		print ("write values to add/remove")
	
	if job == '+':
		valueList = input()
		myList.append(valueList)
		print ("I added this to the list")
	elif job == '-':
		valueList = input()
		if valueList in myList:
			myList.remove(valueList)
			print ("Now you don't have this in your list")
		else:
			print("This iteam is not in the list!!!!!")
	elif job == 'x':
		exitLoop = 1
	else:
		print("You didn't wrote + , -  or x try again!!!!")
		
print ("This is your list")
print (myList)


print ("Now I will print all iteams in 1 line")

result = ''
for i in range (len(myList)):
	result += str(myList[i])
	result +=  ' '
	
print (result)

		
		
	
