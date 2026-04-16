N = int(input())
hansu = 0

if(N<100):
    hansu = N
else:
    hansu = 99
    if(N == 1000):
        N = 999
    for i in range(100, N+1):
        f = str(i)
        if(int(f[0]) + int(f[2]) == 2*int(f[1])):
            hansu += 1
print(hansu)