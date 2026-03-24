H, M = map(int,input().split())
plus = int(input())

if(M + plus > 59):
    H += (M + plus)//60
    M = (M+ plus)%60
    if(H>23):
        H-=24
else:
    M += plus
print(H, M)