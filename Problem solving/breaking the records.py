def breakingRecords(scores):
    h_score = l_score = scores[0]
    h_count = l_count = 0
    
    for score in scores:
        if score > h_score:
            h_score = score
            h_count +=1
        if score < l_score:
            l_score = score
            l_count += 1
    print(h_count, l_count)

    
n = int(input())
scores = list(map(int, input().split()))
breakingRecords(scores)