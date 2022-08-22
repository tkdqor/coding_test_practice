# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

def solution(N, A):
    B = [0] * N  #새로운 Array 생성
    for i in range(len(A)):
        if 1 <= A[i] <= N:
            B[A[i]-1] +=1
        elif A[i] > N:
            B = [max(B)] * N
    return B

print(solution(5, [3,4,4,6,1,4,4]))


# 처음에는 0으로 설정된 N개의 카운터가 제공되며 두 가지 작업이 가능 / ex) N=5이면, (0, 0, 0, 0, 0)
# increase(X) => 카운터 X가 1만큼 증가
# max counter => 모든 카운터는 그 때까지의 카운터중에서 최대값을 전부 적용
# A[K] = X, 1 ≤ X ≤ N인 경우 연산 K는 카운터중에서 X번째를 increase(X)
# A[K] = N + 1이면 작업 K는 max count
# N = 5 그리고 배열 A = [3,4,4,6,1,4,4]