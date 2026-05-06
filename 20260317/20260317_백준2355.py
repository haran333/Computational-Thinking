N1, N2 = map(int,input().split())
N1, N2 = min(N1, N2), max(N1, N2)
sum = (N2*(N2+1))//2 - (N1*(N1+1))//2

print(sum+N1)