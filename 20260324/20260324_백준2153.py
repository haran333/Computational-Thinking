word = list(input(''))
sum = 0
prime = True

for i in word:
    if(64<ord(i)<96):
        sum += ord(i)-64 + 26
    else:
        sum += ord(i)-96

if sum == 1:
    prime = True
elif sum == 2:
    prime = True

for j in range(2, int(sum**0.5) + 1):
    if sum % j == 0:
        prime = False

if prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")