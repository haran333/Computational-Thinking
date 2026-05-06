import random
import numpy as np
# N을 받는 지역 변수를 모든 함수에 추가하는 것보다 전역 변수를 쓰는 것이 더 나은 듯
N = int(input()) 

def MatRandom():
    return np.array([[random.randrange(1,N*N*10) for _ in range(N)] for _ in range(N)])

def Matprint(Matrix):
    print('='*10)
    for i in range(N):
        for j in range(N):
            print(f"{Matrix[i][j]:2d}", end=' ')
        print()
    print('='*10)

A = MatRandom()
B = MatRandom()
C = MatRandom()

Matprint(A)
Matprint(B)
Matprint(C)
Matprint(np.dot(A, B)+C)