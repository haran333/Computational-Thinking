example = [1, 1, 2, 2, 2, 8]
user = input().split()

for i in range(len(example)):
    user[i] = example[i]-int(user[i])

print(' '.join(map(str,user)))