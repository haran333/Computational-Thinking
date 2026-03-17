str_day = input("요일 입력: ")
since = int(input("숫자 입력: "))

list_day  = {1:"월요일", 2:"화요일", 3: "수요일", 4: "목요일", 5: "금요일", 6: "토요일", 7: "일요일"}

for a, b in list_day.items():
    if(str_day == b):
        num_day = a
        if(since%num_day==0):
            print(list_day[7])
        else:
            print(list_day[(since%num_day)])