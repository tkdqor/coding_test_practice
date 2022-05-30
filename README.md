# 코딩테스트 대비 문제풀이
알고리즘 이름 폴더별로 백준 python 문제 및 코딩테스트 대비 문제 풀이 내용 정리하기  
"이것이 취업을 위한 코딩 테스트다 with 파이썬" 책에 포함된 문제도 정리하기

<br>

## 📌 map(int, input().split())
- input 함수는 입력된 값을 문자열로 인식하게 해준다. 이 때, 입력값을 숫자(정수형)로 인식하기 위해서는 int(input()) 이렇게 해주면 된다.
- split 함수는 한 문자열을 띄어쓰기 기준으로 나눠서 리스트로 구분해준다.
  - 그래서, N = input().split() -> 이렇게 하고 11 12 13 14를 입력하면, 

```terminal
['11', '12', '13', '14']
```

- 이렇게 띄어쓰기 기준으로 각각의 값을 문자열로 리스트로 나눠준다. 또한, A, B = input().split() -> 11 12 입력 시, 이렇게 입력값을 2개 이상으로 구분하면, A -> '11' / B -> '12' 로 구분해준다.
- **A, B = int(input().split()) -> 이렇게 하면 오류가 발생한다. input().split() 까지가 -> 리스트로 반환되고 / int 함수는 리스트를 정수형으로 바꿔줄 수 없기 때문이다.**
  - **이럴 때 map 함수가 필요하다. / map(적용할 함수, 반복 가능한 자료형)**
  - **map 함수를 활용하면 모든 반복가능 자료형 데이터 각각에 함수를 적용시킬 수 있다.**
  - **A, B = map(int, ['232', '2324']) -> 이렇게하면 오류가 나지 않는다.**

- 그래서 최종적으로 ==> map(int, input().split()) 이라는 식을 얻을 수 있는 것이다.
  - 다만, map 함수를 사용하면 input().split() 에서 만들어진 리스트가 사라진다. 
  - 그래서 list(map(int, input().split())) -> 이렇게해야 모든 데이터가 정수인 리스트를 만들어줄 수 있다.

- [참고 블로그](https://ccamppak.tistory.com/38)


<br>

## 📌 그리디 알고리즘
현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미   
기준에 따라 좋은 것을 선택하는 알고리즘으로, 문제에서 **‘가장 큰 순서대로', ‘가장 작은 순서대로'** 와 같은 기준을 알게 모르게 제시해준다

<br>

### ex) 거스름돈 예제
- 우리가 음식점의 계산을 도와주는 점원일 때, 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하기. (단, 거슬러줘야 할 돈 N은 항상 10의 배수)

- 입력 예시
```terminal
1260
```

- 출력 예시
```terminal
6
```

- **답안 예시**
```python
N = int(input())
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += (N // coin) # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  N %= coin

print(count)
```

⇒ 해당 문제는 **‘가장 큰 화폐 단위부터'** 돈을 거슬러 주는 것이 문제를 해결할 수 있는 방법이다. 그래야 최소의 동전 개수로 모두 거슬러 줄 수 있다. 

⇒ 대부분의 그리디 알고리즘 문제에서는, 문제 풀이를 위한 최소한의 아이디어를 떠올리고 **이것이 정당한지 검토를 진행**해야 한다.
  - **해당 문제에서는 잔돈의 큰 단위가 작은 단위의 배수 형태라서 그리디 알고리즘으로 해결이 가능한 것이고, 만약 잔돈의 단위가 서로 배수 형태가 아니라 무작위로 주어진 경우에는 다음과 같은 방법으로 해결할 수 없다.** 
  - 그러한 문제는 “다이나믹 프로그래밍" 방법으로 해결할 수 있다.

<br>

### ex) 전형적인 그리디 알고리즘 예제
- 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙. 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없다. 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
- 배열의 크기가 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 → 해당 법칙에 따른 결과를 출력하기.

- 입력 예시
```terminal
5 8 3
2 4 5 4 6
```

- 출력 예시
```terminal
46
```

- **답안 예시**
```python
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for _ in range(k): # 가장 큰 수를 k번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    
    if m == 0: # m이 0이라면 반복문 탈출
        break

    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)
```

⇒ 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다. 
  - 그래서 **‘가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산’** 을 반복하자.

<br>

## 📌 구현 알고리즘
코딩 데스트에서 구현이란, **'머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정'** 을 의미한다.   
또한, 모든 경우의 수를 다 계산하는 **'완전 탐색'** 문제나 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 **'시뮬레이션'** 문제도 포함된다.

<br>

### ex) 대표적인 예제 1 - 시뮬레이션 유형
- 여행가 A가 N * N 크기의 정사각형 공간 위에 서 있을 때, 가장 왼쪽 위 좌표는 (1,1)이며 가장 오른쪽 아래 좌표는 (N, N)에 해당한다. A는 상,하,좌,우 방향으로 이동할 수 있다. 계획서는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 적혀있다. 순서대로 왼쪽, 오른쪽, 위, 아래로 한 칸씩 이동할 수 있다. 첫째 줄에 공간의 크기를 나타내는 N이 주어지고 둘째 줄에 A가 이동할 계획서 내용이 주어질 때 A가 최종적으로 도착할 지점의 좌표를 공백으로 구분하여 출력하기.

- 입력 예시
```terminal
5
R R R U D D
```

- 출력 예시
```terminal
3 4
```

- **답안 예시**
```python
n = int(input())
x, y = 1, 1                # 시작 위치는 (1, 1)로 고정되어 있으니 x,y로 정해주기
plans = input().split()    # 문자 여러 개가 주어졌을 때, 다음과 같이 입력하면 리스트로 담겨진다

# 리스트 순서대로 L, R, U, D 이동 방향 정의
dx = [0, 0, -1, 1]                   # ex) dx[0]과 dx[0]은 L의 이동방향을 정의한 것
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']


for plan in plans:                              # 문자 1개씩 출력 시, 
    for i in range(len(move_types)):            # 0부터 3까지 뽑아서 
        if plan == move_types[i]:               # 문자가 서로 같으면, x,y값을 이동시키기
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:    # x와 y가 1보다 작으면 안되고 / x와 y가 n보다 크면 안됨
        continue                                # continue는 아래 코드를 실행하지 않고 건너뛰는 것을 의미
    x, y = nx, ny                               # 문자 1개씩 출력해서 바뀐 x,y 대입

print(x, y)
```
⇒ 해당 문제는 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로 분류된다.
  - **계획서로 나올 수 있는 문자들을 리스트로 정의해놓고, 각 문자마다 해당될 수 있는 좌표 x,y도 리스트로 미리 정의해두는 문제이다.**

<br>

### ex) 대표적인 예제 2 - 시뮬레이션 유형
- 첫째 줄에 8 * 8 좌표 평면 상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다. 이 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 만들기. 나이트는 1) 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동 / 2) 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동 이렇게 2가지 경우로 이동할 수 있다.

