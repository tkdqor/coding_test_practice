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

## 📌 a, b = input().split(':')
- 다음과 같이 코드를 입력하면, 입력받는 값에서 :를 기준으로 값을 쪼개서 a와 b에 각각 저장해준다.

```python
a, b = input().split(':')

# Hello:World를 입력하면
print(a)

=> Hello
```

<br>

## 📌 print 함수의 sep
- print 함수의 sep을 이용해서 출력하고자 하는 문자열 사이를 수정할 수 있다.
```python
print('Hello', 'World')
```
```terminal
Hello World
```

- 위의 경우에는 한 줄에 모두 출력되지만, sep를 사용해서 문자열 사이 기준으로 다음줄에 출력할 수 있다.
```python
print('Hello', 'World', sep='\n')
```
```terminal
Hello
World
```

<br>

## 📌 10진법, 16진법
- 10진법은 한 자리에 10개(0 1 2 3 4 5 6 7 8 9)의 문자를 사용하고, 16진법은 영문 소문자를 사용하는 경우에 한 자리에 16개(0 1 2 3 4 5 6 7 8 9 a b c d e f)의 문자를 사용한다. 16진수 a는 10진수의 10, b는 11, c는 12 ... 와 같다.


<br>

## 📌 유니코드(Unicode)
- **컴퓨터로 저장되고 처리되는 모든 데이터들은 2진수 형태로 정수화** 되어야 하는데, 컴퓨터에 문자를 저장하는 방법으로 아스키코드(ASCII Code)나 유니코드(Unicode)가 자주 사용된다. 예를 들어, 영문 대문자 'A'는 10진수 값 65 로 표현하고 -> 2진수(binary digit) 값 1000001 로 바꾸어 컴퓨터 내부에 저장한다. **유니코드(unicode)는 세계 여러 나라의 문자를 공통된 코드 값으로 저장할 때 사용하는 표준 코드이다.**

- **유니코드 관련, chr() 함수는 10진수 정수값을 문자로 바꿔주고 / ord() 함수는 문자 1개를 10진수 정수값으로 바꿔준다.**
```python
print(chr(65))
print(ord("A"))
```
```terminal
A
65
```

<br>

## 📌 bool() 함수
- bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력해준다. python 언어에서 정수값 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)로 평가된다. 빈 문자열 "" 나 ''는 False 이고, 나머지 문자열들은 True 로 평가된다.


<br>

## 📌 비트시프트연산과 비트단위(bitwise) 연산자
- 컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에, 2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로 지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데, 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고, 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고, 가장 오른쪽에 있는 1비트는 사라진다.

- **~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor), <<(bitwise left shift), >>(bitwise right shift) 이러한 비트단위 연산자가 있다.**
  - 예를 들어 1이 입력되었을 때 저장되는 1을 32비트 2진수로 표현하면 00000000 00000000 00000000 00000001 이고, ~1은 11111111 11111111 11111111 11111110 가 되는데 이는 -2를 의미한다.
  - 비트단위 and 연산은 두 비트열이 주어졌을 때, 둘 다 1인 부분의 자리만 1로 만들어주는 것과 같다.
    - 예를 들어 3과 5가 입력되었을 때를 살펴보면 3 : 00000000 00000000 00000000 00000011 5 : 00000000 00000000 00000000 00000101 3 & 5 : 00000000 00000000 00000000 00000001 이 된다.
  - 비트단위 or 연산은 둘 중 하나라도 1인 자리를 1로 만들어주는 것과 같다.
    - 예를 들어 3과 5가 입력되었을 때를 살펴보면 3 : 00000000 00000000 00000000 00000011 5 : 00000000 00000000 00000000 00000101 3 | 5 : 00000000 00000000 00000000 00000111 이 된다.
  - 비트단위 ^ 연산은 두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리하는 것과 같다.
    - 예를 들어 3과 5가 입력되었을 때를 살펴보면 3 : 00000000 00000000 00000000 00000011 5 : 00000000 00000000 00000000 00000101 3 ^ 5 : 00000000 00000000 00000000 00000110 이 된다.


<br>

