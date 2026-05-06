N = []

for i in range(9):
    N.append(int(input()))

k = max(N)
print(k)
print(N.index(k)+1)