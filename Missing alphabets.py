'''The program must accept a string S containing only lower case alphabets as the input. The program must print the missing lower case alphabets in string S in alphabetical order as the output. Note: At least one lower case is always missing in the string S.

Input Format

The input must be in string which can include alphanumeric, number etc.

Constraints

None

Output Format

The output must be in string'''

import string
inp= input()
numbers = [int(m) for m in inp if m.isdigit()]
a = [x for x in inp]
b = [i for i in string.ascii_lowercase]
for y in range(len(a)):
    if a[y] in b:
        b.remove(a[y])
output = ''.join(map(str, b))
print(output)
    
    