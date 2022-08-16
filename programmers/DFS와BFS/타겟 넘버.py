# https://school.programmers.co.kr/learn/courses/30/lessons/43165
answer = 0
# idx는 numbers 리스트에서 사용한 숫자의 개수 / value는 그 숫자들을 조합해서 만든 수
# 그래서 idx와 N이 같아야 numbers 모든 요소를 사용한 게 되고 / target과 value가 같아야 된다.
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx == N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))

# idx는 numbers라는 리스트의 순서를 의미하는듯하다.
# numbers 리스트의 요소들을 전부 사용해서 target을 만들어야 하니까 if idx == N이라는 조건이 붙는다.
# 그래서 idx == N인 상태에서 만든 value가 target이랑 같으면 answer 올려주고 재귀함수가 취소되는 것이고
# idx == N이기만 하면 재귀함수만 취소되는 것이다.