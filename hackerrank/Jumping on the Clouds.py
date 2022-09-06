# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_r=internal-search&isFullScreen=false
def jumpingOnClouds(c):
    # Write your code here
    jump = 0
    position = 0
    while c:
        try:
            if c[position] == 0:
                if c[position + 2] == 0:
                    position += 2
                    jump += 1
                elif c[position + 1] == 0:
                    position += 1
                    jump += 1
            if position == len(c)-1:
                return jump
        except:
            break
    position += 1
    jump += 1
    return jump

print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))


'''
0이면 적운이고 1이면 뇌우를 나타내는 구름 배열을 준다. 
플레이어는 현재 위치에서 1 또는 2를 더한 것과 같은 숫자를 가진 적운 구름 위치로 이동할 수 있다.
플레이어는 1번인 뇌우를 피해야 한다. 시작 위치에서 마지막 구름으로 도착하는 데 필요한 최소 점프 횟수를 리턴해야한다.
그래서, 점프 횟수를 나타내는 jump와 현재 위치를 나타내는 position 변수를 설정한다.
반복문으로 position에 해당하는 구름이 0이면, +2한 위치가 0일 때 해당 위치로 이동시키고 점프 횟수도 추가한다.
만약 +2 위치가 1이면 +1 위치로 변경한다.
최종적으로 계속 위치를 옮기다가 position이 마지막 인덱스에 위치할 때의 jump 횟수를 리턴한다.

+2한 위치가 리스트 인덱스에 없는 경우를 위해 -> try - except로 예외처리를 진행한다.
인덱스가 없는 경우에는 while문을 종료시키고 position을 1 증가 시키고 jump도 1 증가 시킨다.
'''