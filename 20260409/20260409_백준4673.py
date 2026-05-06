def summ():


nonself = set()

for N in range(1, 10001):
    temp = sum(map(int, str(N))) + N
    nonself.add(temp)

for j in range(1, 10001):
    if j not in nonself:
        print(j)