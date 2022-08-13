def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            # hash_map에서 접두사가 될 수 있는 key를 찾고 phone_number 자기자신은 제외해야 되니 temp != phone_number 조건 붙이기
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

print(solution(["12","123","1235","567","88"]))