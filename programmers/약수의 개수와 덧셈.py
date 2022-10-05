# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    # return 값인 result를 0으로 설정
    result = 0
    # left에서 right를 하나씩 빼서 약수 개수 구하기
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        # 약수의 개수가 짝수이면 result에 더해주고, 홀수이면 빼주기
        if count % 2 == 0:
            result += i
        else:
            result -= i
    return result