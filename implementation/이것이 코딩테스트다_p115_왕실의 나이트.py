input_data = input()
row = int(input_data[1])                              # 문자열도 슬라이싱이 가능하니까 열과 행을 따로 받기
column = int(ord(input_data[0])) - int(ord('a')) + 1  # ord 함수는 문자의 유니코드 값을 돌려주는 함수 / a는 97이므로 받은 문자 유니코드 - a의 유니코드 +1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 나이트가 이동할 수 있는 8가지 방향 정의

result = 0

for step in steps:                   # 방향 1가지를 빼서
    next_row = row + step[0]         # row에 더하고
    next_column = column + step[1]   # column에도 더하기
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:  # 그 결과가 8 X 8 좌표 평면을 벗어나지 않는 경우, +1
        result += 1

print(result)