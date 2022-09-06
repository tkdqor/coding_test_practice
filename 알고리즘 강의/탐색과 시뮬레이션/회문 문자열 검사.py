# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     size = len(s)
#     for j in range(size//2):
#         if s[j] != s[-1-j]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))


# # 다른 방법
# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     if s == s[::-1]:
#         print("#%d YES" %(i+1))
#     else:
#         print("#%d NO" %(i+1))


'''
문자열 비교 시, 대소문자를 구별하지 않으니까 받은 문자열을 다 대문자로 바꾸기.
그리고 문자열의 길이를 의미하는 변수를 저장한다.
그 다음, 만약 level이라는 문자열이라고 한다면 level 순서대로 0부터 4번 인덱스가 된다. 이 때, level의 길이는 5이고 5 // 2를 하면 2가 된다.
그러면 0번과 4번, 1번과 3번 인덱스 비교를 2번하면 된다.
즉, 위 예시에서는 for j in range(size//2): 이렇게 for문으로 0번 인덱스와 4번 인덱스가 맞는지 비교해야 한다.
파이썬 리스트는 인덱스를 거꾸로 생각할 수도 있다. 리스트의 요소가 5개라면, 뒤에서부터 -1, -2, -3, -4, -5가 된다.
그래서, for문으로 s[j] != s[-1-j] 이렇게 처음과 끝을 비교할 수 있다.
'''