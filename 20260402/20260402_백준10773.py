nonself = set([N i//10000 + i//1000 + i//100 + i//10 + i%10 + i for i in range(1, 10001)])

for j in range(1, 10000):
    if j not in nonself:
        print(j)

#시험 문제
# 한 문제는 내용을 이해하는 것, 다른 한 문제는 코드를 짜는 것(단순한 문법 문제 X 생각을 해라 재귀함수는 시험 범위 아님)