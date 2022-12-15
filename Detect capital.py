'''We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA". All letters in this word are not capitals, like "leetcode". Only the first letter in this word is capital, like "Google", Given a string word, return true if the usage of capitals in it is right.'''


input = input()

if input.isupper():
  print('true')
elif input[0].isupper() and input[1:].islower():
  print('true')
elif input.islower():
  print('true')
else:
  print('false')