## 📌 3항 연산 - "x if C else y"
- 3개의 요소로 이루어지는 3항 연산은 "x if C else y" 의 형태로 작성이 된다.
  - C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
  - x : C의 평가 결과가 True 일 때 사용할 값
  - y : C의 평가 결과가 True 가 아닐 때 사용할 값

```python
print((0 if 123>456 else 1))

=> 1
```
- 이렇게 123>456이 False이니까 1이 출력된다.

- **a, b, c 3개의 값 중 가장 작은 값을 계산하는 코드**

```python
a, b, c = map(int, input().split())
d = a if(a<b) else b
e = d if(d<c) else c
print(e)

==> 12 35 20
==> 12
```

<br>

## 📌 정수 3개 입력 받아 짝수만 출력하기
```python
a, b, c = map(int, input().split())
numbers = [a, b, c]

# 짝수니까 나누기 2를 해서 나머지가 0이면 출력하고 아니면 출력 안하기
for number in numbers:
    if number % 2 == 0:
        print(number)
```

cf) 3의 배수만 출력하는 경우는, 아래와 같이 표현할 수 있다.
```python
a, b, c = map(int, input().split())
numbers = [a, b, c]

for number in numbers:
    if number % 3 == 0:
        print(number)
```


<br>

## 📌 if문 중첩 생각하기
```python
a = int(input())
if (a < 0):
    if (a % 2 == 0):
        print("A")
    else:
        print("B")

else:
    if (a % 2 == 0):
        print("C")
    else:
        print("D")   
```	

<br>

## 📌 정수 1개를 입력받아 0부터 그 수까지 출력하기
```python
n = int(input())

i = 0
while i<=n:
    print(i)
    i += 1
```    

<br>

## 📌 1부터 순서대로 계속 더하다가 입력된 정수와 같거나 커졌을 때 마지막에 더한 정수 출력
```python
n = int(input())

t = 0
s = 0

while s < n:
    t += 1
    s += t

print(t)
```


<br>

## 📌 3명이 같은 날 가입/등업하고, 각각 3/7/9일 마다 들어온다면 처음 가입하고 몇일 만에 다시 만나는지
```python
# day는 일 수, a/b/c는 방문 주기이다.

d = 1
a = 3
b = 7
c = 9

while d%a!=0 or d%b!=0 or d%c!=0:
  d += 1
print(d)

# while이 끝나는 건 모든 일 수로 나눌 때 다 0으로 딱 떨어지는 경우에 while문이 종료된다.
```

<br>

## 📌 n = 10일 때, 9부터 1까지 거꾸로 출력하기
```python
n = 10

for i in range(n-1, 0, -1):
    print(i, end=' ')
```

* * *

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
**선택 정렬은 데이터가 무작위로 여러 개 있을 때, 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복하는 것이다.**    
그래서 매번 **'가장 작은 것을 선택'** 한다는 의미에서 선택 정렬 알고리즘이라고 한다.    
- [선택 정렬 그림 예시](https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html)

- **선택 정렬 동작 과정**
  - 데이터 10개가 있을 때, 전체 중에서 **가장 작은 데이터를 선택**해서 맨 앞에 있는 데이터와 바꾼다.
  - 이제 정렬된 첫 번째는 제외하고 이후 데이터 중에서 가장 작은 데이터를 선택해서 처리되지 않은 데이터 중 가장 앞에 있는 데이터와 바꾼다.
  - 해당 과정을 9번 반복하면 오름차순 정렬이 완성된다. 이처럼 선택 정렬은 가장 작은 데이터를 앞으로 보내는 과정을 데이터가 N개라고 하면, N - 1번 반복하면 정렬이 완료된다. 

- **선택 정렬을 python 코드로 표현하기**
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)): # 리스트에서 맨 앞에 있는 데이터를 뽑아놓기
    min_index = i # 가장 작은 원소의 인덱스를 찾는 과정 시작
    # 리스트 맨 앞에 있는, 처리하지 않은 데이터를 제외한 나머지 데이터를 1개씩 뽑아 크기 비교해서 가장 작은 원소 찾기
    for j in range(i + 1, len(array)):  
        if array[min_index] > array[j]:
            min_index = j # 가장 작은 원소의 인덱스 j를 찾은 상태
    array[i], array[min_index] = array[min_index], array[i] # 이 때, 리스트 맨 앞 데이터와 가장 작은 원소 바꾸기

