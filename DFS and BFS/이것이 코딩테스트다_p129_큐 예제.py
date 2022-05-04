from collections import deque
# 큐 구현을 위해 collections 모듈의 deque(데크) 라이브러리 사용

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 데이터에서 가장 왼쪽 데이터를 꺼내기
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력


# 관련 자료
# https://scribblinganything.tistory.com/31
# https://excelsior-cjh.tistory.com/96
