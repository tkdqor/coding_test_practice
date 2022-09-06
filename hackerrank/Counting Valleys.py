# https://www.hackerrank.com/challenges/counting-valleys/problem
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


'''
해수면 위로 올라가면 산을 올라가는 것이고 U라고 하고, 해수면 아래로 내려가면 계곡이고 D라고 한다.
이 때, 계곡의 개수를 리턴하는 함수를 작성.
그래서 해수면을 level로 정하고 U와 D를 해시로 정의해주었다. 그리고, 하나씩 빼면서 U이면서 level이 0인 경우(즉, level이 계속 마이너스였다가 0이 
되니까 계곡를 1번 갔다온 것)에는 count를 증가시켜 주었다.
'''