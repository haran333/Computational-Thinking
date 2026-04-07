N = int(input())
num = []

for i in range(N):
    num.append(int(input()))
num = list(set(num))
num.sort()

for j in range(len(num)):
    print(num[j])