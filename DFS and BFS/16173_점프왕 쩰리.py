# n = int(input())
# graph = [[]]

# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# x, y = 1, 1
# count = 0

# dx = [0, 1]
# dy = [1, 0]


# def jelly(x, y, n):
#     if (x != n and y != n):
#         # 먼저 오른쪽으로 보내기
#         nx = x + dx[0]
#         ny = y + dy[0]
#         if x <= n and y <= n:
#             x, y = nx, ny
#             count = graph[x][y]
#             # 이동한 위치의 숫자로 먼저 오른쪽 보내기
#             for _ in range(count):
#                 if x <= n and y <= n:
#                     x += count
#                 else:
#                     y += count

#         # n보다 크면 아래쪽으로 보내기
#         else:
#             nx = x + dx[1]
#             ny = y + dy[1]
#             x, y = nx, ny
#             count = graph[x][y]
#             # 이동한 위치의 숫자로 먼저 오른쪽 보내기
#             for _ in range(count):
#                 if x <= n and y <= n:
#                     x += count
#                 else:
#                     y += count

###################### 실패한 풀이.. #######################


# https://fre2-dom.tistory.com/105 해당 블로그 풀이

import sys
from collections import deque


# bfs 함수 정의
def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True

    # 큐에 탐색해야 하는 노드 없을 때까지 실행
    while queue:

        a, b = queue.popleft()
        # 칸에 쓰여있는 수를 check라고 정의
        check = graph[a][b]

        # 현재 위치가 승리 지점이면 멈춰 성공 메시지 출력
        if check == -1:
            print("HaruHaru")
            return

        # 우, 하를 이동하여 비교
        for dx, dy in (1, 0), (0, 1): # 처음에는 하로 이동하고 / 그 다음에는 우로 이동
            x = a + dx * check
            y = b + dy * check

            # 정사각형 구역 내부이고 한번도 방문하지 않았으면 노드를 큐에 넣고 방문 처리한다.
            if 0 <= x < n and 0 <= y < n and visited[x][y] == False:
                queue.append((x, y))
                visited[x][y] = True

    # 모든 상황에서 승리 지점을 가지 못하면 실패 메시지 출력
    print("Hing")


n = int(sys.stdin.readline())
# 2차원 그래프로 표현
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 탐색 여부
visited = [[False] * n for _ in range(n)]
# 탐색
bfs()



#### (0, 0)에서 시작해서 큐에 넣고 방문처리하고 큐에서 빼기 
#### 아래로 이동하고 해당 좌표를 큐에 넣고 방문처리
#### 그리고 다시 (0, 0) 에서 오른쪽로 이동하고 해당 좌표를 큐에 추가로 넣고 방문처리
#### 그 다음 큐 자료구조이니까 먼저 넣었던 아래의 좌표를 큐에서 빼기
#### 그리고 다시 아래로 움직였던 좌표 기준으로 아래 / 오른쪽로 이동..


#### 아래, 오른쪽으로만 이동할 수 있으므로 두 방향을 반복하여 조건에 맞게 한 번씩 다 이동해서 탐색해 보는 것..!

#### 해당 문제를 bfs로 푸는 이유는, 내 생각엔 모든 칸을 갈 필요가 없고 오른쪽과 아래만 가능하니까 최단 경로를 찾는 느낌으로 
#### bfs를 사용한 것 같다!