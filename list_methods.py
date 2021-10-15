"""
Exe6-1
This program asks the user to enter a string. The program should then print the following:
  (a) The total number of characters in the string
  (b) The string repeated 10 times
  (c) The first character of the string (remember that string indices start at 0)
  (d) The first three characters of the string
  (e) The last three characters of the string
  (f) The string backwards
  (g) The seventh character of the string if the string is long enough and a message otherwise
  (h) The string with its first and last characters removed
  (i) The string in all caps
  (j) The string with every a replaced with an e

"""


s=input('Enter a string: ')
s=s.lower()
print('a.) ',len(s))
print('b.) ', s*10, end=' ')
print()
print('c.) ', s[0])
print('d.) ', s[:3])
print('e.) ', s[-3:])
print('f.) ', s[-1::-1])
if len(s)>=10:
	print(s[9])
else:
	print('The string is short!!')
s_n=s.replace(s[0],'')
s_n=s.replace(s[-1],'')
print(s_n)
s_c=s.upper()
print(s.upper())
for c in s:
	if c=='a':
		s_r=s.replace(c,'e')
print(s_r)
for c in range(len(s)):
	s_s=s.replace(s[c],'_')
print(s_s)