N = int(input()) # 수열에 속해있는 수의 개수
list = []        # 리스트 만들기

for i in range(N):                  # 수의 개수만큼 반복될때마다
    list.append(int(input()))       # 한 줄씩 입력받는 수를 리스트에 추가

list = sorted(list, reverse=True) # 그 리스트를 sorted를 사용해서 내림차순 정렬

for i in list:                    # 리스트에서 데이터 1개씩 뽑아 출력 
    print(i, end=" ")               # 단, 다음줄로 넘어가지 않게 공백 주기

