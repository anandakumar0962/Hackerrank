'''
You are provided an array "A" of size "N" that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by 10.

Note: View the sample explanation section for more clarification.

Input Format

First line: A single integer "N" denoting the size of array "A" Second line: "N" space-separated integers.

Constraints

1<=N<=100000 0<=A[i]<=100000

Output Format

If the number is divisible by 10, then print "Yes". otherwise, print "No".

Sample Input 0

5
85 25 65 21 84
Sample Output 0

No
Explanation 0

Last digit of 85 is 5.
Last digit of 25 is 5.
Last digit of 65 is 5.
Last digit of 21 is 1.
Last digit of 84 is 4.
Therefore the number formed is 55514 which is not divisible by 10.
So the output is "No".
Sample Input 1

7
1 90 78 45 789 345 80
Sample Output 1

Yes
Explanation 1

Last digit of 1 is 1.
Last digit of 90 is 0.
Last digit of 78 is 8.
Last digit of 45 is 5.
Last digit of 789 is 9.
Last digit of 345 is 5.
Last digit of 80 is 0.
Therefore the number found is 1085950 which is divisible by 10.
So the output is "Yes". '''

#Solution

N = int(input())
A = input()
list = list(map(int, A.split()))
result_num = 0
for i in range(N):
    result_num += list[i]%10
    if i < (N-1):
        result_num *= 10
if result_num % 10 == 0:
    print("Yes")
else:
    print("No")
