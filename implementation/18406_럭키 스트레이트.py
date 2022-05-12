N = list(map(int, str(input())))   # 캐릭터 점수 N을 받아서 리스트로 만들기
standard = int(len(N) // 2)        # 리스트 개수를 2로 나눈 수 구하기 / 리스트에서 해당 수 인덱스까지가 왼쪽 부분
left = 0
right = 0

for i in N[0:standard]:            # 왼쪽 부분 자릿수 합 구하기
    left += i

for i in N[standard:]:             # 오른쪽 부분 자릿수 합 구하기
    right += i

if left == right:                 
    print("LUCKY")
else:
    print("READY")







