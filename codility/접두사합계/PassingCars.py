# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

def solution(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 0 :
            for j in range(i,len(A)):
                if A[j] == 1:
                    count +=1
    if count > 1000000000:
        count = -1
    return count

print(solution([0,1,0,1,1]))

# 배열에는 0 또는 1만 포함 - 0은 동쪽으로 여행하는 자동차를 나타내고, 1은 서쪽으로 여행하는 자동차를 나타낸다
# 문제 결과로는 동쪽으로 향해가는 차들이 서쪽으로 가는 차량을 몇 번 마주치게 되는지 총합을 출력
# A = [0,1,0,1,1]가 주어지면 지나가는 차가 총 (0, 1), (0, 3), (0, 4), (2, 3), (2, 4) 이렇게 5대로 5를 반환
# ex) (0,3)은 0인덱스랑 3인덱스를 의미
# 그리고 출력할 값이 1000000000보다 크면 -1을 출력

# 위의 코드는, A 리스트에서 차례대로 요소를 뽑아서 0이라면 해당 인덱스부터 숫자를 뽑아서 1이 되는 요소를 for문으로 개수를 세고 출력한다.