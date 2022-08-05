# 두 사람이 서로 무게가 다른 볼링공을 고르려고 한다
# 이미 고른 케이스는 제외하기
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 볼링공 무게를 담을 수 있는 리스트 - 볼링공 무게가 1부터 10까지만 존재할 수 있다고 명시되어있음
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트 증가시키기
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리 - m은 공의 최대 무게를 의미
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기 - 무게가 i인 공의 개수 * B가 선택하는 경우의 수

print(result)

