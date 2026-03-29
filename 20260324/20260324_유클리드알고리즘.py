a = int(input())
b = int(input())

while (b!=0):
    x = a
    a = b
    b = x%b

print(a)