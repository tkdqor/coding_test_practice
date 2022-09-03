n = int(input())
res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + (a * 1000)
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c * 100
    if money > res:
        res = money

print(res)

'''
가장 큰 조건을 if문에 입력하고, 그 다음 조건을 elif에 입력해야 된다. 
3개의 눈이 같은 조건을 나중에 입력하면 3개가 같더라도 다른 조건이 충족되서 if문이 종료되면 안 된다.
같은 눈이 2개인 경우는, a == b or a == c 까지만 입력해야 a라는 변수로 money식을 만들 수 있다. b == c는 따로 조건을 만들어야 한다.
같은 눈이 없는 경우는, 가장 큰 눈에 * 100이니까 이미 오름차순 정렬을 했으니 c가 가장 큰 눈이 된다.
'''