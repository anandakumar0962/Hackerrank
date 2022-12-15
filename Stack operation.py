'''Given an string targets separated with hyphen '-' with an integer n separated by '#'. In each iteration, you will read a number from string.

Build the string number values using the following operations:

Push: Read a new element from the beginning of the string number values, and push it in the array. Pop: delete the last element from the string. If the target value in the string is already built, stop reading more elements. Return the operations to build the target array. You are guaranteed that the answer is unique.

Input Format

The input format is string

Constraints

1 <= target.length <= 100 1 <= target[i] <= n 1 <= n <= 100 target is strictly increasing.

Output Format

The output format is array'''


inp = input()
a = inp[:-2]
x = a.split("-")
output = ""
y = []
for i in range(1, int(inp[-1])+1):
    if str(i) in x:
        output += "Push,"
        y.append(i)
    else:
        output += "Push," + "Pop,"
    if len(y) == len(x):
        break
print("[", output[:-1], "]")