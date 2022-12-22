'''You are given an array of integers. The special property of the array is that exactly two different elements occur once while other elements occur twice.

You are required to determine those two elements.

Input Format

First line: Integer denoting the number of elements in the array Second line: space-separated integers denoting the values in the array

Constraints

None

Output Format

Print two space-separated integers that occur once in the array in ascending order.

Sample Input 0

8
1 2 3 4 5 5 3 4
Sample Output 0

1 2'''

no_of_intergers = int(input())
integers = input()
list_of_integers = integers.split(' ')
unique = []
if len(list_of_integers) == no_of_intergers:
    for i in range(len(list_of_integers)):
        count = list_of_integers.count(list_of_integers[i])
        if count == 1:
            unique.append(int(list_of_integers[i]))

unique.sort()
output = ' '.join([str(a) for a in unique])
print(output)

