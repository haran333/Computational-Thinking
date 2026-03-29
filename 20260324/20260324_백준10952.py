switch = True
while switch:
    a, b = map(int, input().split())
    if(a==0 and b==0):
        switch = False
    else:
        print(a+b)