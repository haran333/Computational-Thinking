a = int(input())
b = ((a%10)+(a//10))%10 + (a%10)*10
count = 1

while a!=b :
    b = ((b%10)+(b//10))%10 + (b%10)*10
    count+=1
print(count)