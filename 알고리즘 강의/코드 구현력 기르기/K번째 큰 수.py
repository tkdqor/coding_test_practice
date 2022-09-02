n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])
print(res)


# 입력예제
# 10 3
# 13 15 34 23 45 65 33 11 26 42

# 출력예제
# 143

# N개의 카드에서 카드들을 내림차순하기 - 그렇게 내림차순된 리스트에서 3장을 뽑아 더한 수들을 리스트로 만들고 - 그 리스트에서 K번째로 큰 수 출력

'''
3중 for문으로 n개의 수에서 3가지 수를 뽑기 / 즉, 중복을 방지하고 서로 다른 3가지 수를 뽑기 위해 이렇게 진행한다. => 이렇게 3중 for문은 조합의 개념으로 순서 관계없이 뽑게 해준다.
set() 자료구조에서는 요소를 추가할 때 append가 아니라 add를 사용한다.
set()이라는 자료구조는 sort() 기능이 없다. 그래서 다시 list화 해야된다.
'''