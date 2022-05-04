def recursive_function():        # 함수를 정의할 때,
    print('재귀 함수를 호출합니다.')   # print를 하고나서
    recursive_function()         # 자기 자신을 또 호출

recursive_function()             # 함수를 한 번 호출하면, 계속 호출이 되는 구조