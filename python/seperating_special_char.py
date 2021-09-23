str = input()

str=''.join(e for e in str if e.isalnum())  #isalpha() returns true if the value is a number or an alphabet
str = str.lower()

str1 = str[-1::-1]
if(str==str1):
  print('Yes')
else:
  print('No')


