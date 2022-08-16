# https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    answer = len(nums) // 2
    c = len(set(nums))
    if c < answer:
        answer = c
    
    return answer


# 해시로 풀어본 나의 풀이
def solution(nums):
    hash_map = {}
    for num in nums:
        # 해시 키에 없다면 새로 추가하는 것으로 중복 제거
        if num not in hash_map:
            hash_map[num] = 1       
    
    if len(nums)//2 >= len(hash_map):
        result = len(hash_map)
    else:
        result = len(nums)//2
    
    return result


# 리스트에 요소의 종류가 다양할 때, 중복을 제거하기 위해 해시를 사용할 생각을 할 수 있다.