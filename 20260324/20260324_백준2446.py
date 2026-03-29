N = int(input())

for i in range(1, N+1):
    print(f"{" "*(i-1)}{"*"*(2*(N-i)+1)}")
for i in range(1, N):
    print(f"{" "*(N-i-1)}{"*"*(2*i+1)}")