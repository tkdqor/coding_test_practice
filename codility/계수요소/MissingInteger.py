# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

def solution(A):
    A.sort()
    A = list(set(A))
    missingdata = 1
    for i in A:
        if i == missingdata :
            missingdata +=1
    return missingdata

print(solution([1, 3, 6, 4, 1, 2]))

# 배열 A가 주어지면 A에서 발생하지 않는 가장 작은 양의 정수를 반환 ex) A = [1,3,6,4,1,2] 이면 5를 반환
# A = [1, 2, 3]이면 4를 반환
# A = [−1, −3]이면 1를 반환
