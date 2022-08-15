# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []
    
    # pattern마다 순환주기가 다르니까 각각 순환주기로 나눠주기
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1
    
    # score 리스트 중 가장 큰 값이라면 인덱스가 0,1,2이니까 
    # +1를 해야 return을 1,2,3으로 할 수 있다.
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    
    return result


print(solution([1,2,3,4,5]))