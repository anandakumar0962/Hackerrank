def kangaroo(x1, v1, x2, v2):
    x = x2 - x1
    v = v1 - v2
    if v == 0:
        return "NO"
    y = x/v
    if y > 0 and y.is_integer():
        return "YES"
    else:
        return "NO"

x1, v1, x2, v2 = map(int, input().split())
print(kangaroo(x1, v1, x2, v2))