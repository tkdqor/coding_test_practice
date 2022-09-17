# https://school.programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    result = [0] * 11
    score = [10,9,8,7,6,5,4,3,2,1,0]
    apeach = 0
    new_ryan = 0
    ryan = 0
    
    while True:
        # for문으로 info의 인덱스와 값 뽑아서 result의 값을 +1해서 설정하기
        for idx, x in enumerate(info):
            result[idx] = x+1
            # 한 번 result에 값 설정할 때마다 n값을 빼기
            n -= result[idx]
            # n이 0이면 어피치와 라이언의 최종점수 계산하기
            if n == 0:
                for i in range(11):
                    if info[i] > result[i]:
                        apeach += score[i]
                    elif info[i] < result[i]:
                        new_ryan += score[i]
                # 계산한 점수가 라이언이 더 크면 result 리턴하기 / 어피치가 더 크면 -1 리턴하기
                if apeach < new_ryan:
                    ryan = new_ryan
                    # return result
                else:
                    return [-1]
            # n이 0보다 작아지면 n과 result 값을 원래 숫자로 돌려놓고, 이어서 for문 진행시키기
            elif n < 0:
                n += x+1
                result[idx] = 0
                continue
            # n이 0과 같은것도 아니고, 0이 더 큰 것도 아니면 이어서 for문 진행시키기
            else:
                continue




## 지금, 계산한 점수가 라이언이 더 크면 바로 result를 리턴하는 게 아니고 새로 계산한 new_ryan이 기존 라이언보다 클 떄만 리턴..
## 그래서 최종 계산 점수 이후에 다시 한 번 for문을 돌려서 가장 과녁점수 높은 경우를 제외하고 다시 시작...그렇게 해서 계산한 점수를 계속 비교...!!
# 라이언이 맞힌 화살 개수가 가장 큰 과녁 점수를 포기하고 그 밑으로 과녁 점수를 배분.해보기!!
# while 다음에 if문 사용할 생각해보자!
# https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%8A%A4%ED%83%9D%EA%B3%BC%20%ED%81%90/%EA%B8%B0%EB%8A%A5%EA%B0%9C%EB%B0%9C.py 
# 이 문제 참고해보기!
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))


'''
1부터 10점까지 있는데, 그 k점을 어피치가 a발 맞추고 / 라이언이 b발을 맞출 때,
더 많은 화살을 k점에 맞힌 선수가 그 k점을 가져가게 된다.
단, a = b일 경우에는 어피치가 k점을 가져간다.
a = b = 0 / 즉, 라이언과 어피치 모두 k점에 하나도 맞히지 못한 경우에는 어느 누구도 k점을 가져가지 않는다.
이렇게 해서 모든 과녁 점수에 대해서 각 선수의 최종 점수를 계산
최종 점수가 같은 경우, 어피치를 우승자로 결정한다
현재 상황은 어피치가 화살 n발을 다 쏜 후이고 라이언이 화살을 쏠 차례
라이언은 어피치를 가장 큰 점수 차이로 이기기 위해서 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 구하려고 한다.
n은 선수가 쏜 화살의 개수를 담은 자연수
info는 어피치가 맞힌 과녁 점수의 개수를 10점부터 0점까지 순서대로 담은 정수 배열을 의미
info = [2,1,1,1,0,0,0,0,0,0,0] 라면 -> 10점에 2번, 9점에 1번 ...
라이언이 가장 큰 점수 차이로 우승하기 위해 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지 
10점부터 0점까지 순서대로 정수 배열에 담아 return
만약, 라이언이 우승할 수 없는 경우(지거나 비기는 경우) -1을 return
라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return
가장 낮은 점수를 맞힌 개수가 같을 경우 계속해서 그다음으로 낮은 점수를 더 많이 맞힌 경우를 return 
ex) 
'''
# result = [0] * 11 / info리스트 요소를 for문으로 하나씩 뽑아서 그 요소값보다 큰 수를 result의 요소로 설정..이 때 n을 초과하면 그 다음
# 과녁점수로 내려가서 추가해보기..!
# 근데, result 요소값의 합이 n이 되면 종료..
# 최종점수를 계산했을 때 라이언이 크면 종료 / 도저히 없으면 return -1
# 최종점수를 계산한 상태에서 또 while문을 돌려서 더 낮은 점수를 찾으면 그걸로...
# apeach = 0 / ryan = 0
