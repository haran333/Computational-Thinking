# 1
'''
N = int(input())
book = {}

for i in range(N):
    name = input()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1

book = sorted(book.items(), key=lambda item:item[1], reverse=True)

key = []
for j in book:
    if book[0][1] != j[1]:
        break
    else:
        key.append(j[0])
key.sort()
print(key[0])
'''

# 2
N = int(input())
book = {}

for _ in range(N):
    name = input()
    book[name] = book.get(name, 0) + 1 # name이 없을 경우 기본값 0 반환 / 반환값에 +1

max_count = max(book.values())

key = [name for name, count in book.items()
       if (count == max_count)]
print(min(key))