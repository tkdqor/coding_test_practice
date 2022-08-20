# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

def solution(X, A):
    # write your code in Python 3.6
    B=[]
    count=0
    # A의 요소를 1개씩 빼고
    for i in A :
        # 만약 그 요소가 B 리스트 안에 있다면
        if i in B:
            # index인 count 1 증가 시키기
            count +=1
        # 만약 그 요소가 B 리스트 안에 없다면
        else:
            # 그 요소를 B 리스트안에 넣어주기 / 즉, B 리스트는 중복없이 A의 요소들이 담겨져 있게 된다
            B.append(i)
            # 만약 B 리스트 요소의 합과 1부터 주어진 X까지의 합이 같다면 => 나뭇잎 위치를 찾은거니까 인덱스인 count 반환(X가 A리스트에서 가장 큰 수)
            if sum(B) == sum(range(1,X+1)):
                return count
            # 합이 같지 않다면 index인 count 1 증가 시키기
            count +=1
    # 나뭇잎 위치를 못 찾으면 -1 반환
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

# 개구리가 강 건너편으로 넘어가고 싶어함 / 위치 0 -> X+1
# 나뭇잎은 나무에서 강 표면으로 떨어진다
# 떨어지는 잎을 나타내는 N개의 정수로 구성된 배열 A가 주어짐
# A[K]는 초 단위로 측정된 시간 K에서 한 잎이 떨어지는 위치를 의미
# 목표는 개구리가 강의 반대편으로 점프할 수 있는 가장 빠른 시간을 찾는 것
# 개구리는 강을 가로질러 1부터 X까지의 모든 위치에 나뭇잎이 나타날 때만 횡단할 수 있음
# X = 5, A = [1,3,1,4,2,3,5,4]가 주어지면 / A[6] = 5이니까 6초에 5라는 위치에 나뭇잎이 가장 먼저 빠르게 나타난다. 그래서 6를 반환하면 된다.
# 개구리가 반대편으로 갈 수 없는 경우 -1을 반환


# A의 값을 하나씩 i로 받아서 해당 원소가 B에 있으면 index만 증가, 해당 원소가 없으면 합을 비교해서 count값 출력