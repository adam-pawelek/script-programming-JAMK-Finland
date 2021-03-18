def calculator(action,number1, number2):
	if action == "add":
		outcome = number1 + number2
	elif action == "sub":
		outcome = number1 - number2
	elif action == 'multiply':
		outcome = number1 * number2

	return outcome


print(calculator("add", 1, 2)) #should print 3
print(calculator("sub", 1, 2)) #should print -1
print(calculator("multiply", 1, 2)) #should print 2

'''
Sample tests works fine
'''


