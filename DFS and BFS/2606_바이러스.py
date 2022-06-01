# import sys
# from collections import deque



# def bfs():
#     queue = deque()
#     queue.append(1)
#     visited[1] = True
#     count = 0

#     while queue:
#         computer = queue.popleft()

#         for x, y in graph:
#             if x == computer:
#                 warm = y
#                 if visited[warm] == False:
#                     queue.append(warm)
#                     visited[warm] = True
#                     count += 1
    
#     print(count)



# n = int(sys.stdin.readline())
# connect = int(sys.stdin.readline())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(connect)]
# visited = [False] * (n + 1)

# bfs()


###################### 시간초과... 답안 ###########################

# https://fre2-dom.tistory.com/88 해당 블로그 풀이

import sys


# dfs 함수
def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = 1

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


n = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

# 각 노드가 연결된 정보를 표현
# 0이 n+1개가 담긴 리스트를 0번 노드부터 n번 노드까지 반복해서 담기
graph = [[0] * (n + 1) for i in range(n + 1)]

for i in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

# 각 노드의 방문유무
visited = [0] * (n + 1)

dfs(1)
# visited 리스트에서 1의 개수를 세고 처음 1번 컴퓨터를 제외해야 하니까 1 빼고 세기
print(visited.count(1) - 1)


#### 해당 문제는 1번 컴퓨터와 연결된 모든 경로를 다 확인해봐야 하니까 DFS로 푸는 것으로 이해했다!