'''
Given an input string S, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in S will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that S may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Input Format

A single line input string S.

Constraints

1 <= S.length <=10000
S contains English lettes (upper-case and lower-case), digits, and spaces" ".
There is at least one word in s.
Output Format

A single line output string (which is the reverse of the words in given string(S) concatenated by single space in-between each word)

Sample Input 0

the sky is blue 
Sample Output 0

blue is sky the
Explanation 0

All the words in the given string are (the, sky, is, blue) arranged in reverse order and concatenated by a single space.
Sample Input 1

     hello world
Sample Output 1

world hello
Explanation 1

Your reversed string should not contain leading or trailing spaces.

Sample Input 2

a good    example
Sample Output 2

example good a
Explanation 2

You need to reduce multiple spaces between two words to a single space in the reversed string. '''

#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
S = S.strip().rstrip().lstrip()
list = S.split(' ')
result = ''
for i in range(len(list)-1, -1, -1):
    if list[i] == '':
        continue
    result += list[i]
    if i > 0:
        result += ' '
print(result)
