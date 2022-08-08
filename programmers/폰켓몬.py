# https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    answer = len(nums) // 2
    c = len(set(nums))
    if c < answer:
        answer = c
    
    return answer