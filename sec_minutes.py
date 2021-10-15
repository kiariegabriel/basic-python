"""
Exe3-8
This program asks the user for a number of seconds 
and prints out how many minutes and seconds that is.
"""


sec=eval(input('Enter the number of seconds: '))
min=sec//60
sec=sec%60
print(min,'minutes',sec,'seconds',sep=' ')