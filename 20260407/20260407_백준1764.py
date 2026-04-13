N, M = map(int, input().split())
hear = set()
see = set()

for _ in range(N):
    hear.add(input())
for _ in range(M):
    see.add(input())

unknown = list(hear&see)
unknown.sort()

print(len(unknown))
for i in unknown:
    print(i)