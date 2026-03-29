star = int(input())

for i in range(1, star+1):
    if (star%2 == 1):
        a = star//2
        for j in range(a):
            print("* ")
    print(f"{"*"*i}{"\b"*star}")