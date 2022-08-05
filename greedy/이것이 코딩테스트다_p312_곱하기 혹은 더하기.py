data = input()

# 첫번째 문자를 숫자로 변경하여 대입 - 즉, 첫번째 문자부터 더한 상태로 시작
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

