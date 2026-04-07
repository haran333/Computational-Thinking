N = int(input())
num = sorted(list(map(int, input().split())))
D = [0]*N
sum = 0

for i in range(1, N):
    D[i] = D[i-1] + (num[i] - num[i-1])*i
    sum += D[i]

print(sum*2)