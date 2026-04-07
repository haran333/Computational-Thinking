N = int(input())
List1 = list(map(int, input().split()))
M = int(input())
List2 = list(map(int, input().split()))

upper = 0
downer = M-1

for i in range(M):
    while(List1[upper] != List2[i]):
        upper += 1
        if (upper == N):
            upper = 0
            break
    while(List1[downer] != List2[i]):
        downer -= 1
        if (downer == -1):
            break
    print(downer - upper + 1, end= ' ')