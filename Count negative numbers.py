'''Given a string which is sorted in non-increasing order return the number of negative numbers.

Input Format

The input format is string separated with special character '#' and spaces

Constraints

none

Output Format

The output format is number

Sample Input 0

4 3 2 -1#3 2 1 -1#1 1 -1 -2#-1 -1 -2 -3
Sample Output 0

8'''

input_string = input()
a = input_string.replace('#', ' ')
b = a.split(' ')
output = 0
for i in b:
    if int(i) < 0:
        output += 1
print(output)
