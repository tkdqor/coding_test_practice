# https://fre2-dom.tistory.com/103 블로그 답변

import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드


# DFS로 가로 노드를 방문하고 연결된 모든 노드들도 방문
def dfs_horizontal(x, y):

    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "-":

        # 해당 노드 방문 처리
        graph[x][y] = "x"

        # 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs_horizontal(x, y - 1)
        dfs_horizontal(x, y + 1)

        return True
    return False


# DFS로 세로 노드를 방문하고 연결된 모든 노드들도 방문
def dfs_vertical(x, y):

    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "|":

        # 해당 노드 방문 처리
        graph[x][y] = "x"

        # 상, 하의 위치들도 모두 재귀적으로 호출
        dfs_vertical(x - 1, y)
        dfs_vertical(x + 1, y)

        return True
    return False


n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline()))

cnt = 0
# n 세로, m 가로
for i in range(n):
    for j in range(m):
        # "-" 일 때 dfs_horizontal 호출
        if graph[i][j] == "-":
            dfs_horizontal(i, j)
            cnt += 1
        # "|" 일 때 dfs_vertical 호출    
        elif graph[i][j] == "|":
            dfs_vertical(i, j)
            cnt += 1

print(cnt)