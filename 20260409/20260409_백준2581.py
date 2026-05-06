def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

M = int(input())
N = int(input())
N_list = []

for j in range(M, N+1):
    if prime(j):
        N_list.append(j)

if(len(N_list) == 0):
    print(-1)
else:
    print(sum(N_list))
    print(min(N_list))