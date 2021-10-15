"""
Exe11-1
This program repeatedly asks the user to 
enter product names and prices. Store all 
of these in a dictionary whose keys are 
the product names and whose values are the 
prices. When the user is done entering 
products and prices, allow them to repeatedly 
enter a product name and print the corresponding 
price or a message if the product is not in the dictionary.
"""


d = dict()
status=''
while status!='Done':
	key=input('Enter product: ')
	value=eval(input('Enter the price: '))
	d[key]=value
	status=input('Enter Done to complete.')

status=''
while status!='Done':
	product=input('Enter product to crosscheck: ')
	if product in d:
		print(d[product])
	else:
		print('Product not in the list.')
	status=input('Enter Done to stop.')