# def solution(sizes):
#     raw = 0
#     column = 0
#     for x in sizes:
#         if x[0] > raw:
#             raw = x[0]
#         if x[1] > column:
#             column = x[1]
#     result = raw * column

#     return result

def solution(sizes):
    raw = []
    column = []
    for x in sizes:
        raw.append(x[0])
        column.append(x[1])
    result = max(raw) * max(column)
    
    # for i in range(len(raw)):
    #     raw[i], column[i] = column[i], raw[i]
    #     change = max(raw) * max(column)
    #     if change < result:
    #         result = change
    #         raw[i], column[i] = column[i], raw[i]
    #     else:
    #         raw[i], column[i] = column[i], raw[i]
    
    # return result

    # while True:
    #     index = raw.index(max(column))
    #     raw[index], column[index] = column[index], raw[index]
    #     if raw[index] < max(raw) and column[index] < max(column):
    #         continue
    hash_map = {}
    column_max = 0
    for idx, y in enumerate(column):
        hash_map[y] = raw[idx]
    
    while True:
        for key in hash_map.keys():
            if key > column_max:
                column_max = key
        if column[column.index(column_max)] < max(raw) and raw[raw.index(hash_map[column_max])] < max(column):
            raw[raw.index(hash_map[column_max])], column[column.index(column_max)] = column[column.index(column_max)], raw[raw.index(hash_map[column_max])]
            key = 0
            continue
        else:
            column[column.index(column_max)], raw[raw.index(hash_map[column_max])] = raw[raw.index(hash_map[column_max])], column[column.index(column_max)]
            break
    return result
        

#### 해보려고 했던 게,, raw, column 각각 리스트로 만든 다음에 세로길이에서 가장 큰 길이를 선택해서 가로 길이랑 바꾼다음,
# 바꾼 세로 길이가 기존 세로길이 max보다 작고 / 바꾼 가로 길이가 기존 가로길이 max보다 작으면 그대로 바꾼채로 둔다..
# 그 다음 큰 세로 길이를 선택해서 반복하고 위의 조건이 맞지 않을 때 그만두기..



print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))