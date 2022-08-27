n = int(input())
a = list(map(int, input().split()))
ave = sum(a)/n
ave += 0.5
ave = int(ave)
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1 
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print(ave, res)


a = 66.6
a += 0.5
print(int(a))


'''
소수첫째자리에서 반올림을 해야되는 경우, 우리가 흔히 알고 있는 반올림은 round_half_up 방식으로 4까지는 내림이고 5부터는 올림을 진행한다.
근데, python에서의 round 함수는 round_half_even 방식을 택하고 있기 때문에 다르다. 
그래서 실수에다가 0.5를 더한 값을 기준으로 확인하면 된다.
소수점 첫째자리가 5이상이면 0.5를 더했을 때 첫째자리가 올라갈 것이고 소수점 첫째자리가 4이하라면 안 올라갈 것이다. 
그 다음, int() 함수를 사용해서 형변환을 하면 소수점이 없어지게 된다.
'''