def hanoi(N, start, mid, end):
    if N == 1: # 옮길 원반이 1번
        print(f'{N}번 원반: {start} -> {end}') # 종료
    else:
        hanoi(N-1, start, end, mid) # N-1번 원반의 목적지가 경유지
        print(f'{N}번 원반: {start} -> {end}')
        hanoi(N-1, mid, start, end) # N-1번 원반을 다시 목적지로

if __name__ == '__main__':
    N = int(input())
    hanoi(N, "A", "B", "C")
    print(2**(N)-1)