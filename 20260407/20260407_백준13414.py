import sys
input = sys.stdin.readline

N, L = map(int, input().split())
List = {}

for _ in range(L):
    id = input().strip()
    
    if id in List:
        del List[id]
    List[id] = 0

List = list(List.keys())

for i in List[:N]:
    print(i)