# https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations = sorted(citations)
    l = len(citations)

    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

print(solution([3, 0, 6, 1, 5]))


# citations이 5개의 요소가 있다면,
# H-Index를 5부터 1씩 줄여가면서 확인한다. H-Index번 이상 인용된 논문이 H-Index편 이상인지? => 이 조건이 만족하면 바로 return 하는 것
# 정렬을 한 이유가 있다. 총 5개에서 인덱스가 2인 데이터를 확인한다면 -> 5-2면 인덱스 2인 데이터 포함해서 뒤에 있는 데이터 개수인 3이 된다.
# 즉, l-i값 이상만큼 해당 논문이 인용되어야 하고 &(동시에) l-i개의 데이터 개수 이상만큼 해당 데이터 포함 다른 논문의 개수가 있어야 한다는 조건을 
# 확인하는 것이다.