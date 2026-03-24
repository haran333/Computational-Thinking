N = int(input())
low = 9999
y= N//3

while(y>-1):
    if ((N-3*y)%5==0):
        x = (N-3*y)//5
        if(low>x+y):
            low = x+y
    y = y-1
if(low==9999):
    print(-1)
else:
    print(low)