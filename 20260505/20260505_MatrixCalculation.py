import random
# N을 받는 지역 변수를 모든 함수에 추가하는 것보다 전역 변수를 쓰는 것이 더 나은 듯
N = int(input()) 

def MatRandom():
    return [[random.randrange(1,N*N*10) for _ in range(N)] for _ in range(N)]

def Matprint(Matrix):
    print('='*10)
    for i in range(N):
        for j in range(N):
            print(f"{Matrix[i][j]:2d}", end=' ')
        print()
    print('='*10)

def MatPlus(Mat1, Mat2):
    return [[Mat1[i][j]+Mat2[i][j] for j in range(N)] for i in range(N)]

def MatMult(Mat1, Mat2):
    #return [[sum([Mat1[i][k]*Mat2[k][j] for k in range(N)]) for j in range(N)] for i in range(N)]
    List = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                List[i][j] += Mat1[i][k]*Mat2[k][j]
    return List

A = MatRandom()
B = MatRandom()
C = MatRandom()

Matprint(A)
Matprint(B)
Matprint(C)

Matprint(MatPlus(MatMult(A, B), C))