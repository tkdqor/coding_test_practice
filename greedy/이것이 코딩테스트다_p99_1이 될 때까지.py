n, k = map(int, input().split())
count1 = 0
count2 = 0

while n >= k:           # while의 조건을 구체적으로 주어야 한다! / n이 k 이상이라면 계속 k로 나누기
    while n % k != 0:   # n을 k로 나눈 나머지가 0이 아닌 경우 n에서 1을 빼기
        n -= 1
        count1 += 1     # 1번 방법의 횟수 증가
    n //= k             # 나머지가 0인 경우 n을 k로 나누고 2번 방법의 횟수 증가
    count2 += 1

while n > 1:             # n이 k보다 작을 경우를 의미
    n -= 1               # 1번 방법의 횟수 증가
    count1 += 1


result = min(count1, count2)  # 2개의 방법 중, 작은 횟수의 방법을 result로 설정

if result == 0:               # 만약 result가 0이면 횟수가 존재하는 방법을 출력하게끔 설정
    print(max(count1, count2)) 
else:
    print(min(count1, count2))

