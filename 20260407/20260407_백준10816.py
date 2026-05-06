# 딕셔너리
N = int(input())
example = list(map(int, input().split()))
M = int(input())
Ns = list(map(int, input().split()))

dic = {}

for i in Ns:
    dic[i] = 0
for j in example:
    if (j in dic):
        dic[j] += 1

# print(*list(dic.values()))  -> Ns에 중복된 숫자가 있을 경우, 안 됨
print(*[dic[key] for key in Ns]) #얘는 key로 불러오는거라서, 중복 유무 상관 X