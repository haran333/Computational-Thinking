a, b, c = map(int, input().split())

if (a*a+b*b == c*c):
    print("직각삼각형")
elif (a*a+b*b < c*c):
    print("둔각삼각형")
else:
    print("예각삼각형")