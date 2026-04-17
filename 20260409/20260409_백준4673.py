def summ():


nonself = set()

for num in range(1, 10001):
    temp = sum(map(int, str(num))) + num
    nonself.add(temp)

for j in range(1, 10001):
    if j not in nonself:
        print(j)