print(array)
```

- **선택 정렬의 시간 복잡도는 반복문이 2중으로 사용되었기 때문에, O(N²) 이라고 볼 수 있다.**
  - 따라서, 정렬해야 할 데이터의 개수가 100개라면 이론적으로 수행 시간은 10,000번이 된다.
  - **선택 정렬은 다른 정렬 알고리즘과 비교했을 때 매우 비효율적이지만, 특정한 리스트에서 가장 작은 데이터를 찾는 일이 코딩 테스트에서 많이 나오므로 해당 소스코드 형태에 익숙해지자.**

<br>

### 🖋️ 삽입 정렬
**삽입 정렬은 특정한 데이터를 적절한 위치에 삽입한다는 의미에서 삽입 정렬이라고 부른다.** 선택 정렬에 비해 실행 시간 측면에서 더 효율적인 알고리즘으로 알려져 있다.     
선택 정렬은 현재 데이터의 상태와 상관없이 무조건 모든 원소를 비교하고 위치를 바꾸는 반면 삽입 정렬은 그렇지 않다.     
- [삽입 정렬 그림 예시](https://wonjayk.tistory.com/218)

- **삽입 정렬 동작 과정**
  - 데이터가 10개 있을 때, 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단하기 때문에 두 번째 데이터부터 시작한다.
  - 그래서 두 번째 데이터가 어떤 위치로 들어갈지 판단한다. 첫 번째 데이터의 왼쪽 혹은 오른쪽으로 들어가는 경우를 판단해서 둘 중 한 곳에 삽입하게 된다.
  - 이어서 세 번째 데이터는 앞의 2개의 데이터가 있으므로, 첫 번째 데이터의 왼쪽 / 2개 데이터 사이 / 두 번째 데이터의 오른쪽 이렇게 3가지의 경우가 존재한다. 이번에도 3곳 중 한 곳에 삽입하게 된다.
  - 이와 같은 과정을 9번, 즉 데이터 개수가 N개일 때, N - 1번 반복하면 모든 데이터가 오름차순 정렬이 된다. 

- **삽입 정렬의 특징은, 특정한 데이터의 왼쪽에 있는 데이터들은 이미 정렬이 된 상태이므로, 삽입될 위치를 찾기 위해 왼쪽으로 한 칸씩 이동할 때 자기보다 작은 데이터를 만났다면 더 이상 데이터를 살펴볼 필요 없이 그 자리에 삽입이 되면 된다.**

- **삽입 정렬을 python 코드로 표현하기**
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 리스트의 첫 번째 데이터가 아닌 두 번째 데이터부터 뽑기
    for j in range(i, 0, -1): # 인덱스 i부터 인덱스 1까지 1씩 감소하면서 거꾸로 꺼내기
        if array[j] < array[j - 1]: # 왼쪽 데이터와 크기 비교해서 왼쪽이 더 크면
            array[j], array[j - 1] = array[j - 1], array[j] # 자리 바꾸기
        else: # 만약 왼쪽 데이터가 더 작으면 그 자리에서 멈추기
            break

print(array)
```

- **range 함수의 매개 변수는 3개(start, end, step)인데, 여기서 세번째 매개 변수 step에 -1이 들어가면 -> start 인덱스부터 시작해서 end + 1 인덱스까지 1씩 감소하게 된다.**


- **삽입 정렬의 시간 복잡도는 선택 정렬과 마찬가지로 반복문이 2중으로 사용되었기 때문에, O(N²) 이라고 볼 수 있다.**
  - 다만, 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다는 점이 다르다.
  - **따라서, 거의 정렬되어 있는 상태로 입력이 주어지는 문제라면 -> 다른 정렬 알고리즘을 이용하는 것 보다 삽입 정렬을 이용하는 것이 정답 확률을 높일 수 있다.**

<br>

