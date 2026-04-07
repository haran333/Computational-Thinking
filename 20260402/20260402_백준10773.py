N = int(input())
num = []
sum = 0

for i in range(N):
    temp = int(input())
    if(temp != 0):
        num.append(temp)
    else:
        del num[-1]
for j in range(len(num)):
    sum += num[j]
print(sum)