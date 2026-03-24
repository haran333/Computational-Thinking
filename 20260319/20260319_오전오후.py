import datetime

now_time = datetime.datetime.now()

if (now_time.hour < 12):
    print("오전")
else:
    print("오후")