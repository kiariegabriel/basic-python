"""
Exe7-2
Write a program that generates a list of 20 
random numbers between 1 and 100. (a) Print 
the list. (b) Print the average of the 
elements in the list. (c) Print the largest 
and smallest values in the list. (d) Print 
the second largest and second smallest entries 
in the list (e) Print how many even numbers are 
in the list.
"""

from random import randint
l=list()
for i in range(20):
	l=l+[randint(1,100)]
print('a.) ', l)
print('b.) ',sum(l)/len(l))
print('c.) ','The largest number is: ',max(l), ' and the least number is: ', min(l))
l.sort()
print('d.) ', 'The second largest number is: ',l[-2], 'and the second smallest is: ',l[1])
count=0
for item in l:
	if item%2==0:
		count+=1
print('e.) ',count)