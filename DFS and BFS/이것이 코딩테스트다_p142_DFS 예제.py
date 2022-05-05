# DFS 메서드 정의
def dfs(graph, v, visited):                # v는 노드를 의미하는 매개변수 
    # 현재 노드를 방문 처리 - 스택에 넣는 것
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:                 # 방문하지 않아 false라면
            dfs(graph, i, visited)         # DFS 함수 호출


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],  # 1번 노드와 연결된 다른 노드
    [1, 7],     # 2번 노드와 연결된 다른 노드
    [1, 4, 5],  # 3번...
    [3, 5], 
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]      # 8번 노드와 연결된 다른 노드
]


# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9   # 맨 처음, 리스트안에 False가 9개가 들어가게끔 설정


# 정의된 DFS 함수 호출
dfs(graph, 1, visited)  # 시작 노드가 1번이라서 v에 1을 삽입하고 DFS 함수 호출



