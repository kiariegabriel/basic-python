# A program to play a simple quiz game.

count = 0
print('What is the capital city of Kenya? ',end='')
ans=input()
if ans.lower() == 'nairobi':
	count += 1
	print('Correct! You got question 1 of 2 correct')
else:
	print('Wrong! The answer is Nairobi. You got 1 of 2 wrong')
print('What county is the largest in Kenya? ',end='')
ans=input()
if ans.lower() == 'turkana':
	count += 1
	print('Correct! You got question 2 of 2 right')
else:
	print('Wrong. The correct answer is Turkana. You got question 2 of 2 wrong')
print('You got ', count,' out of 2 question(s) right!')
