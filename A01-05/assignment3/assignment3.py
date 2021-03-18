def spacess(number, wordd):
	for i in range(number):
		wordd += ' '
	return wordd
		
def addA (number, wordd):
	for i in range(number):
		wordd += 'A'
	return wordd
	


line = 1

for i in range(10):
	wordd = ''
	wordd = spacess(10 - i, wordd)
	wordd = addA((1 + i) * 2,wordd)
	wordd = spacess(10 - i, wordd)
	print(wordd)
	  

