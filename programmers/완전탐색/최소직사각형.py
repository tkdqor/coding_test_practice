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