### 🖋️ 퀵 정렬
퀵 정렬은 지금까지 배운 정렬 알고리즘 중에 가장 많이 사용되고 빠른 정렬 알고리즘으로 알려져 있다.     
**퀵 정렬은 기준 데이터를 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.**    
이 때, **교환하기 위한 '기준'을 피벗**이라고 표현한다. 퀵 정렬을 수행하기 전에는 피벗을 어떻게 설정하고 리스트를 분할할지 정해야 하는데 지금 예제는 **"호어 분할 방식"** 을 기준으로 이해해보자.

- **퀵 정렬 동작 과정**
  - **리스트에서 첫 번째 데이터를 피벗으로 정한다.**
  - 그리고 리스트에서 피벗을 제외한 나머지 데이터들 중에 -> 왼쪽에서부터 피벗보다 큰 데이터를 찾고 / 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
  - 그 다음 큰 데이터와 작은 데이터의 위치를 서로 교환해준다.
  - 그리고 다시 피벗보다 큰 데이터와 작은 데이터를 왼쪽과 오른쪽에서 각각 찾는다. 찾은 뒤에는 두 값의 위치를 서로 교환한다.
  - 해당 과정을 반복하다가 -> 왼쪽에서부터 찾는 큰 값과 오른쪽에서부터 찾는 작은 값의 위치가 서로 엇갈리는 경우가 발생한다. 이 때는, 작은 데이터 값과 피벗의 위치를 서로 변경해준다.
  - **이렇게 피벗이 이동한 다음 데이터의 정렬을 보면, 피벗을 기준으로 왼쪽 데이터는 피벗보다 작은 데이터가 오고 / 오른쪽 데이터는 피벗보다 큰 데이터가 오게 된다. 이렇게 하는 작업을 "분할" 혹은 "파티션"이라고 한다.**
  - **이러한 상태에서 왼쪽 리스트와 오른쪽 리스트에서도 각각 피벗을 설정해서 -> 동일한 방식으로 정렬을 수행하면 전체 리스트에 대해서 모두 오름차순 정렬이 이루어질 것이다.**
  - 이렇게 퀵 정렬은 특정한 리스트에서 피벗을 설정하여 정렬을 수행하고, 피벗을 기준으로 왼쪽 리스트와 오른쪽 리스트에서 각각 다시 정렬을 수행하기 때문에 -> **재귀함수 형태와 동작 원리가 같다.**
    - **이러한 퀵 정렬이 끝나는 조건은 -> 현재 리스트의 데이터 개수가 1개인 경우에 종료된다.**

- **퀵 정렬을 python 코드로 표현하기**
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 퀵 정렬 함수가 한 번 실행되면 -> 큰 데이터와 작은 데이터를 찾아 서로 교체하는 것 까지 수행할 수 있도록 설정
def quick_sort(array, start, end): 
    if start >= end: # 원소가 1개인 경우 종료
        return 
    pivot = start # 피벗은 첫 번째 원소 인덱스로 설정
    left = start + 1 # 피벗 제외 데이터에서 왼쪽 인덱스는 피벗 바로 다음 번호로 설정
    right = end      # 피벗 제외 데이터에서 오른쪽 인덱스는 데이터에서 맨 오른쪽 번호로 설정

    # 여기서 pivot / start / end는 바뀌지 않는다!
    
    while left <= right: # 왼쪽과 오른쪽 인덱스가 서로 엇갈리지 않을 동안만 반복
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]: # left 인덱스가 데이터 끝 인덱스보다 작거나 같고 / 피벗보다 작거나 같으면 안되니까 계속 반복
            left += 1                                      # left 인덱스를 오른쪽로 옮기기
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]: # right 인덱스가 데이터 처음 인덱스보다 크고 / 피벗보다 크거나 같으면 안되니까 계속 반복
            right -= 1                                        # right 인덱스를 왼쪽으로 옮기기
        
        if left > right: # 왼쪽 인덱스가 오른쪽 인덱스보다 크다면(즉, 서로 엇갈렸다면) -> 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:            # 서로 엇갈리지 않았다면 -> 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 왼쪽과 오른쪽 인덱스가 서로 엇갈린 상황이라면 -> while문이 종료되고 분할되었다는 의미
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1) # 이 때는 right가 피벗을 의미하니까 -> start부터 피벗 - 1 인덱스까지 정렬 수행
    quick_sort(array, right + 1, end)   # 이 때는 right가 피벗을 의미하니까 -> 피벗 + 1 인덱스부터 end까지 정렬 수행

