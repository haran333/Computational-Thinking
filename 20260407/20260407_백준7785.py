N = int(input())
name = set()

for i in range(N):
    N1, N2 = input().split()
    if(N2 == "leave"):
        name.discard(N1)
    else:
        name.add(N1)
name = list(name)
name.sort(reverse = True)

for j in name:
    print(j)