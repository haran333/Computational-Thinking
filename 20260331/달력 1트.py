month = input()
th_one = [1, 3, 5, 7, 8, 10, 12]
count = 1
dict = {
    "1": 4,
    "2": 0,
    "3": 0,
    "4": 3,
    "5": 5,
    "6": 1,
    "7": 3,
    "8": 6,
    "9": 2,
    "10": 4,
    "11": 0,
    "12": 2
}

print('           ',month,'월',sep='')
print('일 월 화 수 목 금 토')

if month == "2":
    count += dict[month]
    for i in range(1, 29):
        if(i//10 == 0):
            if count % 7 != 0:
                print(f" {i}", end=' ')
            else:
                print(f" {i}")
        else:
            if count % 7 != 0:
                print(i, end=' ')
            else:
                print(f"{i}")
        count += 1
elif (int(month) in th_one):
    count += dict[month]
    print("  "*dict[month], end='')
    for i in range(1, 32):
        if(i//10 == 0):
            if count % 7 != 0:
                print(f" {i} ", end='')
            else:
                print(f" {i}")
        else:
            if count % 7 != 0:
                print(f"{i} ", end='')
            else:
                print(f"{i} ")
        count += 1
else:
    count += dict[month]
    print("  "*dict[month], end='')
    for i in range(1, 31):
        if(i//10 == 0):
            if count % 7 != 0:
                print(f" {i} ", end='')
            else:
                print(f" {i}")
        else:
            if count % 7 != 0:
                print(f"{i} ", end='')
            else:
                print(f"{i} ")
        count += 1