# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse=True), 0
    while True:
        for i, priority in enumerate(priorities):
            s = search[c]
            if priority == s:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))

# 여기서 search는 항상 내림차순되어 제일 중요도가 높은 우선순위가 앞에 있게한 용도
# s는 찾으려는 우선순위
# search가 내림차순 정렬을 했기 때문에 for문을 돌면서 가장 중요도가 높은순으로 우선순위를 찾으면 -> c와 answer가 1씩 증가
# answer는 몇번째로 인쇄되는지를 의미하니까 가장 높은 우선순위를 찾으면 +1씩 증가시키는 것
# c는 search의 인덱스를 의미하니까 가장 높은 중요도 우선순위를 찾을때마다 다음 우선순위를 찾기위해 +1씩 증가시키는 것
# if i == location: 조건을 충족해 break되면 for문이 종료되고 while문에 속해있으니 또 break를 해줘야 while문에서 나올 수 있다