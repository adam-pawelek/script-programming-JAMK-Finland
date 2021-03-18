#Here’s the example list (can be copied to a Python file):  
persons = ["alice", "bob", "craig", "dave", "elisabeth", "frank", "george"]  
#Hint: use the modulus operator(%)!

for i in range (len(persons)):
	if i % 2 == 1:
		print(str(i) + " : " + persons[i])
	
