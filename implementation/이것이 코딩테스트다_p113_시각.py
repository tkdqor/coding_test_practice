h = int(input())
count = 0

for i in range(h + 1):         # 입력받은 시간에서 +1 해줘야 모든 시간을 선택할 수 있음
    for j in range(60):        # 0~59분을 1개씩 빼주기
        for k in range(60):    # 0~59초를 1개씩 빼주기
            if '3' in str(i) + str(j) + str(k):  # 뺀 모든 숫자들을 문자열로 만들고 3이 있는지 체크 / 있다면 count += 1 해주기
                count += 1

print(count)

