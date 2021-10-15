"""
Exe11-2
this program uses a dictionary whose keys 
are month names and whose values are the 
number of days in the corresponding months. 
It does the following
      (a) Ask the user to enter a month name and use the dictionary to tell them how many daysare in the month.
      (b)Print out all of the keys in alphabetical order.
      (c) Print out all of the months with 31 days.
      (d) Print out the (key-value) pairs sorted by the number of days in each month
"""


days={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
month=input('Enter a month: ')
print(month,'has',days[month],'days')
l=list(days)
l.sort()
print(l)
print([x[0] for x in days.items() if x[1]==31])
print([c for c in days if days[c]==31])
l=list(days.items())
l=[(i[1],i[0])for i in l]
l.sort()
print(l)
s=input('Enter month: ')
for c in days:
	if c[0:2]==s:
		print(days[c])
for c in days:
	print(c[1:2])