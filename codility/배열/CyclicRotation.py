# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    index_list = []
    result = [0] * len(A)

    for i in range(len(A)):
        index_list.append(i)

    for i in range(len(index_list)):
        index_list[i] += K
        if index_list[i] > len(index_list) - 1:
            index_list[i] = index_list[i] % len(index_list)

    for i in range(len(index_list)):
        result[i] = A[index_list.index(i)]

    return result


###### 아래 방법이 더 좋은 점수를 받은 방법 ######
def solution(A, K):
    # write your code in Python 3.6
    hash_map = {}
    result = [0] * len(A)

    for idx, i in enumerate(A):
        hash_map[idx+K] = i
    
    for key in hash_map.keys():
        index = key % len(A)
        result[index] = hash_map[key]
    return result


print(solution([3, 8, 9, 7, 6], 3))