# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):
    # write your code in Python 3.6
    if sum(A) == 0:
        return 1
    else:
        return sum(range(1, len(A)+2)) - sum(A)
    

print(solution([2,3,1,5]))

# 리스트 A의 개수가 4개라면, 1개가 비었으니 원래 개수는 5개이어야 한다.
