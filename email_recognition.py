"""
Exe6-8
Student email addresses end with @student.college.edu, 
while professor email addresses end with @prof.college.edu. 
This program first asks the user how many email addresses 
they will be entering, and then has the user enter those 
addresses. After all the email addresses are entered, the 
program should print out a message indicating either that 
all the addresses are student addresses or that there were 
some professor addresses entered.
"""

count1=0
count2=0
num=eval(input('Enter the number of emails: '))
for i in range(num):
	email=input('Enter an email: \n')
	if email[-16:-12]=='prof':
		count1=1
	elif email[-16:-12]=='dent':
		count2=1
if count1==1 and count2==1:
	print('There\'re professors and students emails')
elif count1==1 and count2==0:
	print('Only professors emails')
elif count1==0 and count2==1:
	print('Only students email')