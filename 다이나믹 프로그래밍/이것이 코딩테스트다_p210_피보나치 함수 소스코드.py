# 피보나치 함수(Fibonacci Function)를 재귀 함수로 바꿔서 표현
def fibo(x):
    if x == 1 or x == 2:  # 피보나치 수 1과 2는 항상 1이기 때문에 1를 return 해주기
        return 1
    return fibo(x - 1) + fibo(x - 2) # 피보나치 점화식 코드

print(fibo(4)) # 4번째 피보나치 수를 구하기
