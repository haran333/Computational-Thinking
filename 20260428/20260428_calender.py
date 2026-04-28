N = int(input())
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count = 0

if N == 1:
    empty = 1
else:
    empty = (sum(month[:N-1])+1)%7

print("Su Mo Tu We Th Fr Sa")
print(" "*3*empty, end='')
count = empty
for i in range(month[N-1]):
    count += 1
    if count%7 != 0 and count != 0:
        print(f"{i+1:2d}", end=' ')
    else:
        print(f"{i+1:2d}")