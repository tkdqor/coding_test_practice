# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):
    # write your code in Python 3.6
    result_list = []

    for P in range(1, len(A)):
        left = sum(A[0:P])
        right = sum(A[P:len(A)])
        result = left - right
        result_list.append(result)
    
    answer = list(map(abs, result_list))
    
    return min(answer)


A = [3,1,2,4,3]
print(solution(A))

# P = 1이라면, 인덱스 0부터 p-1까지 더한값과 / p부터 인덱스 n-1까지 더한값(즉 끝까지 다) / 이 둘의 차이의 절대값
# 그래서 이 차이 중에서 최소값을 구하기

# p를 1부터 쭉 대입하면서 len(A)-1 까지 대입하다가 => 리스트 슬라이싱 진행 => 그러면서 나온 차이값을 리스트에 하나씩 저장해서 나중에 min(리스트)하기