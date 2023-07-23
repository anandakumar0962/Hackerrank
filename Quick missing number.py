'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input Format

3 0 1

Constraints

none

Output Format

2

Sample Input 0

0 1
Sample Output 0

2
Sample Input 1

9 6 4 2 3 5 7 0 1
Sample Output 1

8
Sample Input 2

0
Sample Output 2

1
Explanation 2

n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.'''

def check_missing_num(input_nums):
    
    result = []
    digits = [n for n in range(10)]
    for n in digits:
        if n not in input_nums and n < max(input_nums):
            result.append(n)
            
    if result != []:
        print(result[0])
    else:
        print(max(input_nums)+1)
        
            
given_input = input().split(' ')
list_of_nums = [int(n) for n in given_input]
check_missing_num(list_of_nums)