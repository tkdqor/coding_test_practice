# https://app.codility.com/c/run/trainingSA3E9J-M8P/

def solution(X, Y, D):
    distance = Y-X
    Q = distance//D          # 몫
    R = distance%D           # 나머지
    if R == 0:
        return Q
    elif R < D:       # R != 0 이것도 상관없을 듯 합니다
        return Q+1

print(solution(10, 85, 30))