quick_sort(array, 0, len(array) - 1)
print(array)
```

- 위의 소스코드는 가장 직관적인 형태의 퀵 정렬 소스코드이다.

<br>

### 🖋️ 계수 정렬
계수 정렬 알고리즘은 특정한 조건이 부합할 때만 사용할 수 있으나 매우 빠른 정렬 알고리즘이다.   
계수 정렬은 **'데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때'** 만 사용할 수 있다. 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적이다.   
이러한 특징을 가지는 이유는, 계수 정렬을 이용할 때 **'모든 범위를 담을 수 있는 크기의 리스트(배열)를 선언'** 해야 하기 때문이다.

- **계수 정렬 동작 과정**
  - 먼저, 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성
  - 이 때, 리스트의 인덱스가 모든 범위를 포함할 수 있도록 한다. 그리고 처음에는 리스트의 모든 데이터가 0이 되도록 초기화한다.
  - 그 다음, 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시키면 계수 정렬이 완료된다.
  - 결과적으로 리스트에는 각 데이터가 몇 번 등장했는지 횟수가 기록된다. ex) 5 인덱스의 값이 2라면 '5'는 2번 등장한 것이다.
  - 마지막으로 리스트의 첫 번째 데이터부터 하나씩 인덱스 횟수만큼 출력하면 오름차순으로 정렬된 것을 확인할 수 있다. 

- **계수 정렬을 python 코드로 표현하기**
```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6 ,2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1) # 리스트 내부의 데이터 중 가장 크기가 큰 데이터를 포함할 수 있도록 0를 설정

for i in range(len(array)):
    count[array[i]] += 1 # array 데이터에 해당하는 count 리스트 인덱스 값을 +1 해주기

for i in range(len(count)):   # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')     # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```
```terminal
0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
```

- **계수 정렬의 시간 복잡도**
  - 계수 정렬의 시간 복잡도는 모든 데이터가 양의 정수인 상황에서 데이터 개수가 N, 데이터 중 최대값의 크기를 K라고 할 때, 계수 정렬의 시간 복잡도는 **O(N + K)** 이다.
  - 항상 사용할 수 있는 정렬 알고리즘은 아니고, 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하다.

<br>

## 📌 이진 탐색 알고리즘
이진 탐색에 대해 알아보기 전에 가장 기본 탐색 방법인 순차 탐색에 대해 먼저 이해할 필요가 있다.     
**순차 탐색**이란, 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다. 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.

<br>

### 🖋️ 순차 탐색
순차 탐색은 이름처럼 **순차로 데이터를 탐색**한다는 의미이다.     
이러한 순차 탐색은 리스트에 특정 값의 원소가 있는지 체크할 때 사용할 수 있다. 

아래와 같은 예시 문제를 파이썬 코드로 작성할 수 있다. 리스트에서 찾고자 하는 문자열을 찾으면, 리스트에서 몇 번째 위치에 있는지 알려주는 코드이다.
```terminal
Q. 생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하기
Q. 앞서 적은 원소 개수만큼 문자열을 입력하기(구분은 띄어쓰기 한 칸)
```

- **순차 탐색 소스코드**

```python
# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1        # 현재의 위치 반환(인덱스는 0부터 시작하므로 1을 더해주기)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split() # 받은 데이터를 리스트로 만들어주기
n = int(input_data[0])       # 원소의 개수
target = input_data[1]       # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()      # 받은 문자열들을 리스트로 만들어주기

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
```

```terminal
생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.
5 사과
앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.
석류 오렌지 귤 사과 복숭아

=> 4
```

- **이처럼 순차 탐색은 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인해야 한다는 점이 특징이다.**
- **따라서 데이터 개수가 N개라고 한다면 → 최대 N번의 비교 연산이 필요하므로 최악의 경우, 시간 복잡도는 O(N)이다.**

<br>

### 🖋️ 이진 탐색
- **이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘으로 이미 정렬된 데이터에서 특정 값을 찾을 수 있다.**
  - 데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 빠르게 데이터를 찾을 수 있다.

