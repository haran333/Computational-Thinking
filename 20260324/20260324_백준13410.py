n,k = map(int,input().split())
value = []
for i in range(1,k+1) :
   value.append(str(n*i)[::-1])

value = list(map(int, value))
print(int(max(value)))