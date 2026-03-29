star = int(input())

if (star%2 == 0):
    for i in range(1, star+1):
        print("* "*(star//2))
        print(" *"*(star//2))
else:
    for i in range(1, star+1):
        print("*"+" *"*(star//2))
        print(" *"*(star//2))