def countingValleys(steps, path):
    # Write your code here
    level = 0
    count = 0
    hash_map ={'U': 1, 'D': -1}
    for x in path:
        if x == 'U':
            level += hash_map[x]
        else:
            level += hash_map[x]
        if x == 'U' and level == 0:
            count += 1
    return count

print(countingValleys(8, 'UDDDUDUU'))