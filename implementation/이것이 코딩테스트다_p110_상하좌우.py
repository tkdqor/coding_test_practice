# n = int(input())
# data = input().split()

# x, y = 1, 1
# types = ['L', 'R', 'U', 'D']

# for i in data:
#     if i == types[0]:
#         if y == 1:
#             pass
#         y - 1
#     elif i == types[1]:
#         y + 1
#     elif i == types[2]:
#         if x == 1:
#             pass
#         x - 1
#     else:
#         x + 1
    
# print(x, y)

###################### 실패한 풀이 #######################

n = int(input())
x, y = 1, 1                # 시작 위치는 (1, 1)로 고정되어 있으니 x,y로 정해주기
plans = input().split()    # 문자 여러 개가 주어졌을 때, 다음과 같이 입력하면 리스트로 담겨진다

# 리스트 순서대로 L, R, U, D 이동 방향 정의
dx = [0, 0, -1, 1]                   # ex) dx[0]과 dx[0]은 L의 이동방향을 정의한 것
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']


for plan in plans:                              # 문자 1개씩 출력 시, 
    for i in range(len(move_types)):            # 0부터 3까지 뽑아서 
        if plan == move_types[i]:               # 문자가 서로 같으면, x,y값을 이동시키기
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:    # x와 y가 1보다 작으면 안되고 / x와 y가 n보다 크면 안됨
        continue                                # continue는 아래 코드를 실행하지 않고 건너뛰는 것을 의미
    x, y = nx, ny                               # 문자 1개씩 출력해서 바뀐 x,y 대입

print(x, y)
