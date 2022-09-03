n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0

for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)

'''
sum이라는 변수로 총 점수를 계산하고, cnt라는 변수로 가산점(가중치)을 계산한다.
그래서 특정 숫자가 1이 맞다면 cnt를 1 증가시키고 그 cnt를 sum에 더해주는 것이다. 따라서 연속적으로 1이 나온다면, cnt가 계속 증가해서 가산점을 계산하게 된다.
만약 1이 나오는 게 끝나면, 다시 cnt 변수를 0으로 리셋한다.
'''