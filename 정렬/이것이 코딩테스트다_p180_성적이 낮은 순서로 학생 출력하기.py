N = int(input())


# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(N):
    input_data = input().split()
    # 이름은 문자열 형태 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')



# input_data = input().split() 해당 코드는 input_data = ['홍길동', '95'] 이렇게 해준다
# 람다함수는 일반함수를 가볍게 만든 함수
# ex) 인자로 들어온 값에 2를 곱해서 반환하는 경우는, -> lambda x: x * 2