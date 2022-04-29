# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
# 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주.

# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 해당 법칙에 따른 결과를 출력.
# 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며 각 자연수는 공백으로 구분
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분하고 1이상 10,000 이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.


######################### 첫번째 풀이 #########################

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 입력받은 수들 오름차순 정렬
first = data[N - 1] # 가장 큰 수
second = data[N - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(K):    # 가장 큰 수를 K번 더하기
        if M == 0:        # M이 0이면 반복문 탈출
            break
        result += first
        M -= 1            # result에 더할 때마다 M에서 1씩 빼기
    if M == 0:            # M이 0이면 반복문 탈출
        break
    result += second      # 두 번째로 큰 수를 한 번 더하기
    M -= 1                # result에 더할 때마다 M에서 1씩 빼기

print(result)


######################### 두번째 풀이 #########################

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m // (k + 1)) * k   # 가장 큰 수가 더해지는 횟수 계산
                                # (반복되는 배열이 K+1이고, m으로 나누면 배열이 반복되는 횟수가 나오고 여기에 k를 곱하면 -> 가장 큰 수가 반복되는 횟수가 나온다)
count += m % (k + 1)            # 반복되는 배열 이외의 남는 횟수 더하기

result = 0
result += (count) * first       # 첫번째 수를 다 더한 결과
result += (m - count) * second  # 두번째 수를 다 더한 결과

print(result)

