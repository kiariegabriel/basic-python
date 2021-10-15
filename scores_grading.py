"""
Exe9-5
This program allows the user to enter any number of test scores. 
The user indicates they are done by entering in a negative number. 
Print how many of the scores are A’s (90 or above). Also print out
the average.
"""

sum = 0
score = 0
i = 0
count = 0
while score >= 0:
	score = eval(input('Enter the test score: '))
	if score<0:
		break
	i+=1
	if score >= 90:
		count += 1
	sum += score
print(count, 'scores are A\'s')
print('The average is', sum/i)