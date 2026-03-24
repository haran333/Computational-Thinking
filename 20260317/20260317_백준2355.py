num1, num2 = map(int,input().split())
num1, num2 = min(num1, num2), max(num1, num2)
sum = (num2*(num2+1))//2 - (num1*(num1+1))//2

print(sum+num1)