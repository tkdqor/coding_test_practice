n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]  # n번 만큼 for문을 돌려서 리스트안에 0이 m개인 리스트가 n개 들어있게끔 설정
x, y, direction = map(int, input().split())
d[x][y] = 1                      # 받은 x,y 값을 리스트 안에 리스트에 대입해서 해당 값을 1로 처리 / 즉, 현재 좌표를 방문 처리

array = []                       # n번만큼 for문으로 돌려서 전체 맵 정보 행 1줄씩을 array 리스트에 추가
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수 정의
def turn_left():
    global direction     # 함수 밖에서 선언된 direction 전역변수 사용
    direction -= 1       # direction을 1씩 빼면 왼쪽으로 회전하게 됨
    if direction == -1:  # 만약 -1이라면 0인 북쪽에서 뺀 거니까 
        direction = 3    # 서쪽으로 해주기

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]  # turn_left 함수 호출 후 바뀐 direction으로 dx,dy 리스트 값을 가져오고 기존 x,y에 더하기
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1                           # 방문 처리
        x = nx                                  # x와 y 모두 nx와 ny로 대체
        y = ny 
        count += 1                              # 캐릭터가 방문한 횟수 +1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction] 
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:  # 뒤로가는 칸이 안 가본 칸인 경우 이동
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)
        




