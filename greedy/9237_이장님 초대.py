# 1일 = 묘목을 구입, 묘목 전부를 심음
# 2일 = 묘목 전부가 심어짐
# 하루에 1개만 심는걸까?

# counts = int(input())
# data = list(map(int, input().split()))
# data.sort(reverse=True)
# invite = []

# for day in data:
#     invite.append(day + 3)

# print(max(invite))

###################### 실패한 풀이.. #######################


### 블로그 답안

n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)            # 시간이 오래 걸리는 모묙부터 심어야 하니까 리스트를 내림차순으로 정렬

for i in range(n):
    t[i] = (i+1) + t[i] + 1     # t[i] = 나무 심는 순서 + 나무 다 자라는데 걸리는 시간 + 나무 다 자란 다음날이니까 1

print(max(t))


