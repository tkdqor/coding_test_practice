n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

# def digit_sum(x):
#     sum = 0
#     for i  in str(x):
#         sum += int(i)
#     return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)


'''
tot라는 변수에 각 자릿수를 더해 합을 만들어주는 함수인 digit_sum을 이용해서 합을 구하기.
digit_sum이라는 함수에는 어떤 숫자 x가 입력되었을 때, x를 10으로 나눈 나머지를 계속 더해준다. 그리고 그 x는 10으로 나눈 몫으로 바꾼다. 
이렇게 하면 숫자 x의 각 자릿수를 더한 값을 구할 수 있다.
digit_sum 함수를 어떤 숫자를 문자열로 전환해서 하는 방법도 있다. 특정 숫자를 문자열화하고 한 자릿씩 뽑은 다음, 다시 정수화해서 더해주는 것이다.
max을 -21억으로 잡는 것은, C++로 생각하면 정수형은 4byte이면 2의 31제곱 숫자까지만 저장된다. 즉, 음수쪽으로 2의 31제곱, 양수쪽으로 2의 31제곱 -1 (0이라는 숫자가 있으니까)
그래서, 2의 31제곱이 바로 21억 4천 7백만 이라는 숫자와 비슷하다.
'''