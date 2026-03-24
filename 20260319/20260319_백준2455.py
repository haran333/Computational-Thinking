sum = 0
high = 0

for i in range(4):
    num1, num2 = map(int, input().split())
    sum += num2 - num1
    if(high < sum):
        high = sum
print(high)