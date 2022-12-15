'''Obtain the domain name from the url

Input Format

The input will be a string. For Eg: 'https://www.youtube.com'

Constraints
none

Output Format

The Output format should be in string. For Eg: youtube.com'''



x = input()
a = x.split('.')
str = ""
del a[0] 
del a[-1]
for i in a:
    str +=i
    
    output = str + ".com"
    
    print(output)