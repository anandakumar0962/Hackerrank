def getTotalX(a, b):
    result = 0
    for i in range(max(a), min(b)+1):
        is_factor = True
        for j in a:
            if i % j != 0:
                is_factor = False
                break
        for j in b:
            if j % i != 0:
                is_factor = False
                break
        if is_factor:
            result += 1
    return result

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(getTotalX(a, b))
