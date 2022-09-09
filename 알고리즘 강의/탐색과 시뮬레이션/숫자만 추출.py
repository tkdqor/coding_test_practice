s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = (res * 10) + int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)


'''
isdecimal 함수는 0부터 9까지를 찾아주는 함수이고, isdigit 함수는 알파벳이 아닌 숫자를 전부 찾아주는 함수이다. 2의 2승도 인식한다.
그리고 리스트 요소 하나씩 뽑아서 숫자가 맞다면 res = (res * 10) + int(x) 해당 식으로 정수를 만들어준다. 
이렇게 하면 첫의 자리의 0을 자동으로 무시할 수 있다.
'''
