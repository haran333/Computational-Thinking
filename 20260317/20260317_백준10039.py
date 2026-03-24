sum = 0
for i in range(5):
    grade = int(input())
    if (grade<40):
        sum+=40
    else:
        sum+=grade

print(sum//5)