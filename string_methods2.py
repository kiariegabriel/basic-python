"""
Exe8-2
This program allows the user to enter five numbers
(read as strings). Create a string that consists of
the user’s numbers separated by plus signs. For instance,
if the user enters 2, 5, 11, 33, and 55, then the string 
should be '2+5+11+33+55'.
"""

from string import punctuation
s=input('Enter the numbers:\n')
for c in punctuation:
	s=s.replace(c,'')
l=[]
for i in s:
	l.append(i)
print(l)
n_s='+'.join(l)
print(n_s)