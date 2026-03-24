import datetime

now_time = datetime.datetime.now()

if (3 <= now_time.month <= 5):
    print("봄")
elif ( 6 <= now_time.month <= 8):
    print("여름")
elif ( 9 <= now_time.month <= 11):
    print("가을")
else:
    print("겨울")