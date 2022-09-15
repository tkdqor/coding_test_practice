# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col


print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))


sizes = [1,2,3,4,5]
for i in range(len(sizes)-1):
    print(sizes[i])