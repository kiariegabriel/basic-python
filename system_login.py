"""
Exe11-4
This program uses a dictionary that contains
user names and passwords. The program should
ask the user to enter their username and password.
If the username is not in the dictionary, the program
should indicate that the person is not a valid user of
the system. If the username is in the dictionary, but
the user does not enter the right password, the program
should say that the password is invalid. If the password
is correct, then the program should tell the user that they
are now logged in to the system.
"""


passw={'Gabe':'123456789','Gabriel':'987654321'}
user=input('Enter username')
if user in passw:
	password=input('Enter password:  ')
	if password==passw[user]:
		print('You\'re logged in.')
	else:
		print('Invalid password.')
else:
	print('Not a valid user.')