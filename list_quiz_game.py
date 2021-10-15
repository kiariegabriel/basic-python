"""Prompts the user with questions. After the test the 
program gives the user the number of question(s) they got right"""

questions = ['What\'s the capital city of Kenya? ',
			'What\'s the largest county in Kenya? ']

answers = ['Nairobi',
			'Turkana']

count = 0
for i in range(len(questions)):
	ans = input(questions[i])
	if ans.lower() == answers[i].lower():
		count += 1
		print('Correct! You got question {} of {} correct 😊'.format(i + 1, len(questions)))  
	else:
		print('Wrong. The answer is {}. You got question {} of {} wrong 😔'.format(answers[i], i + 1, len(questions)))       
print('You got {} out of {} question(s) right!'.format(count, len(questions)))