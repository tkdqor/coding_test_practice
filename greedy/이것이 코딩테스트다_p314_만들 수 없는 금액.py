n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료 - 타켓보다 큰 수라면 타켓전까지 계속 만들 수 있다가 못 만들게 된다
    if target < x:
        break
    # 타켓보다 같거나 작은 수라면 기존 타켓에 해당 수를 더해준다 - 그러면 못 만드는 경우가 없게 된다
    target += x

# 만들 수 없는 금액 출력
print(target)
