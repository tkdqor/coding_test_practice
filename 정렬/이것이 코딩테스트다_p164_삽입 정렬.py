array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # 배열의 두번째 원소부터 시작
    for j in range(i, 0, -1):   # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽과 비교해서 왼쪽이 더 크면 
            array[j], array[j - 1] = array[j - 1], array[j]  # 서로 위치를 바꿔주기
        else:
            break  # 그러다가 자기보다 작은 데이터가 왼쪽에 있으면 그 위치에서 멈추기
    
print(array)

