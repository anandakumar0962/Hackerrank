'''To make a full url from a given string

Input Format

The input will be as a string.

Constraints

none

Output Format

The output will be as a url format.'''

input_string= input()
b = input_string.replace("#", ".", 2)
c = b.replace("#", "/")
url_format = "https://" + c + "/"
print(url_format)