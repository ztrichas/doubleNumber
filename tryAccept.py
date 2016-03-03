

number = input("What number should I double? ")

#Tells whether number was successfully converted
Converted = False

while not converted:

	try:
		number = float(number)
		
	except ValueError: 
		number = input("Sorry that's not a number. Try again.")
		
		
#Finally, print result
print("Double that is {}.".format(number * 2))