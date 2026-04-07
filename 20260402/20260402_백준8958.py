N = int(input())

for i in range(N):
    score = 0
    count = 0
    testcase = input()
    for j in range(len(testcase)):
        if(testcase[j] == 'O'):
            count += 1
            score += count
        else:
            count = 0
    print(score)