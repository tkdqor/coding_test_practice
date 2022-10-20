# https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    score = ['0','1','2','3','4','5','6','7','8','9','10']
    bonus = ['S', 'D', 'T']
    option = ['*', '#']
    check = ''
    result = 0
    total_result = []
    
    for idx, i in enumerate(dartResult):
        if i in score:
            if dartResult[idx+1] in score:
                check += i
            else:
                check += i
                result = int(check)
                check = ''
        if i in bonus:
            if i == 'S':
                result = result ** 1 
            elif i == 'D':
                result = result ** 2
            elif i == 'T':
                result = result ** 3
            total_result.append(result)
        if i in option:
            if i == '*' and len(total_result) == 1:
                total_result[-1] = total_result[-1] * 2
            elif i == '*':
                total_result[-1] = total_result[-1] * 2
                total_result[-2] = total_result[-2] * 2
            elif i == '#':
                total_result[-1] = total_result[-1] * (-1)
    return sum(total_result)