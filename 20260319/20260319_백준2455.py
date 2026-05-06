sum = 0
high = 0

for i in range(4):
    N1, N2 = map(int, input().split())
    sum += N2 - N1
    if(high < sum):
        high = sum
print(high)