C = int(input())
average = 0
count = 0

for i in range(C):
    score = list(map(int, input().split()))
    for j in range(1, score[0]+1):
        average += score[j]
    average = average / score[0]
    for k in range(1, score[0]+1):
        if (average < score[k]):
            count += 1
    print(f"{(count/score[0])*100:.3f}%")
    average = 0
    count = 0
    score = []