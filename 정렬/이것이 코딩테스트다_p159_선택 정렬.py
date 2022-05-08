array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):             # 맨 앞에 있는 데이터부터 뽑기
    min_index = i                       # 가장 작은 원소의 인덱스 
    for j in range(i + 1, len(array)):  # 남은 원소에서 하나씩 뽑아서 min_index와 비교하기 / 더 작으면 그게 min_index가 된다.
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]   # 맨 앞자리부터 작은수를 서로 스와프

print(array)
