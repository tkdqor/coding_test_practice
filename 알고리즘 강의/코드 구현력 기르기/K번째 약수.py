N, K = map(int, input().split())
count = 0

for i in range(1, N+1):
    if N%i == 0:
        count += 1
    if count == K:
        print(i)
        break
else:
    print(-1)


# 입력예제
# 6 3

# 출력예제
# 3


"""
1부터 N까지의 약수를 구하고 그 중에서 특정 순서의 약수를 구할 때는 count = 0 생각하기
"""