import time

n = int(input(""))
start_time = time.time()
prime = True

if n == 1:
    prime = False
elif n == 2:
    prime = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        prime = False

if prime:
    print("소수")
else:
    print("소수아님")
print(time.time()-start_time)