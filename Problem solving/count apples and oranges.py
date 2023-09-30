#solution 1
def count_fruits(s, t, tree_point, fruits):
    count = 0
    for fruit in fruits:
        distance = tree_point + fruit
        if distance >= s and distance <= t:
            count += 1
    return count

s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))
print(count_fruits(s, t, a, apples))
print(count_fruits(s, t, b, oranges))


#solution 2
def countApplesAndOranges(s, t, a, b, apples, oranges):
    sum_Apple = 0
    sum_Orange = 0
    for i in range(len(apples)+len(oranges)):
        if i < len(apples):
            if a + apples[i] in range(s,t+1) :
                sum_Apple += 1
        else:
            if b + oranges[i-len(apples)] in range(s,t+1) :
                sum_Orange += 1
                
    print(sum_Apple,sum_Orange,sep="\n")
    
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)