N = int(input())
sosu = [2]

for i in range(3, N+1, 2):
    prime = True
    for j in sosu:
        if (i > j and i % j == 0):
            prime = False
            break
    if prime:
        sosu.append(i)
print(sosu)