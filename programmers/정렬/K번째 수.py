# https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    result_list = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        array_sli = array[i-1:j]
        array_sli.sort()
        result = array_sli[k-1]
        result_list.append(result)
        
    return result_list

### 더 간결한 풀이
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer