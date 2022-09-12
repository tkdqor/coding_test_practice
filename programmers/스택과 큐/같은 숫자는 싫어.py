# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
def solution(arr):
    check = []
    result = []
    for i in range(len(arr)):
        if len(check) == 0:
            check.append(arr[i])
        else:
            if arr[i] == check[0]:
                continue
            else:
                result.append(check[0])
                check = []
                check.append(arr[i])
    result.append(check[0])
    return result

print(solution([1, 1, 3, 3, 0, 1, 1]))