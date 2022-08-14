# https://school.programmers.co.kr/learn/courses/30/lessons/43162

# DFS 방법
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            # DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
            # ex) 1번 컴퓨터에서 시작해서 만약 다른 컴퓨터와 연결된다면 계속 방문할 수 있다.
            answer += 1 
    return answer

def DFS(n, computers, com, visited):
    # 해당 컴퓨터 방문처리 하기
    visited[com] = True
    # 해당 컴퓨터와 연결된 다른 컴퓨터 찾기
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: # 연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)

# BFS 방법
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            # BFS로 한 컴퓨터 방문할 때, 연결된 컴퓨터를 큐에 넣고 빼면서 방문 처리
            # 연결이 안 되어있는 컴퓨터는 따로 BFS 진행
            answer += 1
    return answer

def BFS(n, computers, com, visited):
    # 해당 컴퓨터 방문처리 하기
    visited[com] = True
    queue = []
    # 해당 컴퓨터 큐에 넣기
    queue.append(com)
    while len(queue) != 0:
        # 큐에서 첫번째 요소 빼면서 방문처리
        com = queue.pop(0)
        visited[com] = True
        # 해당 컴퓨터와 연결된 다른 컴퓨터 찾기
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                # 연결된 컴퓨터 방문 안 되어있으면 큐에 넣기
                if visited[connect] == False:
                    queue.append(connect)



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


# 한 노드에서 탐색을 시작해 최대한 방문한 것을 1개의 트리로 계산하기.
# 구하려는 네트워크의 갯수는 트리의 갯수와 같다. DFS 또는 BFS 방법으로 구할 수 있다.