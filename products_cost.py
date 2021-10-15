"""
Exe11-1b
This program repeatedly asks the user to enter
product names and prices. Store all of these in
a dictionary whose keys are the product names and 
whose values are the prices. When the user is done 
entering products and prices, allow them to repeatedly 
enter a product name and print the corresponding price 
or a message if the product is not in the dictionary. 
It then allows the user to enter a dollar amount and 
print out all the products whose price is less than that amount.
"""


status = ''
d={}
while status!='done':
	product=input('Enter product name: ')
	d[product]=eval(input('Enter price of the product: '))
	status=input('Enter Done to close ')
print(d)
for i in range(2):
	product=input('Enter the product: ')
	if product in d:
		print(d[product])
	else:
		print('Not in the list.')
dollar=eval(input('Enter the money: '))
l=[x[0] for x in d.items() if x[1]<=dollar ]
print(l)