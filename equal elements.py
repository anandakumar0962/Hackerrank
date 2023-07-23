'''You are given an integer array A consisting of N elements. You can perform the following operations on array A: • Choose any element and increase or decrease it by 3 for 1 coin. • Choose any element and increase or decrease it by 2 for free. You are required to spend the minimum number of coins in order to make all the elements in array A equal.

Input Format

• The first line contains an integer T denoting the number of test cases. • The first line of each test case contains an integer N denoting the number of elements in array A. • The second line of each test case contains N space-separated integers of array A.

Constraints

1≤T≤20000 1≤N≤100000 1≤Ai≤109∀i∈[1,N] Sum of N over all test cases does not exceed 500000

Output Format

Print T lines. For each test case, print a single line denoting the minimum number of coins to make all elements equal.

Sample Input 0

1
4
3 5 2 3
Sample Output 0

1
Explanation 0

We can make all elements equal to 3 in 1 coin which is optimal.

Increase 2 to 5 for 1 coin. Decrease both 5 to 3 for free

Sample Input 1

1
10
6 9 1 14 16 2 14 7 20 20
Sample Output 1

3
Sample Input 2

1
10
2 6 10 17 14 2 17 12 12 15
Sample Output 2

3
Sample Input 3

1
10
14 19 9 17 18 2 16 14 16 7
Sample Output 3

4
Sample Input 4

1
10
12 1 17 20 14 19 14 17 8 1
Sample Output 4

5 '''

i = int(input())
N = int(input())
a = list(map(int, input().split(" ")))
result = 0
a.sort()
centre  = N//2
for i in a:
    if i%2 != 0:
        i+=3
        result +=1
    while i < a[centre]:
        i+=2
if (N-result) < result:
    print(N-result)
else:
    print(result)
