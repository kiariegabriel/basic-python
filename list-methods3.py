"""
Exe7-1
This program asks the user to enter a list of integers. Do the following: 
  (a) Print Yes if the list contains a 5 and No otherwise.
  (b) Remove the first and last items from the list, sort the remaining items, and print the result.
"""


l=[6,12,5,8,12,19,55,7]
if 5 in l:
	print('Yes')
else:
	print('No')
del l[0]
del l[-1]
l.sort()
print(l)