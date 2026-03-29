N, X = map(int,input().split())
ListA = []*N
ListA = list(map(int, input().split()))
ListSmall = []

for i in ListA:
    if (i<X):
        print(i, end = ' ')