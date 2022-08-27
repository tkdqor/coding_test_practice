arr = [5,3,7,9,2,5,2,6]
# arrMin = float('inf')
# for i in range(len(arr)):
#     if arr[i] < arrMin:
#         arrMin = arr[i]

arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]


print(arrMin) 


'''
arrMin이라는 변수를 하나 지정하고 여기에 최종적으로 arr이라는 리스트 원소중에서 가장 작은 값이 기록되도록 코드를 구현해보자.
arrMin = float('inf') 이렇게 하면 python에서 가장 큰 무한대 값을 의미
또는 arrMin = arr[0] 이렇게 주어진 리스트의 처음 인덱스로 설정해놓고 for문에서 range를 1부터 적용해도 된다.
'''