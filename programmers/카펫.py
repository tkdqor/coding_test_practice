# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    # 카펫 가로 * 세로 = 갈색 격자 개수 + 노란색 격자 개수
    nm = brown + yellow
    # 가로를 의미하는 n를 구하는 과정 시작
    # nm이 12라면, n이 1부터 12까지 나올 수 있다. 가로12 * 세로1도 가능
    for n in range(1, nm+1):
        # nm을 n으로 나눴을 때 나머지가 있다면 그 수는 가로가 될 수 없다.
        if nm%n != 0:
            continue
        # nm을 n으로 나눴을 때 딱 떨어진다면 해당 몫을 m으로 지정 / 즉, 세로가 된다
        m = nm//n
        # 카펫의 가로에서 2를 뺀 값과 세로에서 2를 뺸 값을 곱하면 노란색 격자 개수가 되는지 확인
        if (n-2)*(m-2) == yellow:
            return sorted([n, m], reverse = True)

print(solution(10, 2))