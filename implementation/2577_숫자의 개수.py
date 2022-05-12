a = int(input()) # 3개의 자연수 차례대로 받기
b = int(input())
c = int(input())

result = list(map(int, str(a * b * c))) # 3개의 자연수를 모두 곱한 수를 리스트로 만들기

for i in range(0, 10):                  # 0부터 9까지 차례대로 뽑아서
    print(result.count(i))              # result 리스트에 해당 데이터가 몇 개가 있는지 출력하기


