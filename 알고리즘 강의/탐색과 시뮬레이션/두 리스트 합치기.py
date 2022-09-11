n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1=p2=0
c = []
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]

print(c)


'''
sort() 함수를 사용하면 nlogn의 시간복잡도를 가지지만, while, for문으로 n번만으로 답을 낼 수 있게끔 하는 것이 시간복잡도 상으로 더 좋다.
포인트 변수를 사용. P1은 a 리스트의 0번 인덱스를 가리키고, P2는 b 리스트의 0번 인덱스를 가리킨다. P1 = 0, P2 = 0
그래서 if a[P1] <= b[P2] 이면 a[P1]의 값을 c라는 리스트에 append시키는 것이다. 그리고나서 P1은 1이 된다. P1 = 1
즉, 작은 것을 먼저 집어넣는다. 그래서 계속 if문으로 비교하는 것이다.
그리고 P1이나 P2가 리스트의 개수 인덱스를 초과했을 때는, 아직 도달하지 않은 리스트의 남은 요소들을 그대로 c 리스트에 추가해주면 된다.

while문 조건이 헷갈린다면, 반대로 생각했을때가 while문이 종료되는 조건이다.
ex) while p1 < n and p2 < m: 이면 -> p1이 n과 같거나 커지는 경우 또는 p2가 m과 같거나 커지는 경우, while문 종료
'''