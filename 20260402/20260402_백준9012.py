'''
N = int(input())
switch = True

for i in range(N):
    count = 0
    string = input()
    for j in range(len(string)):
        if(string[j] == "("):
            count += 1
        elif(string[j] == ")"):
            count -= 1

        if(count < 0):
            switch = False
            break

    if(count == 0):
        switch = True
    else:
        switch = False

    if(switch):
        print("YES")
    else:
        print("NO")
'''

# 리팩토링
N = int(input())

for i in range(N):
    count = 0
    string = input()
    for j in range(len(string)):
        if(string[j] == "("):
            count += 1
        elif(string[j] == ")"):
            count -= 1
        if(count<0):
            break

    if(count == 0):
        print("YES")
    else:
        print("NO")