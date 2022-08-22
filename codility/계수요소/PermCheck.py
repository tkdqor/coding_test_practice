# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

def solution(A):
    # write your code in Python 3.6
    
    # 배열 A의 개수와 max(A)가 같아야 한다.
    if len(A) == max(A):
        return 1
    else:
        return 0


print(solution([4,1,3,2]))
# A = [4,1,3,2] => 이렇게 1부터 N개의 요소가 1번씩 다 들어가 있으면 순열 / 4개이니까 1부터 4까지 1번씩 들어가 있음
# A = [4,1,3] => 이 경우에는 2가 없기 때문에 순열이 아님
# 그래서 주어진 배열 A가 순열인지 확인하는 것 / 순열이면 1을 반환하고 그렇지 않으면 0을 반환하기


###### 더 점수가 높은 답안 ######
def solution(A):
    # write your code in Python 3.6
    if sum(A) == sum(range(1, len(A)+1)):
        return 1
    else:
        return 0