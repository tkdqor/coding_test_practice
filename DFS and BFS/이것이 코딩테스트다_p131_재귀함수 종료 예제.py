def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return

    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    print(i, '번째 재귀 함수를 종료합니다.')
    recursive_function(i + 1)

recursive_function(1)    


# 재귀함수와 스택 자료구조 관련 블로그 
# https://dojang.io/mod/page/view.php?id=1376
