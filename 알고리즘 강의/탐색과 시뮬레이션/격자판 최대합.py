n = int(input())
result = []
raw = 0
column = 0
col = 0
cross = 0
cross2 = 0

for x in range(n):
    a = list(map(int, input().split()))
    result.append(a)

for i in result:
    if sum(i) > raw:
        raw = sum(i)

for j in range(n):
    for k in range(n):
        col += result[k][j]
    if col > column:
        column = col
        col = 0
    else:
        col = 0

for m in range(n):
    cross += result[m][m]

for z in range(n-1, -1, -1):
    cross2 += result[abs(z-4)][z]

print(max(raw, column, cross, cross2))

