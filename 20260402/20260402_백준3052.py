remain = ['']*10
for i in range(10):
    remain[i] = int(input()) % 42
remain = set(remain)
print(len(remain))