- **이진 탐색은 위치를 나타내는 변수 3개를 사용한다.**
  - 탐색하고자 하는 범위의 **시작점 / 끝점 / 중간점**이다.
  - 찾으려고 하는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 게 이진 탐색 과정이다.

- **이진 탐색 진행 과정 - ex) 정렬된 데이터 10개 중, 값이 4인 원소 찾기**
  - 배열에서 시작점 인덱스와 끝점 인덱스를 확인한 다음, 둘 사이에 중간점 인덱스를 정한다. 만약 중간점 인덱스가 실수일 경우, 소수점 이하를 버린다. (시작점이 [0], 끝점이 [9]라면 중간점은 4.5에서 소수점 이하를 버려서 [4]이다)
  - 그 다음, 중간점 [4]의 데이터 8과 찾으려는 데이터인 4를 비교한다.
  - 이 때, 중간점의 데이터 8이 더 크다면 → 이미 정렬되어 있으니 중간점 이후의 값은 확인할 필요가 없어진다. 그래서 끝점을 [4]의 이전인 [3]으로 옮긴다.
  - 이제 시작점 / 끝점 / 중간점을 다시 정한다. 시작점은 [0], 끝점이 [3]이니까 중간점은 1.5로 [1]이다. 
  - 이 때, 중간점의 데이터 2가 찾으려는 데이터 4보다 작으니까 → 이미 정렬되어 있으니 중간점 이하의 값은 확인할 필요가 없어진다. 그래서 시작점을 [1]의 이후인 [2]로 옮긴다.
  - 이제 시작점은 [2], 끝점은 [3]이니까 중간점은 2.5로 [2]이다. 중간점에 위치한 데이터가 찾으려는 데이터 4이므로 이 시점에서 탐색을 종료한다.

- **이진 탐색은 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서, 시간 복잡도가 O(logN)이다.**

- **재귀 함수로 구현한 이진 탐색 소스코드**
```python
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None # start 인덱스가 end 인덱스보다 크면 종료
    # 중간점 설정
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 -> 끝점을 중간점 이전으로 설정
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 -> 시작점을 중간점 이후로 설정
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

```terminal
# 원소의 개수와 찾는 데이터 입력받기
10 7 
# 전체 데이터 입력받기
1 3 5 7 9 11 13 15 17 19

=> 4 # 찾고자 하는 데이터의 순서 출력
```

- **반복문으로 구현한 이진 탐색 소스코드**
```python
# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        # 중간점 설정
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 -> 끝점을 중간점 이전으로 설정
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 -> 시작점을 중간점 이후로 설정
        else:
            start = mid + 1
    return None

# n(원소의 개수)와 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

<br>

### 🖋️ 트리 자료구조
- 이진 탐색은 전제 조건이 데이터 정렬인데, 동작하는 프로그램에서 **트리 자료구조**를 통해 데이터를 정렬해 둔다면 이진 탐색을 효과적으로 사용할 수 있다.
- **데이터베이스**는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용해서 항상 데이터가 정렬되어 있다. 데이터베이스에서는 이진 탐색과 유사한 방법으로 탐색해서 데이터가 많아도 탐색하는 속도가 빠르다.

- **트리 자료구조 특징**
  - 트리 자료구조는 그래프 자료구조의 일종으로 데이터베이스 시스템이나 파일 시스템과 같은 곳에서 많은 양의 데이터를 관리하기 위한 목적으로 사용한다. 
  - 트리 자료구조는 다음과 같은 특징을 가지고 있다.
    - 트리는 부모 노드와 자식 노드의 관계로 표현한다
    - 트리의 최상단 노드를 루트 노드 / 최하단 노드를 단말 노드라고 한다
    - 트리에서 일부를 떼어내도 트리구조이며 이를 서브 트리라고 한다
    - **큰 데이터를 처리하는 소프트웨어는 대부분 데이터를 트리 자료구조로 저장해서 이진 탐색과 같은 탐색 기법을 이용해 빠르게 탐색이 가능하다**

<br>

