n, m = map(int, input().split())  # 행의 개수와 열의 개수 받기

result = [] 

for _ in range(n):                          # 행의 개수만큼 for문으로
    data = list(map(int, input().split()))  # 숫자들을 받아서 리스트로 만들기
    result.append(min(data))                # 그 리스트 중에 가장 작은 수를 result 리스트에 추가하기

print(max(result))                          # result 리스트에서 가장 큰 값 출력
