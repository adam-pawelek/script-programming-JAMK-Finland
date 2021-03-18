def vowels(word):
	allVowels = 'aeiouy'
	sumVowels = 0
	for i in range (len (word)):
		if word[i] in allVowels:
			sumVowels += 1
	return sumVowels


'''
print(vowels("aaa")) # prints: 3
print(vowels("aba")) # prints: 2
print(vowels("bca")) # prints: 1

program returns correct answers to sample tests
'''

