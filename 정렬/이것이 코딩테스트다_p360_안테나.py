n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값(median)을 출력하기 - 배열의 마지막 인덱스를 2로 나눈 몫이 인덱스가 되게하기
print(data[(n - 1) // 2])
