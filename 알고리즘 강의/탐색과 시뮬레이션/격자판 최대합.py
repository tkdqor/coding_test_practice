n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# 최대값을 구하는 largest 변수 / 먼저 가장 작은 값으로 설정
largest = -2147000000
for i in range(n):
    # 행의 합은 sum1, 열의 합은 sum2로 설정
    sum1 = sum2 = 0
    for j in range(n):
        # 행의 합은 a 리스트 i행의 0부터 마지막까지의 j열을 다 더한 값
        sum1 += a[i][j]
        # 열의 합은 a 리스트 i열의 0부터 마지막까지의 j행을 다 더한 값
        sum2 += a[j][i]
    # 해당 if문을 통해 행의 합과 열의 합에서 가장 큰 수를 계산
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 이제 대각선의 합 구하기
sum1 = sum2 = 0
for i in range(n):
    # 격자판 왼쪽 끝부터 오른쪽 아래까지의 대각선 합
    sum1 += a[i][i]
    # 격자판 오른쪽 끝부터 왼쪽 아래까지의 대각선 합
    sum2 += a[i][n-i-1]
# 해당 if문을 통해 위에서 계산한 largest와 대각선 2개의 합에서 가장 큰 수를 계산
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)