



choice = 0
number1  = 0
number2  = 0
while True:
	print('0) add')
	print('1) sub')
	print('2) multiply')
	print('3) divide')
	print('-1) quit')


	#choice
	try:
		print('choice: ', end =  ' ')
		choice = int(input())
	except:
		print('This is not a number try again!!!!')
		continue

	if choice < -1 or choice > 3:
		print('Invalid choice try again')

	if choice == -1:
		break
	#nuber1
	try:
		print('number1: ', end =  ' ')
		number1 = float(input())
	except:
		print('This is not a number try again!!!!')
		continue

	#nuber2
	try:
		print('number2: ', end =  ' ')
		number2 = float(input())
	except:
		print('This is not a number try again!!!!')
		continue

	if choice == 0:
		print( number1 + number2)

	if choice == 1:
		print(number1 - number2)

	if choice == 2:
		print(number1 * number2)

	if choice == 3:
		try:
			print(number1 / number2)
		except ZeroDivisionError:
			print("You tried divide by 0!!!!!!!")



