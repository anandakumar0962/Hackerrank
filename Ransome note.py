'''Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Input Format

The input format is string The first line input is ransomeNote The second line input is magazine

Constraints

1 <= ransomNote.length, magazine.length <= 105 ransomNote and magazine consist of lowercase English letters.

Output Format

The output is boolean

Sample Input 0

a
b
Sample Output 0

false'''

ransomeNote = input()
magazine = input()
output = ''
for i in magazine:
    if i in ransomeNote:
        output += i
if ransomeNote == output:
    print("true")
else:
    print("false")
