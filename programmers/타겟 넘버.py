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