# https://school.programmers.co.kr/learn/courses/30/lessons/92342
# https://velog.io/@sewonkim/2022-KAKAO-BLIND-RECRUITMENT-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4

def calcPoint(apeach, lion):
    apeach_score = 0
    lion_score = 0
    for i in range(11):
        if apeach[i] == lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            apeach_score += 10 - i
        else:
            lion_score += 10 - i
    return lion_score - apeach_score

# 지금쏘는 과녁 idx, 남은 화살 개수, 어피치점수, 내점수
def DFS(idx, n, apeach, lion):
    global answer, point
    if n < 0:
        return
    #점수 계산
    if idx > 10:
        diff = calcPoint(apeach, lion)
        if diff <= 0:
            return
        if diff > point:
            point = diff
            answer = [lion[i] for i in range(11)]
            answer[10] += n            
        return

    #상대가 쏜 점수보다 높이 쏴본다
    lion[10-idx] = apeach[10-idx]+1
    DFS(idx+1, n-lion[10-idx], apeach, lion)
    lion[10-idx] = 0
    DFS(idx+1, n, apeach, lion)

def solution(n, info):
    global answer, point
    answer = [-1]
    point = 0
    DFS(0, n, info, [0 for _ in range(11)])
    return answer


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))


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
