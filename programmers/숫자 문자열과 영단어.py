def solution(s):
    # 숫자만 담은 numbers 리스트와 영단어와 숫자가 대응되는 change 해시 정의
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    change = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    # 영단어를 확인할 temp 변수와 최종 숫자를 의미하는 result 변수 정의
    temp = ""
    result = ""
    # 문자열 s에서 하나씩 빼서 temp에 넣고 temp가 numbers에 있는지, change에 있는지 확인 후,
    # result에 추가하기
    for x in s:
        temp += x
        if temp in numbers:
            result += temp
            temp = ""
        if temp in change:
            result += str(change[temp])
            temp = ""
    return int(result)