"""
Exe7-7
This program takes any two lists L and M of the 
same size and adds their elements together to form 
a new list N whose elements are sums of the corresponding 
elements in L and M. For instance, if L=[3,1,4] and M=[1,5,9], 
then N should equal [4,6,13].
"""


l = eval(input('Enter a list\n'))
m = eval(input('Enter a list\n'))
n = []
for i in range(len(l)):
	n.append(l[i] + m[i])
print(n)