- 입력 예시
```terminal
a1
```

- 출력 예시
```terminal
2
```

- **답안 예시**
```python
input_data = input()
row = int(input_data[1])                              # 문자열도 슬라이싱이 가능하니까 열과 행을 따로 받기
column = int(ord(input_data[0])) - int(ord('a')) + 1  # ord 함수는 문자의 유니코드 값을 돌려주는 함수 / a는 97이므로 받은 문자 유니코드 - a의 유니코드 +1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 나이트가 이동할 수 있는 8가지 방향 정의

result = 0

for step in steps:                   # 방향 1가지를 빼서
    next_row = row + step[0]         # row에 더하고
    next_column = column + step[1]   # column에도 더하기
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:  # 그 결과가 8 X 8 좌표 평면을 벗어나지 않는 경우, +1
        result += 1

print(result)
```
⇒ **이번에는 위의 문제와 다르게 steps 변수에 dx와 dy 변수의 기능을 합쳐서 리스트안에 튜플로 정의.**
  - 나이트가 움직일 수 있는 모든 이동 경로를 steps 변수에 정의하고 반복문으로 현재 위치에서 움직이고 8 * 8 좌표에서 벗어나지 않으면 경우의 수로 확인.
  - **ord() 함수는 문자를 유니코드 값으로 돌려준다. 대표적으로 a는 97이다.**


<br>

### ex) 대표적인 예제 3 - 완전 탐색 유형
- 첫째 줄에 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성하기. 

- 입력 예시
```terminal
5
```

- 출력 예시
```terminal
11475
```

- **답안 예시**
```python
n = int(input())
count = 0

for i in range(n + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in (str(i) + str(j) + str(k)):
        count += 1

print(count)
```
⇒ 해당 문제는 **가능한 경우의 수를 모두 검사해보는 완전 탐색 유형으로 분류**된다. 일반적으로 알고리즘 문제에서는 확인 및 탐색해야 할 전체 데이터 개수가 100만개 이하일 때 완전 탐색을 사용하면 좋다.
  - 위의 문제에서는, 매 시각을 문자열로 바꾼 다음 문자열에 '3'이 포함됐는지 검사한다. 

<br>

## 📌 DFS/BFS 알고리즘
DFS/BFS는 대표적인 탐색 알고리즘으로 **기본 자료구조인 스택과 큐에 대한 이해**가 먼저 필요하다.    
그리고 DFS와 BFS를 구현하려면 **재귀 함수**도 이해하고 있어야 한다.

