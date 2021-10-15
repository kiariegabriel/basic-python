"""
Exe6-2
 words in a string is to count the number 
 of spaces in the string. This program that 
 asks the user for a string and returns an 
 estimate of how many words are in the string.
 """

s=input('Enter a string:\n')
count=0
for c in s:
	if c==' ':
		count+=1
print(count+1)