# https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    # 총 필요한 놀이기구 이용 금액을 result로 설정
    result = 0
    # count만큼 for문을 진행해서 총 금액 result 계산
    for i in range(count):
        result += (price * (i+1))
    # 만약 지금 가지고 있는 돈인 money가 result보다 크면 0 return, 
    # 아니면 모자란 금액 return
    if money >= result:
        return 0
    else:
        result -= money
        return result