### 🖋️ 이진 탐색 트리
- 트리 자료구조 중에서도 가장 간단한 형태가 **이진 탐색 트리**이다. 즉, 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다. 
- 그리고 이진 탐색 트리는 **부모 노드보다 왼쪽 자식 노드가 작고 / 부모 노드보다 오른쪽 자식 노드가 크다.**

![image](https://user-images.githubusercontent.com/95380638/173019082-e2eb3037-5daf-44e6-bc2b-1eff141b3b5c.png)

- 즉, **왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드** → 이게 성립되어야 이진 탐색 트리라고 할 수 있다. 위의 그림에서도 17 < 30 < 48으로 성립한다는 걸 알 수 있다. 

- **이진 탐색 트리에서 데이터를 조회하는 과정 - ex) 원소 37를 찾는 과정**
  - 처음에는 루트 노드인 30과 찾는 원소값 37일 비교한다. 공식에 따라 부모 노드의 왼쪽 자식 노드는 30 이하이므로 → 왼쪽에 있는 모든 노드는 확인할 필요가 없다. 따라서 오른쪽 노드를 방문한다.
  - 오른쪽 자식 노드인 48이 이번에는 부모 노드가 된다. 그래서 48과 찾는 원소값 37를 비교한다. 공식에 따라 부모 노드의 오른쪽 자식 노드는 모두 48 이상이니까 확인할 필요가 없다. 따라서 왼쪽 노드를 방문한다.
  - 현재 방문한 노드의 값인 37과 찾은 원소값인 37이 동일하다. 따라서 탐색을 마친다. 
  - 만약 자식 노드가 없을 때까지 원소를 찾지 못했다면, 이진 탐색 트리에 원소가 없는 것이다.

<br>

### 🖋️ 빠르게 입력받기
- 이진 탐색 문제처럼 입력 데이터가 많고 탐색 범위가 넓은 경우, 예를 들어 데이터의 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면 input() 함수를 사용하게 되면 동작 속도가 느려 시간 초과로 오답 판정을 받을 수 있다.
- **이처럼 입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다.**

```python
import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)
```

- **이렇게 sys 라이브러리를 사용할 때는 rstrip() 함수를 꼭 호출해야 한다. 만약 입력하지 않고 readline() 에서 끝내면 입력 후 엔터가 줄 바꿈 기호로 입력되서 비어있는 한 줄이 출력된다. 따라서 해당 줄을 제거하기 위해 rstrip() 함수를 사용하자.**

<br>

## 📌 다이나믹 프로그래밍
- **컴퓨터를 효율적으로 이용하려면 연산 속도와 메모리 공간을 최대한 활용해야 하는데, 다이나믹 프로그래밍이란 메모리 공간을 조금 희생해 연산속도를 비약적으로 증가시키는 알고리즘 설계 기법이라고 할 수 있다. 즉, 공간복잡도는 조금 증가하지만 시간복잡도는 크게 감소한다.**
- **또한, 다이나믹 프로그래밍은 필요한 계산 값을 저장해두었다가 재사용하는 알고리즘 설계 기법이라고도 한다.** 큰 문제를 한번에 해결하기 어려울 때, 여러개의 작은 문제로 나누어 푸는 '분할 정복' 알고리즘이 있다. 이때 동일한 작은 문제들이 반복적으로 계산되는 경우가 생길 수 있다. 그 문제를 매번 재계산 하지 않고 값을 저장했다가 재사용하는 기법인 것이다.

- **다이나믹 프로그래밍 사용 조건**
  - 큰 문제를 작은 문제로 나눌 수 있어야 한다.
  - 작은 문제에서 구한 정답은 작은 문제를 포함하는 큰 문제에서도 동일해야 한다.

- **다이나믹 프로그래밍 구현 방법**       
**(1) 탑다운 방식**
- 메모제이션 혹은 캐싱이라고도 하는데, 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출해 메모한 결과를 그대로 다시 사용하는 기법이다.
- 그래서, 한 번 구한 정보를 리스트에 저장하고 / 다이나믹 프로그래밍을 재귀적으로 수행하다 이미 호출된 값을 필요로 하는 경우 리스트에 저장된 그 값을 가져온다.     
  - ex) 피보나치 수열



