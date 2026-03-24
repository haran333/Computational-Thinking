time = 0
sum = 0

for i in range(4):
    time = int(input())
    sum += time

print(sum//60)
print(sum%60)