def largest(myList):
	if len(myList) == 0:
		return ("You don't have arguments on this list") 
	maxx = myList[0]
	
	for i in range(len(myList)):
		if (myList[i] > maxx):
			maxx = myList[i]
	return maxx
	
		
