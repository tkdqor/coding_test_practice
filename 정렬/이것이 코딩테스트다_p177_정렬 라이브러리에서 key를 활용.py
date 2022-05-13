array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

# [('바나나', 2), ('당근', 3), ('사과', 5)]
# sorted 메소드에서는 key를 기준으로 정렬할 수 있다