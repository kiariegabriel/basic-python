"""
Exe11-5
Repeatedly ask the user to enter a team name
and the how many games the team won and how many
they lost. Store this information in a dictionary where
the keys are the team names and the values are lists of 
the form [wins, losses].

  (a) Using the dictionary created above, allow the user to enter a team name and print out the team’s winning percentage.
  (b) Using the dictionary, create a list whose entries are the number of wins of each team.
  (c) Using the dictionary, create a list of all those teams that have winning records.
"""


d=dict()
for i in range(5):
	l=list()
	team=input('Enter team: ')
	l.append(eval(input('Enter winning: ')))
	l.append(eval(input('Enter losses: ')))
	d[team]=l
print(d)t=input(',Enter a team name: ')
x=sum(d[t])
p=(d[t][0])*100/x
print(p,'% winning rate',sep='')
wins=[c[0] for c in d.values()]
print(wins)
w_r=[c[0] for c in d.items() if c[1][0]>=60]
print(w_r)