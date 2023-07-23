'''Given an array and contains alphabets. print the count of the alphabets in alphabetical order in an dictionary format

Input Format
aaaeebbcc

Constraints
none

Output Format
{a:3,b:2,c:2,e:2}   '''

def count_alpha(input_alpha):
    
    input_alpha.sort()
    total_count ='{'
    for i in input_alpha:
        count_alpha = input_alpha.count(i)
        if i in total_count:
            continue
        total_count += i+':'+str(count_alpha)+','
    total_count =    total_count[:len(total_count)-1]
    total_count +='}'
    return total_count
    
alpha_list = list(input())
result = count_alpha(alpha_list)    
print(result)