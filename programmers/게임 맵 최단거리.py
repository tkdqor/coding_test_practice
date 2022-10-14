from collections import deque

def solution(maps):
    # 아래쪽, 오른쪽, 위쪽, 왼쪽 좌표 정의
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]

    # 행 개수와 열 개수 구하기
    x_h, y_h = (len(maps[0]), len(maps))
    queue = deque([(0, 0, 1)])

    while queue:
        # x좌표, y좌표, 칸의 개수를 0,0,1로 설정
        x, y, d = queue.popleft()

        # 지금 위치에서 for문으로 아래쪽, 오른쪽, 위쪽, 왼쪽으로 움직이기
        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]

            # 움직인 위치가 -1보다는 크고 전체 행과 열 개수보다는 작은지 확인
            if nx > -1 and ny > -1 and nx < x_h and ny < y_h:
                # 움직인 위치가 1과 같거나 d+1보다 큰 경우에는 해당 위치 값을 d+1로 바꿔주기
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:
                    maps[ny][nx] = d + 1
                    # 만약 해당 위치의 행과 열이 maps 우측 하단이면 d+1 반환하고 종료
                    if nx == x_h - 1 and ny == y_h - 1:
                        return d + 1
                    # maps 우측 하단이 아니면 queue에 추가하기
                    queue.append((nx, ny, d + 1))

    # while문을 다 진행하고도 종료되지 않는다면 상대 진영에 도달하지 못한 것으로 -1 반환
    return -1