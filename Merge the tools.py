'''Merge the tools:

Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD'''

#Solution:

def remove_duplicates(sub_string):
    unique_sub_str = ''
    for c in sub_string:
        if c not in unique_sub_str:
            unique_sub_str += c
    return unique_sub_str
def merge_the_tools(string, k):
    # your code goes here
    list_str = []
    for i in range(0,len(string), k):
        list_str.append(string[i:i+k])

    for sub_string in list_str:
        print(remove_duplicates(sub_string))


if _name_ == '_main_':
    string, k = input(), int(input())
    merge_the_tools(string, k)
