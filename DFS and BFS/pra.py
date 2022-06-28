input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

result = 0

for step in steps:
    new_row = row + step[0]
    new_column = column + step[1]

    if new_row >= 1 and new_column >= 1 and new_row <= 8 and new_column <= 8:
        result += 1

print(result)
