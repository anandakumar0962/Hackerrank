def all_socks_in_pairs(socks):
    count_dict = {}
    
    for sock in socks:
        if sock in count_dict:
            count_dict[sock] += 1
        else:
            count_dict[sock] = 1
    
    for count in count_dict.values():
        if count % 2 != 0:
            return "false"
    
    return "true"


socks_input = input()
result = all_socks_in_pairs(socks_input)
print(result) 
