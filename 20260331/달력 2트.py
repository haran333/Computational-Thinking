month = int(input())
th_one = [1, 3, 5, 7, 8, 10, 12]
empty = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
count = 1

print('\t',month,'월',sep='')
print('일 월 화 수 목 금 토')

if month == "2":
    num = 29
elif (int(month) in th_one):
    num = 32
else:
    num = 31

count += empty[month-1]
for i in range(1, num):
        if(i//10 == 0):
            if count % 7 != 0:
                print(f" {i}", end=' ')
            else:
                print(f" {i}")
        else:
            if count % 7 != 0:
                print(i, end=' ')
            else:
                print(i)
        count += 1