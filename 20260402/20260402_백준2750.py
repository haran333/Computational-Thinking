N = int(input())
N = []

for i in range(N):
    N.append(int(input()))
N = list(set(N))
N.sort()

for j in range(len(N)):
    print(N[j])