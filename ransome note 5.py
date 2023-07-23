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

false
Explanation 0

Input: ransomNote = "a", magazine = "b" Output: false

Sample Input 1

aa
ab
Sample Output 1

false
Explanation 1

Input: ransomNote = "aa", magazine = "ab" Output: false

Sample Input 2

aa
aab
Sample Output 2

true '''


ransome_note = input()
magazine = input()

if ransome_note in magazine:
    print(True)
else:
    print(False)
