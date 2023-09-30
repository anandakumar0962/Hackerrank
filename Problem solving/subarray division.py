def separate_choco(s, d, m):
    output = 0
    if len(s) == 1:
        return 1
    else:
        for i in range(len(s)):
            subset = s[i:m+i]
            if sum(subset) == d and len(subset) == m:
                output += 1
            if m+i == len(s):
                break
        return output

n = int(input())
s = list(map(int, input().split()))
d, m = map(int,input().split())
print(separate_choco(s, d, m))
