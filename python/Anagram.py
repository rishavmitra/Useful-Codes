/*Check if two strings are anagram*/

from collections import defaultdict

str1 = input()
str1 =''.join(e for e in str1 if e.isalnum())
str1=str1.lower()

str2 = input()
str2 = ''.join(e for e in str2 if e.isalnum())
str2 = str2.lower()

Dict1 = defaultdict(int)
Dict2 = defaultdict(int)

for i in range(len(str1)):
  Dict1[str1[i]] += 1

for j in range(len(str2)):
  Dict2[str2[j]] += 1

if(dict(Dict1)==dict(Dict2)):
  print('Yes')
else:
  print('No')


