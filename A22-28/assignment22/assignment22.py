def speeding_ticket (speed , speedLimit):
	if speed - speedLimit > 5 and speed - speedLimit < 20:
		outcome =(100,False)
	elif speed - speedLimit > 20:
		outcome = (500,True)
	else:
		outcome = (0,False)
	return outcome
	


print(speeding_ticket(50, 50)) #No fine. Prints: (0, False)
print(speeding_ticket(60, 50)) #100€ fine, doesn't lose license. Prints: (100, False)
print(speeding_ticket(100, 50)) #500€ fine, loses license. Prints: (500, True)