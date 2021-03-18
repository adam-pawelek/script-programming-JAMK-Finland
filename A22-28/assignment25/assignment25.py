def calculator(action,number1, number2):
	if action == "add":
		outcome = number1 + number2
	elif action == "sub":
		outcome = number1 - number2
	elif action == 'multiply':
		outcome = number1 * number2
	elif action == "divide":
		try:
			outcome = number1 / number2
		except ZeroDivisionError:
			outcome = None
		except TypeError:
			outcome = 'TypeError You are trying to divide with no-number'

	return outcome


print(calculator("add", 1, 2)) #should print 3
print(calculator("sub", 1, 2)) #should print -1
print(calculator("multiply", 1, 2)) #should print 2
print(calculator("divide", 4, 2)) #should print 2
print(calculator("divide", 4, 0)) #should print None
print(calculator("divide",4,'a'))
print(calculator("divide",'a',3))

'''
Sample tests works fine
'''


