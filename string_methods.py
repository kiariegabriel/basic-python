"""
Exe7-5
Ask the user to enter a list of strings. 
Create a new list that consists of those 
strings with their first characters removed.
"""


s=input('Enter a string: ')
l=list(s)
l_n=list()
for i in range(len(l)):
	n=l[i].replace(l[i][0],'')
	l_n.append(n)
print(l_n)
