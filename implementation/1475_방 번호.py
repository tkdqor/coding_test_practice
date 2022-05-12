N = list(map(int, str(input())))        # 방 번호 리스트로 만들기
set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    # 한 세트 나열
count = 0


while N != ['O'] * len(N):              # N 리스트가 문자열 O으로 채워지지 않을 동안 반복
    for i in range(0, len(N)):          # N 리스트 개수만큼 인덱스 뽑기
            if N[i] in set:             # N 리스트 데이터가 set에 있다면
                set.remove(N[i])        # 해당 데이터를 set에서 제거
                N[i] = 'O'              # 해당 데이터를 N 리스트에서 문자열 O으로 바꾸기
            
            if N[i] == 6:               # 만약 6이라면 9로 바꿔서 다시 검토
                N[i] = 9
                if N[i] in set:
                    set.remove(N[i])
                    N[i] = 'O'
            elif N[i] == 9:             # 만약 9라면 6으로 바꿔서 다시 검토
                N[i] = 6
                if N[i] in set:
                    set.remove(N[i])
                    N[i] = 'O'


    if N != ['O'] * len(N):             # 아직 N 리스트가 문자열 O으로 채워지지 않았다면 
        count += 1                      # 세트 개수 추가
        set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 한 세트 다시 구입
    
    if N == ['O'] * len(N):             # N 리스트가 문자열 O으로 다 채워졌다면
        count += 1                      # 세트 개수 추가하고 while문 끝

print(count)