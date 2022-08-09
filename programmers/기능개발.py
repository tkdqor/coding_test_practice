# https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    # 하루를 time으로 표현 / time = 7이면 7일이 경과
    time = 0
    # 완료된 작업 count하기
    count = 0
    while len(progresses)> 0:
        # 100% 작업이 완료되면
        if (progresses[0] + time*speeds[0]) >= 100:
            # 완료된 해당 작업을 progresses 리스트에서 빼기
            progresses.pop(0)
            # speeds에서도 빼기
            speeds.pop(0)
            count += 1
        # 작업이 완료되지 않았다면
        else:
            # 그 때까지 완성된 작업 개수를 answer 리스트에 추가하고 count 리셋하기
            if count > 0:
                answer.append(count)
                count = 0
            # 작업된 개수가 없다면 time 올려주기
            time += 1
    answer.append(count)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))