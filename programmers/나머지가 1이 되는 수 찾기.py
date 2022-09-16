def solution(n):
    x = 0
    # n를 x로 나눈 나머지가 1이 될때까지 x += 1하면서 while문 진행
    while True:
        x += 1
        if n % x == 1:
            return x