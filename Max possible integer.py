'''The program must accept an integer N as the input. The program must print the maximum possible Integer X which is less than N, but the sum of digits in X is greater than the sum of digits in N. If there is no such integer, the program must print the integer N as it is.

Input Format

35

Constraints

none

Output Format

29'''


x = int(input())
str_x= str(x)
y = [int(a) for a in str_x ]
add_1 = sum(y)
a =[]
d =[]
for j in range(1, x):
    a.append(j)
a.sort(reverse = True)
for i in a:
    str_i = str(i)
    z = [int(b) for b in str_i]
    add_2 = sum(z)
    if add_2 > add_1:
        d.append(i)   
    else:
        continue
if d ==[]:
    print(x)    
else:
    print(max(d))
    
        
        

    