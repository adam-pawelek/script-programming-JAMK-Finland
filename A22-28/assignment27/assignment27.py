import random 

number =  random.randint(0, 20)




print ("++ Guessing Game ++")
print("Guess a number between 0 and 20 !")



guess = 1

while guess < 6:
	print(f"Guess {guess}/5:", end =  ' ')
	try:
		loaded = int(input())
	except:
		print("Not a number, try again")
		continue
	if loaded < 0 or loaded > 20:
		print("The guess should be between 0 and 20, try again")
		continue
	if number != loaded:
		print("sorry, try again!")
	else:
		print ('correct!')
		quit()
	guess+=1

print(f'game over, you lost! the correct number was {number}')


	