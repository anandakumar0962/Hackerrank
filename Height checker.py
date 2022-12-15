'''A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an string with integer heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Input Format

The input format will be in string

Constraints

1 <= heights.length <= 100 1 <= heights[i] <= 100

Output Format

The output format will be in a integer'''


n = list(input())
a = sorted(n)
x = 0
y = 0
for i in n:
    if i != a[x]:
        y += 1
    x += 1
print(y)