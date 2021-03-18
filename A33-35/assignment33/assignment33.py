class Dog:
	def __init__(self, name,sound, walking_speed, running_speed):
		self.name = name
		self.sound = sound
		self.walking_speed = walking_speed
		self.running_speed = running_speed

	def walk(self):
		print(self.walking_speed)
	def run(self):
		print(self.running_speed)
	def bark(self):
		print(self.sound)
	def print_name(self):
		print(self.name)
		

# Test 
#Printing values

print('Created object \n')

animal = Dog('Burek','Hau Hau',10,20)

animal.walk()
animal.run()
animal.bark()
animal.print_name()

#Changes in object

animal.name = 'Zeus'
animal.sound = 'Wouf Wouf'
animal.walking_speed = 20
animal.running_speed = 40


print("\nChanged object \n")


#Printing values

animal.walk()
animal.run()
animal.bark()
animal.print_name()


