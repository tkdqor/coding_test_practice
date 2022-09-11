n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)


'''
리스트 인덱스를 가리키는 2개의 변수를 생성한다. lt는 왼쪽, rt는 오른쪽이다.
그리고 요소의 연속 합을 tot라는 변수로 설정한다. 그래서 tot는 lt부터 rt전까지 연속적인 요소의 합이다.
이 tot 값이 m보다 작으면 rt값을 tot에 더해준다. 그리고 rt += 1을 해준다.
그래서 tot 값이 m과 같으면 카운트를 증가시킨다. 그리고 tot에서 lt가 가르키는 값을 빼준다. 그러면서 lt += 1을 해준다.
이걸 반복하면서 계속 밀고가는 것이다. 그런데, tot가 m보다 큰 경우에는 lt값을 빼주고 lt += 1을 해주면 된다.
마지막으로 rt가 리스트 요소 개수인 n이 되었을 때 break
'''