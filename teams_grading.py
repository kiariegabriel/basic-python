"""
Exe11-6
This program ask the user to enter game 
scores in a format like team1 score1 - 
team2 score2. Store this information in a 
dictionary where the keys are the team names 
and the values are lists of the form [wins, losses].
"""

d=dict()
score=100
for i in range(5):
	l=list()
	team=input('Enter team: ')
	l.append(eval(input('Enter score: ')))
	l.append(score-l[0])
	d[team]=l
print(d)