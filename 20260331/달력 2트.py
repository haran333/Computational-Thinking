month = int(input())
month_31 = [1, 3, 5, 7, 8, 10, 12]
empty = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2] # 달력 앞 공백 칸 수
count = 1

print('\t',month,'월',sep='')
print('일 월 화 수 목 금 토')

if month == "2":
    num = 29
elif (int(month) in month_31):
    num = 32
else:
    num = 31

count += empty[month-1]
print("   "*empty[month-1], end= '')
for i in range(1, num):
    if count % 7 != 0:
        print(f"{i:>2}", end=' ')
    else:
        print(f"{i:>2}")
    count += 1