### 🖋️ 스택(Stack)
![image](https://user-images.githubusercontent.com/95380638/170251583-06a7f7e6-c615-40b7-8755-c401578d679d.png)

자료구조 스택은 아래에서부터 위로 박스를 쌓는 구조로 박스를 치울 때는 맨 위에 있는 박스를 먼저 내리게 되는 **후입선출 방식**    
입력연산은 Push / 출력연산은 Pop이라고 부른다.     
python 코드로 표현할 때 **append() 메서드**는 리스트 가장 뒤쪽에 데이터를 삽입하고 **pop() 메서드** 역시 리스트의 가장 뒤쪽에서 데이터를 꺼낸다.

- **스택을 python 코드로 표현하면 다음과 같다.**
```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
```

```terminal
[5, 2, 3, 1]
[1, 3, 2, 5]
```

<br>

### 🖋️ 큐(Queue)
<img src="https://user-images.githubusercontent.com/95380638/170252052-285588e1-d8e8-4fab-a3b3-6facef6d6393.png" width="700" height="400">



자료구조 큐는 대기 줄에 비유할 수 있고, 먼저 들어온 사람이 먼저 나가게 되는 **선입선출 방식**    
입력 동작은 Enqueue / 출력 동작은 Dequeue    
- python 코드로 표현할 때, **collections 모듈에서 제공하는 deque 라이브러리 활용**
  - 데이터 삽입/삭제 속도가 리스트 자료형에 비해 속도가 빠르다고 한다
  - 리스트 자료형은 데이터 삽입/삭제 시, ‘가장 뒤쪽 원소'를 기준으로 수행하므로 리스트 앞쪽에서 원소를 삽입/삭제할 때 많은 시간이 소요됨
  - [참고 블로그](https://devmath.tistory.com/12) 

- **큐를 python 코드로 표현하면 다음과 같다.**

```python
from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)  # 리스트 가장 뒤쪽에 삽입
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  # 리스트 가장 왼쪽에서 빼기
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
print(list(queue)) # deque 객체를 리스트 자료형으로 변경
```

```terminal
deque([3, 7, 1, 4])
deque([4, 1, 7, 3])
[4, 1, 7, 3]
```

<br>

### 🖋️ 재귀 함수
<img src="https://user-images.githubusercontent.com/95380638/170253846-e6067355-134a-496e-bb26-0577b6778655.png" width="600" height="400">

재귀 함수는 **자기 자신을 다시 호출하는 함수**를 의미    
python에서는 최대 재귀 깊이가 1,000으로 정해져 있어서, 자기자신을 계속 호출하다가 최대 재귀 깊이를 초과하면 **RecursionError**가 발생

```python
def recursive_function():
		print('재귀 함수를 호출합니다.')
		recursive_function()

recursive_function() # 함수 recursive_function()를 호출
```
```terminal
재귀 함수를 호출합니다.
재귀 함수를 호출합니다.
재귀 함수를 호출합니다.
...
RecursionError: maximum recursion depth exceeded while calling a Python object
```

<br>

### 🖋️ 재귀 함수의 종료 조건
재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시해야 한다.
- 재귀 함수는 내부적으로 스택 자료구조와 동일하다.
  - 함수를 계속 호출했을 때 → 가장 마지막에 호출한 함수가 먼저 종료되어야 그 앞의 함수 호출이 종료되기 때문이다.
  - 따라서 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다.

```python
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)
```

```terminal
1 번째 재귀 함수에서 2 번째 재귀 함수를 호출합니다.
2 번째 재귀 함수에서 3 번째 재귀 함수를 호출합니다.
...
99 번째 재귀 함수에서 100 번째 재귀 함수를 호출합니다.
99 번째 재귀 함수를 종료합니다.
...
2 번째 재귀 함수를 종료합니다.
1 번째 재귀 함수를 종료합니다.
```

<br>

### 🖋️ DFS(Depth-First-Search)
**깊이 우선 탐색**이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.    
즉, 가장 깊숙이 위치하는 노드에 닿을 때까지 탐색을 하게 된다.

- **스택 자료구조를 이용한 DFS 동작 과정**
  - 탐색 시작 노드를 스택에 삽입하고 방문 처리
  - 스택의 최상단 노드에, 방문하지 않은 인접 노드가 있다면 → 그 인접 노드 하나를 스택에 넣고 방문처리(일반적으로 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있다면 번호가 낮은 순서부터 처리)
  - 방문하지 않은 인접 노드가 없다면 → 스택에서 최상단 노드를 꺼내기
  - 위의 과정을 더 이상 수행할 수 없을 때까지 반복하기
  - [관련 블로그](https://www.crocus.co.kr/520)

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ') # 노드를 방문했을 때 터미널에 바로 출력
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
	    dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

```terminal
1 2 7 6 8 3 4 5
```

<br>

### 예제 - 모든 경로를 확인해봐야 하는 유형
- [해당 문제 설명](https://www.acmicpc.net/problem/2606)

- 입력 예시
```terminal
7
6
1 2
2 3
1 5
5 2
5 6
4 7
```

- 출력 예시
```terminal
4
```

- **답안 예시**
```python
import sys


# dfs 함수
def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = 1

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


n = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

# 각 노드가 연결된 정보를 표현
# 0이 n+1개가 담긴 리스트를 0번 노드부터 n번 노드까지 반복해서 담기
graph = [[0] * (n + 1) for i in range(n + 1)]

for i in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

# 각 노드의 방문유무
visited = [0] * (n + 1)

dfs(1)
# visited 리스트에서 1의 개수를 세고 처음 1번 컴퓨터를 제외해야 하니까 1 빼고 세기
print(visited.count(1) - 1)


#### 해당 문제는 1번 컴퓨터와 연결된 모든 경로를 다 확인해봐야 하니까 DFS로 푸는 것으로 이해했다!
```

<br>

### 🖋️ BFS(Breadth -First-Search)
**너비 우선 탐색**이라고 부르며, 가까운 노드부터 탐색하는 알고리즘이다.   
**BFS는 인접한 노드를 한꺼번에 큐에 삽입하여 DFS보다 수행시간이 빠르다.**

- **큐 자료구조를 이용한 BFS 동작 과정**
  - 탐색 시작 노드를 큐에 삽입하고 방문 처리
  - 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리(일반적으로 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있다면 번호가 낮은 순서부터 처리)
  - 위의 과정을 더 이상 수행할 수 없을 때까지 반복하다가 큐가 비었을 때 종료
  - [관련 블로그](https://www.crocus.co.kr/521?category=209527)

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑을 때 터미널에 바로 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 for문으로 모두 큐에 삽입
        for i in graph[v]:
	    if not visited[i]:
		queue.append(i)
		visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

```terminal
1 2 3 8 7 4 5 6
```

<br>

### 예제 - 모든 칸을 갈 필요가 없고 오른쪽과 아래만 가능하니까 최단 경로를 찾는 유형
- [해당 문제 설명](https://www.acmicpc.net/problem/16173)

- 입력 예시
```terminal
3
1 1 10
1 5 1
2 2 -1
```

- 출력 예시
```terminal
HaruHaru
```

- **답안 예시**
```python
import sys
from collections import deque


# bfs 함수 정의
def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True

    # 큐에 탐색해야 하는 노드 없을 때까지 실행
    while queue:

        a, b = queue.popleft()
        # 칸에 쓰여있는 수를 check라고 정의
        check = graph[a][b]

        # 현재 위치가 승리 지점이면 멈춰 성공 메시지 출력
        if check == -1:
            print("HaruHaru")
            return

        # 우, 하를 이동하여 비교
        for dx, dy in (1, 0), (0, 1): # 처음에는 하로 이동하고 / 그 다음에는 우로 이동
            x = a + dx * check
            y = b + dy * check

            # 정사각형 구역 내부이고 한번도 방문하지 않았으면 노드를 큐에 넣고 방문 처리한다.
            if 0 <= x < n and 0 <= y < n and visited[x][y] == False:
                queue.append((x, y))
                visited[x][y] = True

    # 모든 상황에서 승리 지점을 가지 못하면 실패 메시지 출력
    print("Hing")


n = int(sys.stdin.readline())
# 2차원 그래프로 표현
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 탐색 여부
visited = [[False] * n for _ in range(n)]
# 탐색
bfs()

#### 해당 문제를 bfs로 푸는 이유는, 내 생각엔 모든 칸을 갈 필요가 없고 오른쪽과 아래만 가능하니까 조건에 맞게 이동해서 탐색하는 것으로 
#### 최단 경로를 찾는 느낌으로 bfs를 사용한 것 같다!
```

<br>

### DFS와 BFS 비교
- 동작 원리 : DFS -> 스택 / BFS -> 큐
- 구현 방법 : DFS -> 재귀 함수 이용 / BFS -> 큐 자료구조 이용



<br>

## 📌 정렬 알고리즘
**정렬이란, 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 의미한다.** 정렬 알고리즘으로 데이터를 정렬하면 이진 탐색이 가능해진다.
정렬 알고리즘은 굉장히 다양하지만 그 중에서도 **선택 정렬 / 삽입 정렬 / 퀵 정렬 / 계수 정렬**에 대해서 배워보자. 해당 정렬들을 설명할 때는 
```terminal
7 5 9 0 3 1 6 2 4 8
```

**이렇게 0부터 9까지 숫자가 하나씩 적힌 10장의 카드를 오름차순으로 정렬하는 상황**을 공통적으로 가정하도록 한다.
**내림차순 정렬은 python에서 리스트의 요소들을 뒤집는 reverse() 메소드를 사용하면 된다.**

<br>

### 🖋️ 선택 정렬


