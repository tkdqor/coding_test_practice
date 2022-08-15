# https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    # 리스트 요소를 문자열로 바꾸고 리스트로 설정
    input_list = list(map(str, numbers))
    
    # sort함수의 key 매개변수를 사용해서 정렬 기준 설정
    # 문자열의 길이를 3배로 늘려서 비교
    input_list.sort(key = lambda x:x*3, reverse=True)
    answer = ''
    answer = answer.join(input_list)
    # 마지막으로 answer를 int로 바꾸고 str로 바꾸는 이유는 "0000"과 같은 케이스를 0으로 바꾸고 문자열로 출력하기 위함이다.
    return str(int(answer))

print(solution([3, 30, 34, 5, 9]))