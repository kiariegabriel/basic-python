"""
Exe9-4
This program asks the user to enter a password.
If the user enters the right password, the program 
should tell them they are logged in to the system. 
Otherwise, the program should ask them to reenter 
the password. The user should only get five tries to 
enter the password, after which point the program should 
tell them that they are kicked off of the system.
"""

password = 'Rango'
i = 0
entry = input('Enter password: ')
if entry == password:
	print('You are logged into the system.')
while entry != password and i < 4:
	entry = input('Invalid password Enter the password: ')
	i += 1
	if entry == password:
		print('You are logged into the system')
		break
	elif i == 4 and entry != password:
		print('You are kicked out of the system')
