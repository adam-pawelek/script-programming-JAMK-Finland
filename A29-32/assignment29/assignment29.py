
try:
	file = open("animals.txt",'r')
	myList = file.readlines()
finally:
	file.close()

myList.sort()

for i in myList:
	print(i.strip())