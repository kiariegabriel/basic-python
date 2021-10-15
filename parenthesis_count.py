"""
Exe6-3
People often forget closing parentheses when 
entering formulas. This program asks the user 
to enter a formula and prints out whether the 
formula has the same number of opening and closing 
parentheses.
"""


s=input('Enter a formula:\n')
if s.count('(')==s.count(')'):
	print('Closing and opening parenthesis are equal')
else:
	print('Closing and opening parenthesis aren\'t equal')