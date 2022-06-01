array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 퀵 정렬 함수가 한 번 실행되면 -> 큰 데이터와 작은 데이터를 찾아 서로 교체하는 것 까지 수행할 수 있도록 설정
def quick_sort(array, start, end): 
    if start >= end: # 원소가 1개인 경우 종료
        return 
    pivot = start # 피벗은 첫 번째 원소 인덱스로 설정
    left = start + 1 # 피벗 제외 데이터에서 왼쪽 인덱스는 피벗 바로 다음 번호로 설정
    right = end      # 피벗 제외 데이터에서 오른쪽 인덱스는 데이터에서 맨 오른쪽 번호로 설정

    # 여기서 pivot / start / end는 바뀌지 않는다!
    
    while left <= right: # 왼쪽과 오른쪽 인덱스가 서로 엇갈리지 않을 동안만 반복
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]: # left 인덱스가 데이터 끝 인덱스보다 작거나 같고 / 피벗보다 작거나 같으면 안되니까 계속 반복
            left += 1                                      # left 인덱스를 오른쪽로 옮기기
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]: # right 인덱스가 데이터 처음 인덱스보다 크고 / 피벗보다 크거나 같으면 안되니까 계속 반복
            right -= 1                                        # right 인덱스를 왼쪽으로 옮기기
        
        if left > right: # 왼쪽 인덱스가 오른쪽 인덱스보다 크다면(즉, 서로 엇갈렸다면) -> 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:            # 서로 엇갈리지 않았다면 -> 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 왼쪽과 오른쪽 인덱스가 서로 엇갈린 상황이라면 -> while문이 종료되고 분할되었다는 의미
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1) # 이 때는 right가 피벗을 의미하니까 -> start부터 피벗 - 1 인덱스까지 정렬 수행
    quick_sort(array, right + 1, end)   # 이 때는 right가 피벗을 의미하니까 -> 피벗 + 1 인덱스부터 end까지 정렬 수행

quick_sort(array, 0, len(array) - 1)
print(array)

