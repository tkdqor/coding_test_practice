# https://school.programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    equal_count = 0
    zero_count = 0
    ranking = [6, 6, 5, 4, 3, 2, 1]
    
    for i in lottos:
        if i in win_nums:
            equal_count += 1
        
        if i == 0:
            zero_count += 1

    return ranking[equal_count + zero_count], ranking[equal_count]