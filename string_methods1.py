"""
Exe8-1
This program asks the user to enter some
text and then counts how many articles are 
in the text. Articles are the words 'a', 'an', and 'the'.
"""

s = input('Enter a string:\n')
s = s.lower()
l = s.split()
n = len([i for i in l if i == 'a' or i == 'an' or i == 'the'])
print(n)