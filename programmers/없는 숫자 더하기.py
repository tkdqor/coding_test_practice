# https://school.programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    # 0부터 9까지 더한 수에서 numbers 합 빼주기
    answer = sum(range(10)) - sum(numbers)
    return answer