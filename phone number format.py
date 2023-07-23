'''You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.

You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:

2 digits: A single block of length 2. 3 digits: A single block of length 3. 4 digits: Two blocks of length 2 each. The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.

Return the phone number after formatting.

Input Format

1-23-45 6

Constraints

2 <= number.length <= 100 number consists of digits and the characters '-' and ' '. There are at least two digits in number.

Output Format

123-456 '''
 
given_data = input()
num_str = given_data.replace(' ','').replace('-','')
print(num_str)
result =[]
result.append(num_str[:3])
for i in range(3,len(num_str), 3):
    s = num_str[i:]
    print(s)

    if len(s) == 4:
        result.append(s[0]+s[1])
        result.append(s[2]+s[3])
        break
    elif len(s)== 2:
        result.append(s[0]+s[1])
    elif len(s)%3 == 0 or len(s)%3 == 2 or len(s)%3 == 1:
        result.append(s[:3])
        s = s[i:]
print('-'.join(result))