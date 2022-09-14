## collection of ideas

### Codes

- 📖 **Contents**
  - [숫자 구분자](#숫자-구분자)	
  - [소수 반올림](#소수-반올림)
  - [set 함수](#set-함수)
  - [퍼센트 포매팅](#퍼센트-포매팅)
  - [람다 함수란](#람다-함수란)
  - [특정 숫자가 소수인지 확인하는 함수](#특정-숫자가-소수인지-확인하는-함수)
  - [함수의 return](#함수의-return)
  - [2차원-리스트-생성과-접근](#2차원-리스트-생성과-접근)
  - [튜플에 있는 원소 값에 접근하기](#튜플에-있는-원소-값에-접근하기)
  - [리스트 값들을 랜덤으로 섞기](#리스트-값들을-랜덤으로-섞기)
  - [리스트 관련 내장함수 clear](#리스트-관련-내장함수-clear)
  - [리스트 관련 내장함수 remove](#리스트-관련-내장함수-remove)
  - [리스트 관련 내장함수 pop](#리스트-관련-내장함수-pop)
  - [리스트 관련 내장함수 insert](#리스트-관련-내장함수-insert)
  - [리스트 합치기](#리스트-합치기)
  - [특정 아스키번호에 대응되는 알파벳 문자열을 반환하는 chr 함수](#특정-아스키번호에-대응되는-알파벳-문자열을-반환하는-chr-함수)
  - [특정 알파벳 문자열의 아스키번호를 반환하는 ord 함수](#특정-알파벳-문자열의-아스키번호를-반환하는-ord-함수)
  - [알파벳일 경우에만 True 반환하는 isalpha 함수](#알파벳일-경우에만-true-반환하는-isalpha-함수)
  - [특정 문자열이 대문자인지 소문자인지 확인하는 isupper와 islower 함수](#특정-문자열이-대문자인지-소문자인지-확인하는-isupper와-islower-함수)
  - [리스트 인덱스 관련](#리스트-인덱스-관련)
  - [문자열 관련 find와 count 함수](#문자열-관련-find와-count-함수)
  - [문자열을 전부 대문자 혹은 소문자로 바꾸는 upper와 lower 함수](#문자열을-전부-대문자-혹은-소문자로-바꾸는-upper와-lower-함수)
  - [2중 for문으로 별 5개부터 1개 출력하기](#2중-for문으로-별-5개부터-1개-출력하기)
  - [N의 약수 출력하기](#n의-약수-출력하기)
  - [for와 else 구문 그리고 break](#for와-else-구문-그리고-break)
  - [range로 10부터 1까지 출력하기](#range로-10부터-1까지-출력하기)
  - [range를 변수로 리스트 만들기](#range를-변수로-리스트-만들기)
  - [if elif else문은 하나의 문장 구조](#if-elif-else문은-하나의-문장-구조)
  - [실수와 정수 더하면 Type은 실수형](#실수와-정수-더하면-type은-실수형)
  - [List Comprehension](#list-comprehension)
  - [zip 함수를 이용해 같은 인덱스에 해당하는 요소들을 뽑기](#zip-함수를-이용해-같은-인덱스에-해당하는-요소들을-뽑기)
  - [값 교환하기](#값-교환하기)
  - [if else나 for else는 같은 인덴트로 작성하고 다른 문의 경우에는 한 인덱스 들여쓰고 쓰는 예시](#if-else나-for-else는-같은-인덴트로-작성하고-다른-문의-경우에는-한-인덱스-들여쓰고-쓰는-예시)
  - [append와 extend 차이점](#append와-extend-차이점)
  - [해시에서 key만 따로 value만 따로 선택할 수 있게 해주는 keys와 values함수](#해시에서-key만-따로-value만-따로-선택할-수-있게-해주는-keys와-values함수)
  - [해시에서 key와 value를 동시에 선택할 수 있게 해주는 items 함수](#해시에서-key와-value를-동시에-선택할-수-있게-해주는-items-함수)
  - [문자열에 0을 채우는 방법으로 rjust 함수 사용하기](#문자열에-0을-채우는-방법으로-rjust-함수-사용하기)
  - [format 함수 문자열 포맷팅으로 변수들을 이용해서 하나의 문자열로 조합하는 방법](#format-함수-문자열-포맷팅으로-변수들을-이용해서-하나의-문자열로-조합하는-방법)
  - [리스트의 마지막 요소 값 출력하기](#리스트의-마지막-요소-값-출력하기)
  - [strip 함수 관련 내용](#strip-함수-관련-내용)
  - [all 함수란](#all-함수란)
  - [any 함수란](#any-함수란)
  - [리스트 요소의 인덱스를 확인하는 index 함수](#리스트-요소의-인덱스를-확인하는-index-함수)
  - [리스트를 만드는 다른 방법](#리스트를-만드는-다른-방법)
  - [10진수 숫자를 이진수 문자열로 돌려주는 bin 함수](#10진수-숫자를-이진수-문자열로-돌려주는-bin-함수)
  - [리스트 요소 순서 거꾸로 하기](#리스트-요소-순서-거꾸로-하기)
  - [for문으로 범위 설정하기](#for문으로-범위-설정하기)
  - [max와 min 함수](#max와-min-함수)
  - [map 함수 사용하기](#map-함수-사용하기)
  - [해당 매개변수가 지정한 타입이 맞는지 확인하는 isinstance 함수](#해당-매개변수가-지정한-타입이-맞는지-확인하는-isinstance-함수)
  - [문자열을 split를 이용해 나누게 되면 리스트 형태](#문자열을-split를-이용해-나누게-되면-리스트-형태)
  - [인덱스와 함께 요소들을 뽑아낼 수 있는 enumerate 함수](#인덱스와-함께-요소들을-뽑아낼-수-있는-enumerate-함수)
  - [리스트 슬라이싱](#리스트-슬라이싱)
  - [sort 함수와 sorted 함수](#sort-함수와-sorted-함수)
  - [global 사용하기](#global-사용하기)
  - [병합 연산자 사용하기](#병합-연산자-사용하기)
  - [permutation 함수로 순열 만들기](#permutation-함수로-순열-만들기)
  - [문자열 변수로 리스트를 만드는 list 함수](#문자열-변수로-리스트를-만드는-list-함수)
  - [range 함수의 마지막 매개변수는 range의 간격을 지정](#range-함수의-마지막-매개변수는-range의-간격을-지정)
  - [join 함수 사용하기](#join-함수-사용하기)
  - [루트 계산 관련](#루트-계산-관련)
  - [정수 연산 예시](#정수-연산-예시)
  - [반복문에서 조건이 맞지 않을 때 반복문을 종료시키지 않고 맨 처음의 조건문으로 보내주는 continue](#반복문에서-조건이-맞지-않을-때-반복문을-종료시키지-않고-맨-처음의-조건문으로-보내주는-continue)
  - [문자열 반복하기](#문자열-반복하기)
  - [리스트에서 원하는 값 제거하는 방법](#리스트에서-원하는-값-제거하는-방법)
  - [주어진 문자열이 숫자로 되어있는지 검사하는 함수](#주어진-문자열이-숫자로-되어있는지-검사하는-함수)
  - [while문 종료 조건 생각하기](#while문-종료-조건-생각하기)


<br>

### 숫자 구분자
- python에서 변수를 정수로 입력할 때, 언더바(_)를 이용해서 세자리 단위를 표현할 수 있다. 

```python
num = 1000000
num2 = 1_000_000
print(num)
print(num2)

1000000
1000000
```

<br>

### 소수 반올림
- **python에서의 round 함수는 round_half_even 방식을 택하고 있고, 우리가 흔히 알고 있는 반올림은 round_half_up 방식으로 4까지는 내림이고 5부터는 올림을 진행한다. 그래서 다르게 해야한다.**
```python
ex) a = 4.500
print(round(a))

4

a = 5.500
print(round(a))

6
```
- 이렇게 round는 정확하게 half 지점에 있을 때 짝수가 되게끔 한다. 그래서 4가 나오고 a = 4.600이면 5가 나온다. 즉, 소수점 첫째자리가 지금처럼 5일 경우 우리가 생각하는 반올림처럼 되지 않는 다는 게 문제이다. 
A = 5.500의 경우에는 half 지점에서 짝수게 되게끔 해서 6이 출력된다.

```python
a = 66.6
a = a + 0.5
a = int(a)

67
```
- 그래서, 이렇게 해당하는 실수에다가 0.5를 더한 값을 기준으로 확인하면 된다. 소수점 첫째자리가 5이상이면 0.5를 더했을 때 첫째자리가 올라갈 것이고 소수점 첫째자리가 4이하라면 안 올라갈 것이다. 그 다음, int() 함수를 사용해서 형변환을 하면 소수점이 없어지게 된다.

<br>

### set 함수
- **set() 자료구조에서는 요소를 추가할 때 append가 아니라 add를 사용**
- **set()이라는 자료구조는 sort() 기능이 없다. 그래서 다시 list화 해야된다.**

- **set 함수 예시**
```python
print(set(range(0, 2)))

{0, 1}

print(set(range(0, 3)) - set(range(0, 2)))

{2}
```

<br>

### 퍼센트 포매팅
```python
num = 50
s = 'my age %d' % num
print(s)

my age 50

# %s -> 문자열
# %d -> 정수
# %f -> 실수
```

- https://blockdmask.tistory.com/428	

<br>

### 람다 함수란
- 람다 함수는 함수에 이름이 없다고 해서 익명의 함수라고도 한다. 일반적으로는 함수를 만들어서 그 함수를 호출해서 사용하게 되는데, 람다 함수는 다르다.
```python
plus_two = lambda x: x+2
print(plus_two(1))

3
```
- 이렇게 먼저 lambda라고 쓰고 x를 입력하면 이 때 x가 매개 변수가 된다. 그리고 :를 입력한 다음 : 뒷부분에 함수의 내용을 입력하면 된다. 그래서 위의 예시에서는 x+2라는 내용을 입력했다.
이렇게 작성하면 값을 넘겼을 때, 그 값에 +2한 값을 리턴해주는 함수가 만들어지게 된다. 근데, 람다 함수는 어떤 변수에다가 할당을 해줘야 한다. 여기서 plus_two는 함수 이름이 아니라, 변수의 이름이다. 
호출할 때는 해당 변수명을 이용해서 값을 넣어주면 된다.

- **이 람다 함수는 어떤 내장 함수의 인자로 유용하게 사용될 수 있다.**
```python
def plus_one(x):
    return x+1

a = [1,2,3]
print(list(map(plus_one, a)))

[2, 3, 4]
```
- 위의 예시를 보면, 먼저 plus_one이라는 함수를 정의하고, map 함수에서 사용하게 된다. 그런데, 이 상황에서 함수를 따로 정의하지 않고 map 함수에서 바로 함수를 표현할 수 있는 방법이 바로 람다 함수이다.

```python
a = [1,2,3]
print(list(map(lambda x: x+1, a)))

[2,3,4]
```
- 이렇게 한 줄로 표현할 수 있다.

<br>

### 특정 숫자가 소수인지 확인하는 함수
```python
def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

a = [12,13,7,9,19]

for x in a:
    if isPrime(x):
        print(x, end=' ')
```
- 이렇게 2부터 해당 숫자 전까지 하나씩 나눠보면서 딱 떨어지는 수가 하나라도 있다면 소수가 아니니까 False를 리턴한다. 만약 2부터 해당 숫자 전까지 모두 딱 떨어지지 않는다면 소수가 맞기 때문에 for문이 끝나는 인덱스에 True를 리턴한다. 이 함수를 이용해 a리스트에서 하나씩 빼면서 소수일때만 출력해줄 수 있다.

<br>

### 함수의 return
```python
def add(a, b):
    c = a + b
    return c

x = add(3,2)
print(x)
```
- 위와 같은 코드가 있을 때, return은 함수가 호출되었을 때 값을 리턴하면서 함수를 종료시키는 역할도 한다.

```python
def add(a, b):
    c = a + b
    d = a - b
    return c, d
print(add(3,2))

(5, 1)
```
- 이렇게 2개의 값을 동시에 반환할 수도 있다. 그러면 튜플 자료구조로 리턴된다.

<br>

### 2차원 리스트 생성과 접근
```python
a = [[0]*3 for _ in range(3)]
print(a)

[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```
- 위와같이 작성하면, 반복문이 3번 반복하면서 [0]*3를 3번 실행하는 것이다. 그러면 2차원 리스트가 생긴다.
<img width="256" alt="Pasted Graphic 1" src="https://user-images.githubusercontent.com/95380638/187040464-67f2e7bd-cff8-4569-a80b-0d74fe4fedd7.png">

- 그리고 2차원 리스트는 이렇게 표로 이해하는 것이 좋다. 행번호와 열번호를 기억하자. 그래서 [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 이 2차원 리스트에 첫번째인 [0,0,0]은 표에서 0번 행을 의미한다. 그래서 a[0][1] = 1은 0행과 1열을 의미한다.

```python
for x in a:
    print(x)

[0, 1, 0]
[0, 2, 0]
[0, 0, 0]
```
- 이렇게 출력할 수 있다.

```python
a = [[0]*3 for _ in range(3)]
for x in a:
	for y in x:
		print(y, end=‘ ‘)
	print()
 
0 1 0 
0 2 0 
0 0 0 
```
- 그리고 2차원 리스트의 값들을 리스트가 아닌 하나하나 접근하고 싶을 때는 x가 1차원 리스트이니까 거기에서 원소를 하나씩 접근해주면 된다.

<br>

### 튜플에 있는 원소 값에 접근하기
```python
a = (1,2,3,4,5)
print(a[0])

1
```
- 튜플도 리스트와 마찬가지로 인덱스로 값에 접근할 수 있다. 리스트와 다른 점은, a[0] = 7 이렇게 특정 값을 다른 값으로 할당하고 싶다고해도 되지 않는다. 즉, 튜플 값은 절대 변경이 불가능하다.

<br>

### 리스트 값들을 랜덤으로 섞기
```python
import random as r

a = list(range(1, 11))
r.shuffle(a)
print(a)

[4, 1, 3, 10, 9, 7, 5, 8, 2, 6]
```
- random 모듈안에 있는 shuffle를 사용

<br>

### 리스트 관련 내장함수 clear
```python
a = list(range(1, 11))
a.clear()
print(a)

[]
```
- clear() 함수를 사용하면 리스트 요소들을 전부 제거해준다.

<br>

### 리스트 관련 내장함수 remove
```python
a = [1,2,3,4,5]
a.remove(4)
print(a)

[1, 2, 3, 5]
```
- remove 함수에 값을 넣으면, 해당 값을 리스트에서 찾아서 삭제해준다.

<br>

### 리스트 관련 내장함수 pop
```python
a = [1,2,3,4,5]
a.pop()
print(a)

[1,2,3,4]

b = [1,2,3,4,5] 
b.pop(0)
print(b)

[2, 3, 4, 5]
```
- 이렇게 pop은 리스트 맨 뒤의 요소를 하나 뺀다. 

<br>

### 리스트 관련 내장함수 insert
```python
a = [1,2,3,4,5]
a.insert(3, 7)
print(a)

[1, 2, 3, 7, 4, 5]
```
- insert는 특정 인덱스 지점에다가 어떤 값을 넣는 함수이다. 위의 예시에서는 3번 인덱스에 7이 들어가는 것이다.

<br>

### 리스트 합치기
```python
a = [1,2,3]
b = [3,4,5]
print(a+b)

[1, 2, 3, 3, 4, 5]
```

<br>

### 특정 아스키번호에 대응되는 알파벳 문자열을 반환하는 chr 함수
```python
tmp = 65
print(chr(tmp))

A
```

<br>

### 특정 알파벳 문자열의 아스키번호를 반환하는 ord 함수
```python
tmp = ‘AZ’
for x in tmp:
	print(ord(x))

65
90

tmp = 'az'
for x in tmp:
    print(ord(x))

97
122
```
- ord() 함수는 특정 문자열의 아스키번호를 출력해준다. 아스키번호는 대문자 A부터 Z까지 65부터 90를 의미한다. 그리고 소문자 a부터 z는 97부터 122를 의미한다.


### 알파벳일 경우에만 True 반환하는 isalpha 함수
```python
Ex1 = 'A'
Ex2 = '100'
print(Ex1.isalpha())
print(Ex2.isalpha())

True
False
```

<br>

### 특정 문자열이 대문자인지 소문자인지 확인하는 isupper와 islower 함수
- **isupper()는 대문자이면 True 반환, islower()는 소문자이면 True 반환**
```python
msg = "It is Time"
for x in msg:
	if x.isupper():
		print(x)

I T

msg = "It is Time"
for x in msg:
	if x.islower():
		print(x)

t i s i m e
```

<br>

### 리스트 인덱스 관련
- **A = [1,2,3,4] 가 있으면, A[:2]는 인덱스 0,1에 해당하는 값이 출력된다. 즉 리스트의 제일 처음부터 1번까지만 추출해 내는 것이다.**

<br>

### 문자열 관련 find와 count 함수
- **find 함수는 문자열에서 찾고자 하는 문자열의 인덱스 번호를 출력해준다**
```python
msg = "It is Time"
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))

IT IS TIME
1
2
```
- 중복되는 문자열이 여러개있으면 처음 발견되는 인덱스 번호를 출력해준다. 
- array.count(i) / 리스트에서 i라는 요소의 개수를 출력한다.

<br>

### 문자열을 전부 대문자 혹은 소문자로 바꾸는 upper와 lower 함수
```python
msg = "It is Time"
M = msg.upper()
m = msg.lower()
print(M)
print(m)

IT IS TIME
it is time
```
- 원본인 msg는 그대로 있고 새로운 값을 만들어주는 것이다. 

<br>

### 2중 for문으로 별 5개부터 1개 출력하기
```python
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()
```

<br>

### N의 약수 출력하기
```python
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
```

<br>

### for와 else 구문 그리고 break
```python
for i in range(1, 11):
	print(i)
	if i == 5:
		break
else:
	print(11)
```
- 위의 경우, for문이 1부터 10까지 빼서 출력하다가 if i == 5에서 브레이크를 수행한다. 이렇게 정상적인 종료를 하지 않고 중간에 브레이크를 당해 끝내버리면, else를 실행시키지 않는다. 근데 만약 for문이 정상적으로 브레이크를 당하지 않고 정상 종료를 했다면, 마지막에 else 밑에 있는 코드들을 실행시킨다.
- 위와같이 for문을 중지하고 싶을 때는 break를 사용한다.

<br>

### range로 10부터 1까지 출력하기
```python
for i in range(10, 0, -1):
	print(i)
```
- 이렇게 하면 10부터 1까지 출력된다.

<br>

### range를 변수로 리스트 만들기
```python
a = range(10)
print(list(a))

[0,1,2,3,4,5,6,7,8,9]
```

<br>

### if elif else문은 하나의 문장 구조
```python
x = 93
If x >= 90:
	print(‘A’)
elif …
	print(‘B’)
…
else:
	print(‘F’)
```
- 위에서는 도중에 조건이 맞으면 print 함수를 실행시키고 하나의 문장이 끝난다.

```python
x = 93
if x >= 90:
	print(‘A’)
If x >= 80:
	print(‘B’)
If x >= 70:
	print(‘C’)

A
B
C
```
- 근데, 위와 같은 경우는 여러 개의 문장 구조가 있는 경우이다. 이렇게 되면 3개의 문장구조가 있는 것이라서 각자 따로 If문이니까 조건이 맞으면 다 print를 하게 된다.

<br>

### 실수와 정수 더하면 Type은 실수형
```python
a = 4.3
b = 5
c = a+b
print(type(c))

float
```
- 실수는 정수를 포함하고 있는 더 넓은 범위이다. 그래서 더 넓은 범위로 연산결과가 나온다.

<br>

### List Comprehension
  - 코드 한 줄로 기존 list에서 원하는 조건을 충족하는 값으로 이루어진 새로운 list 만들기
```python
# [ 변수 for 변수 in 기존리스트 if 조건]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenlist= [i for i in list if i%2 == 0]
print(evenlist)

# 다르게 활용하는 경우
visited = [False for i in range(3)]
print(visited)


[2, 4, 6, 8, 10]
[False, False, False]
```

<br>

### zip 함수를 이용해 같은 인덱스에 해당하는 요소들을 뽑기
```python
numbers = [1,2,3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

(1, 'A')
(2, 'B')
(3, 'C')

# letters = "ABC" 라고 해도 같은 결과가 나온다.
```
- [관련 블로그](https://www.daleseo.com/python-zip/)

<br>

### 값 교환하기
```python
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

10 20
20 10
```

<br>

### if else나 for else는 같은 인덴트로 작성하고 다른 문의 경우에는 한 인덱스 들여쓰고 쓰는 예시

```python
if … :

else:

while

  break

for ..

else:

def

  return
```

<br>

### append와 extend 차이점
  - a = [1,2,3]이고 b = [3,4,5]일 때, a.append(b)는 a = [1,2,3,[3,4,5]] / a.extend(b)는 a = [1, 2, 3, 3, 4, 5] 가 된다.
  - [관련 블로그](https://m.blog.naver.com/wideeyed/221541104629)

<br>

### 해시에서 key만 따로 value만 따로 선택할 수 있게 해주는 keys와 values함수
```python
map = {'Seoul': 10, 'Tokyo': 20}
for city in map.keys():
    print(city)
for score in map.values():
    print(score)

Seoul
Tokyo
10
20
```

<br>

### 해시에서 key와 value를 동시에 선택할 수 있게 해주는 items 함수
```python
hash_map = {"seoul": 1, "Tokyo": 2}
for k, v in hash_map.items():
    print(k, v)

seoul 1
Tokyo 2
```

- **또한, items 함수를 이용해서 특정 value가 어떤 key를 가지는지 찾을 수 있다.**
```python
hash_map = {"seoul": 1, "Tokyo": 2}
a = [k for k,v in hash_map.items() if v == 1]
print(a)

['seoul']
```

- [관련 블로그](https://blog.naver.com/wideeyed/222007663089)

<br>

### 문자열에 0을 채우는 방법으로 rjust 함수 사용하기
  - ex) ‘Hello’.rjust(7, “0”) 이렇게 하면 문자열이 원하는 길이인 7이 될 때까지 문자열 왼쪽에 원하는 문자인 “0”를 추가 / 그래서 00Hello가 출력된다.
  - [관련 블로그](https://www.delftstack.com/ko/howto/python/pad-string-with-zeros-in-python/)

<br>

### format 함수 문자열 포맷팅으로 변수들을 이용해서 하나의 문자열로 조합하는 방법
  - ex) file = "{0}{1}.{2}".format(key, str(j+1).rjust(k,'0'), ext)
  - item = 'Hello {1}. count: {0}'.format(10, 'Jim') => 'Hello Jim. count: 10'
  - [관련 블로그](https://brownbears.tistory.com/421)

<br>

### 리스트의 마지막 요소 값 출력하기
  - a = [1,2,3,4,5], print(a[-1]) => 5

<br>

### strip 함수 관련 내용
  - item = '  apple ' / item.strip(' ') 이렇게 했을 때, apple 이렇게 문자열의 양 옆 공백을 제거해주는 역할.
  - str2 = "Welcome to Entity05", after_strip1 = str2.strip("05"), print(after_strip1) => Welcome to Entity 이렇게 문자열 매개변수가 지정되는 경우, 문자가 일치하면 문자열의 시작 또는 끝에 있는 문자가 원래 문자열에서 제거되고 나머지 문자열이 반환된다.
  - [관련 블로그](https://www.entity.co.kr/entry/Python-String-strip-%ED%95%A8%EC%88%98-strip-%ED%95%A8%EC%88%98%EC%9D%98-%EC%A0%95%EC%9D%98)
 
 <br>
 
 - **rstrip(), lstrip() 함수**
   - strip 함수와 마찬가지로 인자를 전달하지 않으면 문자열에서 공백을 제거해주는데, rstrip()의 경우 오른쪽의 공백을 제거해주고 lstrip()의 경우 왼쪽의 공백을 제거해준다.
   - 인자를 전달한다면, 그 인자와 동일한 문자를 각각 오른쪽에서, 왼쪽에서 제거해준다.
 
 ```python
 text = ' Water boils at 100 degrees '
print('[' + text.rstrip() + ']')
print('[' + text.lstrip() + ']')
print('[' + text.strip() + ']')

[ Water boils at 100 degrees]
[Water boils at 100 degrees ]
[Water boils at 100 degrees]
```

- [관련 블로그](https://codechacha.com/ko/python-string-strip/)

 <br>
 
### all 함수란
  - all(iterable) 함수는 인자로 받은 반복 가능한 자료형(iterable)의 모든 요소가 참(True)이면 참(True)을 반환하는 함수
  - and의 특징을 가졌으며, 인자로 받은 요소중 하나라도 False이면 False를 반환하고 인자로 받은 요소가 비어있으면 True이다.
  - 리스트, 튜플, 집합, 딕셔너리, 문자열이 변수가 될 수 있다.
  - [관련 블로그](https://blockdmask.tistory.com/430)

```python
a = [23, 12, 36, 53, 19]
if all(60>x for x in a):
    print("YES")
else:
    print("NO")

YES
```
- 이렇게 하면 a라는 리스트에서 하나씩 뽑고 하나씩 60>x이라는 조건을 비교해서 True인지 False인지 판단하게 된다. 그래서 모든 요소가 참이면 all() 함수는 True를 리턴하게 된다. 하나라도 거짓이 된다면 all() 함수는 거짓을 리턴하게 된다.

<br>

### any 함수란
  - any(iterable) 함수는 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참(True)이 있으면 참(True)를 반환하는 함수
  - or의 특징을 가졌으며, 인자로 받은 요소중 하나라도 True이면 True를 반환하고 인자로 받은 자료형이 비어있는 경우 False를 반환한다.
  - 리스트, 튜플, 집합, 딕셔너리, 문자열이 변수가 될 수 있다.
  - [관련 블로그](https://blockdmask.tistory.com/430)

```python
a = [23, 12, 36, 53, 19]
if any(15>x for x in a):
    print("YES")
else:
    print("NO")

YES
```
- 같은 예제에서 any()라는 함수를 이용하면, 15>x 라는 조건을 a 리스트의 요소 중 하나라도 만족해서 True가 나온다면 any() 함수는 True를 리턴하게 된다. 모든 요소가 거짓이라면 그 때는 False를 리턴하게 된다.

<br>

### 리스트 요소의 인덱스를 확인하는 index 함수
- 중복되는 요소들이 있다면 가장 처음 나온 요소의 인덱스를 반환한다.
- L = [1,2,2,4,5], L.index(4) = 3, L.index(2) = 1

<br>

### 리스트를 만드는 다른 방법
- **result = [0] * len(A)** 이렇게 해야 [0, 0, 0, …] 이렇게 될 수 있다.

<br>

### 10진수 숫자를 이진수 문자열로 돌려주는 bin 함수
- bin(number) 이렇게 전달받은 integer 혹은 long integer 자료형의 값인 10진수 숫자를 이진수(binary) 문자열로 돌려주는 함수이다.
- print(bin(1041))하면, 0b10000010001 이렇게 출력됨

```python
a = bin(10234)
b = a[2:]

print(a)
print(b)

0b10011111111010
10011111111010
```
- [관련 블로그](https://iambeginnerdeveloper.tistory.com/114)

<br>

### 리스트 요소 순서 거꾸로 하기
- stack = [5, 2, 3, 1]일 때, print(stack[::-1]) 하면 [1, 3, 2, 5]

<br>

### for문으로 범위 설정하기
- **for i in range(~, ~)** / 범위 for문

- **for _ in range(n+1)** / 데이터 n개 for문

- **for i in range(1, m+1)** / 1부터 m까지 for문으로 뽑기

<br>

### max와 min 함수
- **max(~, ~)** / 둘 중 최댓값, **min(~, ~)** / 둘 중 최솟값
```python
print(min(7, 5))
print(max(7, 5))

5
7
```
- min 함수는 들어간 여러 개 인자 중 가장 작은 값을 출력해준다. max() 함수는 반대이다.

<br>

### map 함수 사용하기
- **map(적용할 함수, 반복 가능한 자료형)**
  - map 함수를 활용하면 모든 반복가능 자료형 데이터 각각에 함수를 적용시킬 수 있다.

- **array = [1,2,3,4]가 있을 때, 모든 요소들을 문자열로 만들고 싶다면 map(str, array) 이렇게 해주면 된다.**
  - ex) array = [1,2,3,4], print(list(map(str, array))) 라고 입력하면 ['1', '2', '3', '4']

- **n, m = map(int, input().split())** / 숫자들을 공백 기준으로 따로 변수에 저장

- **data = list(map(int, input().split()))** / 숫자들을 공백 기준으로 입력받고 리스트로 저장

<br>

### 해당 매개변수가 지정한 타입이 맞는지 확인하는 isinstance 함수
- **isinstance(1.2, float)** / 해당 매개변수가 지정한 타입이 맞는지 확인하는 함수
  - [관련 블로그](https://brownbears.tistory.com/155)

<br>

### 문자열을 split를 이용해 나누게 되면 리스트 형태
- **string = "Hello World!", string3 = string.split(' '), print(string3) 하게되면 ['Hello', 'World!']** / 문자열을 split를 이용해 나누게 되면 리스트 형태가 된다.
  - [관련 블로그](https://wikidocs.net/2839)

<br>

### 인덱스와 함께 요소들을 뽑아낼 수 있는 enumerate 함수
```python
a = [23, 12, 36, 53, 19]
for x in enumerate(a):
	print(x, end=' ')

(0, 23) (1, 12) (2, 36) (3, 53) (4, 19)
```
- enumerate 함수를 사용해서 인덱스와 값이 함께 들어간 튜플형태로 만들 수 있다. 튜플이니까 아래와 같이 할 수도 있다.

```python
a = [23, 12, 36, 53, 19]
for x in enumerate(a):
	print(x[0], x[1])

0 23
1 12
2 36
3 53
4 19
```

<br>

- **for idx, answer in enumerate(answers):** / enumerate 함수를 사용해서 자료형에서 인덱스와 함께 요소들을 뽑아낼 수 있다.
```python
a = [23, 53, 12, 36, 19]
for idx, x in enumerate(a):
    print(idx, x)

0 23
1 53
2 12
3 36
4 19
```

- [관련 블로그](https://hckcksrl.medium.com/python-enumerate-b19ad6b94c00)

<br>

### 리스트 슬라이싱
- **array[1:5]** 이렇게 슬라이싱하면, 인덱스 1부터 4까지 슬라이싱된다.
  - ex) my_list = [“Mitch”, [3,6,7], [“yellow”, 5, 6]] 라고할 때, my_list[1][1:3]이면 -> [6,7] 슬라이싱

<br>

### sort 함수와 sorted 함수
- **리스트를 정렬할 때 사용하는 sort 함수와 sorted 함수의 차이점**
  - sort 함수는 리스트명.sort() 형식으로 리스트의 원본값을 직접 수정하며 리턴값이 None이다. 기본적으로 오름차순 정렬을 진행한다.
  - sorted 함수는 sorted(리스트명) 형식으로 리스트의 원본값은 그대로이고 새로운 리스트를 만들어 정렬값을 반환한다.
  - [관련 블로그](https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=wideeyed&logNo=221745416992&redirect=Dlog&widgetTypeCall=true&directAccess=false)

- **sort, sorted 모두 key, reverse 매개변수를 갖고 있다**
  - reverse는 bool값을 넣어준다. False이면 오름차순 / True이면 내림차순으로 정렬할 수 있다.
  - key는 정렬을 목적으로 하는 함수를 값으로 넣어주면 된다. lambda를 이용할 수 있다. 즉, key값을 기준으로 정렬이 되고 기본값은 오름차순이다.
  - [관련 블로그](https://ooyoung.tistory.com/59)
```python
>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> print(sorted(str_list, key=len))  # 함수
['굿모닝', '좋은하루', 'niceday', 'good_morning']

>>> print(sorted(str_list, key=lambda x : x[1]))  # 람다
['niceday', 'good_morning', '굿모닝', '좋은하루']
# lambda x 에서 x는 리스트의 요소 1개를 의미
```

<br>

### global 사용하기
- 함수밖에서 선언되는 변수를 “전역 변수”라고 하는데, 그 전역 변수의 값을 함수 안에서 변경하려면 global이라는 키워드를 사용해서 선언해주면 변경할 수 있다.
  - [관련 블로그](https://codingpractices.tistory.com/entry/Python-%EC%A0%84%EC%97%AD-%EB%B3%80%EC%88%98-%EC%A7%80%EC%97%AD-%EB%B3%80%EC%88%98-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%B4%9D-%EC%A0%95%EB%A6%AC-global-nonlocal)

- 참고로 **local**은 함수내에서 사용하는 "지역 변수"이다.
- 또한, **non local**은 함수 a가 있고 그 내부에 함수 b가 있을 때 b한테 함수 a의 공간을 의미한다. 그래서, 함수 b 내부에서 함수 a의 지역변수를 가져올 때는 non local 키워드를 사용한다.

<br>

### 병합 연산자 사용하기
- |= 연산자 사용하기
  - 병합 연산자로 union 즉, 합집합을 의미한다.
  - [관련 블로그](https://velog.io/@nayoon-kim/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%97%B0%EC%82%B0%EC%9E%90) 

<br>

### permutation 함수로 순열 만들기
- **itertools.permutation 함수로 순열 만들기**
  - 이 함수를 사용하면 for문을 사용하지 않고도 순열을 구할 수 있다
  - **순열이란, 조합과 다르게 순서가 중요하다. 대표적으로 총 5개의 카드에서 3장을 뽑아 3자리 숫자를 만들어 줄을 세우는 경우를 생각할 수 있다.**
  - [관련 블로그](https://school.programmers.co.kr/learn/courses/4008/lessons/12836)
```python
from itertools import permutations

pool = ['A', 'B', 'C']
print(list(map(''.join, permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, permutations(pool, 2)))) # 2개의 원소로 수열 만들기

['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
```

<br>

### 문자열 변수로 리스트를 만드는 list 함수
```python
n = "17"
print(list(n))

['1', '7']
```

<br>

### range 함수의 마지막 매개변수는 range의 간격을 지정
  - print(list(range(1, 11, 2))) / [1, 3, 5, 7, 9]
  - 이렇게하면 원래는 1부터 10까지 출력되지만, 간격이 2이기 때문에 1부터 2씩 증가된 수가 출력된다

<br>

### join 함수 사용하기
  - ‘구분자’.join(리스트) / 이러한 원형으로 매개변수로 들어온 리스트에 있는 요소 하나하나 사이에 구분자를 넣어서 하나의 문자열로 합쳐주는 함수이다. 구분자는 공백일 수도 있다. 
  - [관련 블로그](https://blockdmask.tistory.com/468)

<br>

### 루트 계산 관련
  - print(4 ** 0.5) / 2
  - 루트 4를 의미하니까 2가 출력된다

<br>

### 정수 연산 예시
- **12%1 = 0, 12//3 = 4, 12/3 = 4.0, 0%5 = 0, 1%5 = 1**

<br>

### 반복문에서 조건이 맞지 않을 때 반복문을 종료시키지 않고 맨 처음의 조건문으로 보내주는 continue
- **continue는 반복문에서 조건이 맞지 않을 때 반복문을 종료시키지 않고 맨 처음의 조건문으로 보내주는 역할을 한다.**
  - **pass는 어떤 조건문에 대해서 아무런 실행을 하지 않고 아래 코드를 이어서 실행하게 된다. 반면에 continue는 맨 처음 조건문으로 돌아가면서 아래 코드를 실행하지 않는다.**
  - [관련 블로그](https://securityspecialist.tistory.com/73)

<br>

### 문자열 반복하기
  - print("6"*3, "10"*3, "2"*3) / 666 101010 222

<br>

### 리스트에서 원하는 값 제거하는 방법
  - 리스트에 remove 함수 / 반복문 사용 / del 키워드 / pop 함수 / clear 함수를 이용해 원하는 값을 제거할 수 있다.
  - [관련 블로그](https://zeroaan.github.io/python/2020/05/02/Python-List%EC%97%90%EC%84%9C-%EC%9B%90%ED%95%98%EB%8A%94-%EA%B0%92-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0.html)

<br>

- **del 키워드 사용하기 - remove 함수는 원하는 값을 매개변수로 받아 삭제하지만 del 키워드는 인덱스를 입력 받아 삭제**
```python
>>> int_list = [1, 2, 3, 4, 5, 6, 7]
>>> str_list = ['가','나','다','라','마']

>>> del int_list[0]  # 한개의 요소를 삭제
>>> print(int_list)
[2, 3, 4, 5, 6, 7]

>>> del str_list[3:]  # 여러개의 요소를 삭제
>>> print(str_list)
['가', '나', '다']
```
- [관련 블로그](https://ooyoung.tistory.com/49)

<br>

### 주어진 문자열이 숫자로 되어있는지 검사하는 함수
- **isdecimal()**
  - 주어진 문자열이 0부터 9까지라면 True를 반환해주는 함수

- **isdigit()**
  - 주어진 문자열이 알파벳이 아닌 숫자형태라면 True를 반환해주는 함수. 2의 2승도 True로 반환해준다.

- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%ED%83%90%EC%83%89%EA%B3%BC%20%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98/%EC%88%AB%EC%9E%90%EB%A7%8C%20%EC%B6%94%EC%B6%9C.py)
- [관련 블로그](https://it-neicebee.tistory.com/33)
<br>

### while문 종료 조건 생각하기
- while문의 종료 조건이 헷갈린다면, 반대로 생각했을때가 while문이 종료되는 조건이다.
- ex) while p1 < n and p2 < m: 이면 -> p1이 n과 같거나 커지는 경우 또는 p2가 m과 같거나 커지는 경우, while문이 종료된다.
- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%ED%83%90%EC%83%89%EA%B3%BC%20%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98/%EB%91%90%20%EB%A6%AC%EC%8A%A4%ED%8A%B8%20%ED%95%A9%EC%B9%98%EA%B8%B0.py)

<hr>


### Ideas

- 📖 **Contents**
  - [계수요소](#계수요소)
    - [주어진 리스트의 요소들을 새로운 리스트를 만들어서 중복없이 담아내기](#주어진-리스트의-요소들을-새로운-리스트를-만들어서-중복없이-담아내기)
    - [주어진 리스트의 요소들이 1부터 N까지 1씩 증가하는지 확인하기](#주어진-리스트의-요소들이-1부터-n까지-1씩-증가하는지-확인하기)
    - [리스트를 정렬해서 리스트에는 없는 가장 작은 양의 정수를 찾기](#리스트를-정렬해서-리스트에는-없는-가장-작은-양의-정수를-찾기)
  - [시간복잡도](#시간복잡도)
    - [서로 다른 두 위치의 거리를 변수로 설정해서 가는 횟수 구하기](#서로-다른-두-위치의-거리를-변수로-설정해서-가는-횟수-구하기)
    - [1부터 1씩 커지는 요소가 들어있는 리스트에서 비어있는 요소 찾기](#1부터-1씩-커지는-요소가-들어있는-리스트에서-비어있는-요소-찾기)
    - [리스트 요소마다 절대값 적용하기](#리스트-요소마다-절대값-적용하기)
  - [배열](#배열)
    - [리스트 요소의 갯수가 홀수이고 쌍을 이룰 때 쌍을 이루지 않는 요소 찾기](#리스트-요소의-갯수가-홀수이고-쌍을-이룰-때-쌍을-이루지-않는-요소-찾기)
    - [주어진 리스트를 enumerate 함수로 인덱스와 값을 뽑고 해시에 key와 value로 정의하기](#주어진-리스트를-enumerate-함수로-인덱스와-값을-뽑고-해시에-key와-value로-정의하기)
  - [스택과 큐](#스택과-큐)
    - [while문으로 하루씩 지나갈 때 완료된 업무 개수 증가시키고 리스트에서 pop 진행](#while문으로-하루씩-지나갈-때-완료된-업무-개수-증가시키고-리스트에서-pop-진행)
    - [while문 안에 for문 설정하기](#while문-안에-for문-설정하기)
  - [완전탐색](#완전탐색)
    - [dx 리스트와 dy 리스트로 좌표 정의하기](#dx-리스트와-dy-리스트로-좌표-정의하기)
    - [루트 제곱근 계산 하기](#루트-제곱근-계산-하기)
    - [리스트의 요소가 주기를 가지고 계속 반복될 때 특정 인덱스가 가리키는 요소 확인하기](#리스트의-요소가-주기를-가지고-계속-반복될-때-특정-인덱스가-가리키는-요소-확인하기)
    - [1부터 주어진 수까지 소수 구하기](#1부터-주어진-수까지-소수-구하기)
    - [문제에서 주어진 사각형이 격자로 이루어져 있을 때 식 만들기](#문제에서-주어진-사각형이-격자로-이루어져-있을-때-식-만들기)
  - [정렬](#정렬)
    - [로또 번호 일치 개수를 리스트의 인덱스라고 생각하기](#로또-번호-일치-개수를-리스트의-인덱스라고-생각하기)
    - [for문으로 2차원 배열의 리스트 1개씩 뽑기](#for문으로-2차원-배열의-리스트-1개씩-뽑기)
    - [문자열로 되어있는 숫자들이 들어있는 리스트 정렬하기](#문자열로-되어있는-숫자들이-들어있는-리스트-정렬하기)
    - [리스트 오름차순 정렬 후 총 개수에서 특정 인덱스를 차감하면 해당 인덱스 요소를 포함한 남은 요소 개수가 된다](#리스트-오름차순-정렬-후-총-개수에서-특정-인덱스를-차감하면-해당-인덱스-요소를-포함한-남은-요소-개수가-된다)
    - [슬라이싱으로 문자열 순서 뒤집기](#슬라이싱으로-문자열-순서-뒤집기)
    - [오름차순 정렬을 진행한 리스트에서 가장 큰 수는 리스트의 마지막 요소](#오름차순-정렬을-진행한-리스트에서-가장-큰-수는-리스트의-마지막-요소)
  - [해시](#해시)
    - [주어진 리스트 요소들의 중복을 제거하기 위해 해시를 사용할 수 있다](#주어진-리스트-요소들의-중복을-제거하기-위해-해시를-사용할-수-있다)
    - [주어진 리스트 요소들의 중복을 제거하기 위해 set 함수를 사용할 수 있다](#주어진-리스트-요소들의-중복을-제거하기-위해-set-함수를-사용할-수-있다)
    - [해시 딕셔너리에 특정 키가 있는지 확인하기](#해시-딕셔너리에-특정-키가-있는지-확인하기)
    - [리스트에 특정 값이 있는지 없는지 확인하기](#리스트에-특정-값이-있는지-없는지-확인하기)
    - [리스트가 여러 개 있을 때 모든 리스트들을 sort해서 비교할 생각하기](#리스트가-여러-개-있을-때-모든-리스트들을-sort해서-비교할-생각하기)
    - [문제에서 주어진 리스트 요소들을 해시 딕셔너리에 value가 1이 되게끔 추가해서 문제풀기](#문제에서-주어진-리스트-요소들을-해시-딕셔너리에-value가-1이-되게끔-추가해서-문제풀기)
    - [빈 문자열을 변수로 지정하고 해당 변수에 한 문자열씩 더해서 문제풀기](#빈-문자열을-변수로-지정하고-해당-변수에-한-문자열씩-더해서-문제풀기)
    - [해시의 모든 키에서 값을 선택하는 경우의 수 구하기](#해시의-모든-키에서-값을-선택하는-경우의-수-구하기) 
  - [DFS와 BFS](#dfs와-bfs)
    - [함수에서 return 공백으로 재귀함수 1개 취소하기](#함수에서-return-공백으로-재귀함수-1개-취소하기)
    - [1문제를 DFS 또는 BFS로 푸는 예시](#1문제를-dfs-또는-bfs로-푸는-예시)
    - [방문여부를 확인하기 위한 리스트를 list comprehension으로 설정하기](#방문여부를-확인하기-위한-리스트를-list-comprehension으로-설정하기)
  - [ETC](#etc)
    - [주어진 이진수 사이에 있는 0의 개수 계산하기](#주어진-이진수-사이에-있는-0의-개수-계산하기)
    - [CSV 형태와 같은 데이터 파싱 문제](#csv-형태와-같은-데이터-파싱-문제)
    - [리스트의 인덱스를 어떤 수들의 합이라고 생각하기](#리스트의-인덱스를-어떤-수들의-합이라고-생각하기)
    - [어떤 수가 주어졌을 때 그 수의 자릿수의 합을 구하기](#어떤-수가-주어졌을-때-그-수의-자릿수의-합을-구하기)
    - [어떤 숫자가 주어질 때 1부터 그 숫자까지의 범위안에 소수 구하기](#어떤-숫자가-주어질-때-1부터-그-숫자까지의-범위안에-소수-구하기)
    - [어떤 숫자가 주어질 때 그 숫자를 뒤집은 숫자를 만들기](#어떤-숫자가-주어질-때-그-숫자를-뒤집은-숫자를-만들기)
    - [특정 숫자가 소수인지 아닌지 확인하기](#특정-숫자가-소수인지-아닌지-확인하기)
    - [가산점을 고려한 총 점수를 계산하기](#가산점을-고려한-총-점수를-계산하기)
    - [리스트 인덱스가 없는 경우 예외처리 하기](#리스트-인덱스가-없는-경우-예외처리-하기)
    - [리스트에서 처음과 끝 요소 비교하기](#리스트에서-처음과-끝-요소-비교하기)
    - [리스트 요소 하나씩 꺼내서 자연수 만들기](#리스트-요소-하나씩-꺼내서-자연수-만들기)
    - [리스트에서 하나씩 뽑을 때 앞에 요소를 뽑고 해당 요소 바로 뒤부터 뽑기](#리스트에서-하나씩-뽑을-때-앞에-요소를-뽑고-해당-요소-바로-뒤부터-뽑기)
    - [리스트 인덱스를 가리키는 2개의 변수를 생성해서 연속적인 리스트 요소들의 합을 구하기](#리스트-인덱스를-가리키는-2개의-변수를-생성해서-연속적인-리스트-요소들의-합을-구하기) 
   

<br>

## 계수요소

### 주어진 리스트의 요소들을 새로운 리스트를 만들어서 중복없이 담아내기
- 해당 문제에서는 => A라는 리스트의 가장 큰 수가 X라고 할 때, B라는 리스트를 새롭게 생성하고 A 리스트의 요소들을 중복없이 담아내면, B 리스트 요소의 총합과 sum(range(1, X+1))의 값이 같게 된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/%EA%B3%84%EC%88%98%EC%9A%94%EC%86%8C/FrogRiverOne.py)

<br>

### 주어진 리스트의 요소들이 1부터 N까지 1씩 증가하는지 확인하기
- A라는 리스트가 N개의 요소가 있을 때, 해당 리스트가 [1,2,3, …N]이 되는지 확인하는 문제 - A의 합과 / 1부터 A의 개수인 숫자까지 더한 값이 같다면, 조건에 맞는 리스트가 맞다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/%EA%B3%84%EC%88%98%EC%9A%94%EC%86%8C/PermCheck.py)

<br>

### 리스트를 정렬해서 리스트에는 없는 가장 작은 양의 정수를 찾기
- 리스트 A에는 없는 가장 작은 양의 정수를 반환하는 문제 - 먼저 sort()로 오름차순 정렬을 한 다음, A = list(set(A)) 이렇게 set으로 중복을 제거. 그리고 missingdata = 1 이렇게 처음에는 없는 양의 정수를 1로 고정시킨 상태에서 A 리스트의 요소를 하나씩 빼서 missingdata와 비교하기. 만약 같다면 missingdata를 1씩 올려주고 같지 않다면 그 때 시점의 missingdata가 리스트에 없는 가장 작은 양의 정수가 된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/%EA%B3%84%EC%88%98%EC%9A%94%EC%86%8C/MissingInteger.py)


<br>

## 시간복잡도

### 서로 다른 두 위치의 거리를 변수로 설정해서 가는 횟수 구하기
- X라는 위치에서 Y라는 위치까지 D씩 뛰어서 가는 방법을 구할 때, Y-X를 distance라는 변수로 두고 distance % D가 0이라면 distance // D 의 값인 X가, D가 몇번 반복되면 되는지 알려준다. 그리고 나눈 나머지보다 D가 더 크다면 정답은 X+1번이 된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84/Frogjmp.py)

<br>

### 1부터 1씩 커지는 요소가 들어있는 리스트에서 비어있는 요소 찾기
- 리스트 A가 범위가 1부터 시작해서 1씩 커지고 n개를 가지고 있을 때, 순서에서 비어있는 1개의 원소를 찾는 것이 목표인 문제
  - 원소가 없는 A 리스트일 경우에는 1을 return 값으로 주고, 만약 리스트 A의 개수가 현재 4개라면 1개가 비었으니 원래 리스트 A의 개수는 5개이어야 한다.
  - 따라서 result = sum(range(1, len(A)+2)) - sum(A) 이렇게 1부터 5까지를 더한 수에서 - 현재 리스트 A를 다 더한 수를 빼주면 비어있는 수를 알 수 있게 된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84/PermMissingElem.py)

<br>

### 리스트 요소마다 절대값 적용하기
- answer = list(map(abs, result_list)) ==> 이런식으로 리스트 요소마다 절대값을 적용할 수 있다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84/TapeEquilibrium.py)
  - [관련 블로그](https://blockdmask.tistory.com/380)

<br>

## 배열

### 리스트 요소의 갯수가 홀수이고 쌍을 이룰 때 쌍을 이루지 않는 요소 찾기
- 리스트 요소의 갯수가 홀수이고 쌍을 이루는 요소들이 있을 때, 정렬을 해서 2개씩 뽑다보면 처음 뽑은 수가 쌍을 이루지 않는 하나의 요소가 될 수 있다. 그래서 2개씩 뽑을 때, 그 2개가 다르다면 첫번째가 쌍을 이루지 않는 요소가 된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/%EB%B0%B0%EC%97%B4/OddOccurrencesInArray.py)
  - [관련 블로그](https://smecsm.tistory.com/205)

<br>

### 주어진 리스트를 enumerate 함수로 인덱스와 값을 뽑고 해시에 key와 value로 정의하기
- 주어진 리스트를 enumerate 함수를 사용하여 인덱스와 값을 차례대로 뽑은 다음, hash_map = {}에 key와 value로 정의. 그 다음, 해당 hash_map의 key만 뽑을 수 있는 keys() 함수를 이용해 새로운 리스트를 정의할 수 있다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/%EB%B0%B0%EC%97%B4/CyclicRotation.py)

<br>

## 스택과 큐
- **문제 특징**
  - 리스트 요소마다 진행되는 속도가 서로 다르다.
  - 대기목록 리스트가 있고 우선순위에 따라 순서가 달라질 수 있다.
  - while이나 for문으로 진행되다가 특정 if문 조건을 만족하면 리스트에서 pop를 사용할 수 있다.
  - while문 안에 if문 또는 while문 안에 for문으로 시작하는 경우가 있다.

<br>

### while문으로 하루씩 지나갈 때 완료된 업무 개수 증가시키고 리스트에서 pop 진행
- while문을 사용해서 하루씩 증가할 때 완료된 모든 업무의 개수를 count + 이미 들어가있는 리스트에서 완료될때마다 pop(0) 진행 > 자료구조 큐 생각하기
  - pop()을 하게 되면 while로 리스트의 요소가 있을 경우에만 진행되도록 설정하기
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%8A%A4%ED%83%9D%EA%B3%BC%20%ED%81%90/%EA%B8%B0%EB%8A%A5%EA%B0%9C%EB%B0%9C.py)

<br>

### while문 안에 for문 설정하기
- 우선순위와 관련된 문제를 while문 안에있는 for문으로 구하는 과정
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%8A%A4%ED%83%9D%EA%B3%BC%20%ED%81%90/%ED%94%84%EB%A6%B0%ED%84%B0.py) 

<br>

## 완전탐색
- **문제 특징**
  - 코드를 작성할 때, 여러 변수들을 리스트로 정의해서 요소들을 미리 나열해서 푸는 경우가 많다.
  - 문제에 일정한 패턴이 존재할 수 있다.
  - enumerate 함수를 사용할 수 있다.
  - 한 문제에서 for문을 여러 개 사용할 수 있다.
  - set(), 즉 집합의 특성을 생각해볼 수 있다.
  - 모르는 특정 변수를 for 변수 in range로 1부터 수를 대입해서 맞는 조건을 찾을 수 있다.

<br>

### dx 리스트와 dy 리스트로 좌표 정의하기
- dx = [0, 1, 0, -1] dy = [-1, 0, 1, 0] / 서남동북 행과 열 표시
- nx = x + dx[i] ny = y + dy[i] / (x, y)에서 좌표이동

<br>

### 루트 제곱근 계산 하기
- 루트 제곱근 계산 방법
  - x를 제곱하여 a가 되었다면, x를 a의 제곱근이라고 부른다. 수학 라이브러리인 Math를 이용해서 제곱근을 구할 수 있다.
  - 또한, print(4 ** 0.5) = 2.0 이렇게 어떤 수에 0.5를 제곱해서 구할 수 있다.
  - [관련 블로그](https://needneo.tistory.com/77)

```python
result = 4 ** 0.5
print(int(result))

2
```
<br>

### 리스트의 요소가 주기를 가지고 계속 반복될 때 특정 인덱스가 가리키는 요소 확인하기
- 어떤 리스트에 요소가 5개가 있고 그 5개가 순환주기로 계속 반복될 때 특정 인덱스가 어떤 요소를 가리키는지 확인해야 한다면, 인덱스 % 요소개수 = 인덱스 이렇게 구할 수 있다.
  - ex) pattern1 = [1, 2, 3, 4, 5] 일 때, 인덱스 6인 요소는 6 % len(pattern1) = 1이니까 6번째는 2가 된다.
  - 어떤 수를 x로 나누면 나머지는 무조건 x보다 작다. 그래서 특정 범위 내 숫자를 구할 때 자주 사용된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%99%84%EC%A0%84%ED%83%90%EC%83%89/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC.py)

<br>

### 1부터 주어진 수까지 소수 구하기
- **소수를 구하는 방법**
  - 소수란, 1과 자기 자신외의 약수를 가지지 않는 1보다 큰 자연수를 의미한다. 이론상으로 단일 숫자가 소수인지 판단하는 방법은, 숫자 n이 소수인지 알아보기 위해 2부터 n-1까지의 숫자를 반복하며, 나누어 떨어지는 숫자가 있는지 확인하고 만일 없다면, 소수가 된다.
  - 더 효율적으로 소수를 구하는 공식이 있는데, 바로 **에라토스테네스의 체**라는 방법이다.
    - 소수를 구하고자 하는 범위 2에서 n이 있을 때, 2~n의 제곱근에 해당하는 범위 안의 소수의 배수들을 계속 제외하면 결국 소수만 남는다는 이론이다.
    - ex) 이를테면 n=100일 때, 100까지의 소수를 구하고 싶다면, 2에서 100까지 숫자에서 -> 100의 제곱근이 10이니까 2~10까지의 범위 안에 소수의 배수인 2의 배수 제외, 3의 배수 제외, 5의 배수 제외, 7의 배수 제외를 진행한다는 것이다.
    - 밑에 관련 문제에서는 2부터 제곱근까지 있는 수의 배수를 전부 제외했다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%99%84%EC%A0%84%ED%83%90%EC%83%89/%EC%86%8C%EC%88%98%20%EC%B0%BE%EA%B8%B0.py)
  - [관련 블로그](https://velog.io/@jakeseo_me/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-14-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4)

<br>

### 문제에서 주어진 사각형이 격자로 이루어져 있을 때 식 만들기
- **문제에서 사각형과 그 안에 격자로 이루어져 있다면 ==> 사각형 가로 * 세로 = 갈색 격자 개수 + 노란색 격자 개수 라는 식을 세울 수 있다.**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%99%84%EC%A0%84%ED%83%90%EC%83%89/%EC%B9%B4%ED%8E%AB.py)

<br>

## 정렬
- **문제 특징**
  - 문제 자체에서 “정렬”이라는 단어가 나올 수 있다.
  - 리스트 정렬 과정에서 슬라이싱이 활용될 수 있다.
  - 리스트 정렬 과정에서 정렬 기준이 필요할 수 있다.
  - 리스트 정수 요소들을 문자열로 바꾸고, 특정 기준으로 정렬한 다음, join을 이용해서 이어 붙이는 문제가 있다.
  - 가장 큰 수나 가장 작은 수가 답이 될 수 있다.
  - 문제에 2차원 배열이 나올 수 있다.

<br>

### 로또 번호 일치 개수를 리스트의 인덱스라고 생각하기
- 로또 번호 순위 리스트에 미리 정의해놓기, 일치번호 개수와 불일치번호 개수로 나누기
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%A0%95%EB%A0%AC/%EB%A1%9C%EB%98%90%EC%9D%98%20%EC%B5%9C%EA%B3%A0%20%EC%88%9C%EC%9C%84%EC%99%80%20%EC%B5%9C%EC%A0%80%20%EC%88%9C%EC%9C%84.py)

<br>

### for문으로 2차원 배열의 리스트 1개씩 뽑기
- 2차원 배열에서 리스트 뽑기
  - 2차원 배열에서 리스트 뽑을 때는 for문을 사용하면 된다. ex) commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]] 일 때, for command in commands: i,j,k = command 이렇게하면 i = 2, j = 5, k = 3 이렇게 변수 지정 가능.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%A0%95%EB%A0%AC/K%EB%B2%88%EC%A7%B8%20%EC%88%98.py)

<br>

### 문자열로 되어있는 숫자들이 들어있는 리스트 정렬하기
- **문자형태의 숫자를 비교할 때 \*로 문자열의 길이를 늘려서 비교해볼 수도 있다**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%A0%95%EB%A0%AC/%EA%B0%80%EC%9E%A5%20%ED%81%B0%20%EC%88%98.py)
  - 문자열로 되어있는 숫자들이 들어있는 리스트를 정렬해보면, 아래처럼 문자열의 첫번째 인덱스 수가 크면 내림차순 시, 먼저 나온다. 그리고 첫번째 인덱스 수가 같으면 그 다음 인덱스를 비교한다. 없으면 더 인덱스가 많은 수가 큰 수가 된다.
  - 근데, 해당 문제에서는 이러면 안 된다. 그래서 문자열의 길이를 늘려서 비교해보는 것이다. 해당 문제는 리스트 원소가 1,000이하 이니까 * 3을 해준다. “3” 과 “300”과 “31”이 있을 때, “31”이 먼저 나오는 게 아니라 “3”이 먼저 나오게끔 해야되니까 문자열을 늘리는 것이다.
  - [관련 블로그](https://esoongan.tistory.com/103)
```python
# 문자열로 되어있는 숫자들이 들어있는 리스트 정렬
array = ["3","300","31","387"]
array.sort(reverse=True)
print(array)

['387', '31', '300', '3']

# 해당 문제를 위해 key를 이용한 정렬
array.sort(key = lambda x : x*3, reverse=True)
print(array)

['387', '3', '31', '300']
```

<br>

### 리스트 오름차순 정렬 후 총 개수에서 특정 인덱스를 차감하면 해당 인덱스 요소를 포함한 남은 요소 개수가 된다
- **리스트가 있을 때, 오름차순 정렬을 한 다음에 총 개수에서 특정 인덱스를 차감하면 -> 특정 인덱스 데이터 포함해서 남은 리스트 요소의 개수가 된다. 그리고 남은 리스트 요소들은 특정 인덱스 값보다 크다는 것을 알 수 있다.**
  - ex)정렬된 상태라고 생각하고 총 5개에서 인덱스 2를 빼면 -> 3이니까 인덱스 2 데이터 포함해서 뒤에 3개가 남아있다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%A0%95%EB%A0%AC/H-Index.py)

<br>

### 슬라이싱으로 문자열 순서 뒤집기

```python
string = 'Hello, World!'
reversed_str = string[::-1]

print(f'Original String: {string}')
print(f'Reversed String: {reversed_str}')

Original String: Hello, World!
Reversed String: !dlroW ,olleH
```
  - [관련 블로그](https://codechacha.com/ko/python-reverse-string/)

<br>

### 오름차순 정렬을 진행한 리스트에서 가장 큰 수는 리스트의 마지막 요소
- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%EC%BD%94%EB%93%9C%20%EA%B5%AC%ED%98%84%EB%A0%A5%20%EA%B8%B0%EB%A5%B4%EA%B8%B0/%EC%A3%BC%EC%82%AC%EC%9C%84%20%EA%B2%8C%EC%9E%84.py)


<br>

## 해시
- **문제 특징**
  - 리스트에 중복되는 요소가 존재한다. 그래서 중복을 제거하기 위해 해시를 사용할 생각을 할 수 있다.
  - 서로 다른 리스트에 겹치는 요소가 존재할 수 있다. 그래서 중복이 제거된 해시를 이용해 겹치는 요소와 안 겹치는 요소를 구분할 수 있다.
  - 리스트의 요소를 해시의 key로 설정해도 되고 value로 설정해도 된다.
  - “”문자열 안에 숫자가 서로 겹치는 부분이 있는 리스트가 주어지는 문제일 수 있다.

<br>

### 주어진 리스트 요소들의 중복을 제거하기 위해 해시를 사용할 수 있다
- **리스트에 요소의 종류가 다양할 때, 중복을 제거하기 위해 해시를 사용할 생각을 할 수 있다.**

<br>

### 주어진 리스트 요소들의 중복을 제거하기 위해 set 함수를 사용할 수 있다
- **또한,리스트의 중복을 제거할 때는 set()을 사용할수도 있다.**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%ED%95%B4%EC%8B%9C/%ED%8F%B0%EC%BC%93%EB%AA%AC.py)

<br>

### 해시 딕셔너리에 특정 키가 있는지 확인하기
- 해시(Hash) 딕셔너리에 특정 키가 있는지 확인하기
  - hash_map = {}, if temp in hash_map:
  - [관련 블로그](https://hashcode.co.kr/questions/59/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%ED%82%A4%EA%B0%80-%EC%9E%88%EB%8A%94%EC%A7%80-%ED%99%95%EC%9D%B8%ED%95%98%EA%B3%A0%EC%8B%B6%EC%96%B4%EC%9A%94)

<br>

### 리스트에 특정 값이 있는지 없는지 확인하기
- ex) if item in list: / if item not in list: 
  - [관련 블로그](https://lelecoder.com/111)

<br>

### 리스트가 여러 개 있을 때 모든 리스트들을 sort해서 비교할 생각하기
- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%ED%95%B4%EC%8B%9C/%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80%20%EB%AA%BB%ED%95%9C%20%EC%84%A0%EC%88%98.py)

<br>

### 문제에서 주어진 리스트 요소들을 해시 딕셔너리에 value가 1이 되게끔 추가해서 문제풀기

<br>

### 빈 문자열을 변수로 지정하고 해당 변수에 한 문자열씩 더해서 문제풀기
- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%ED%95%B4%EC%8B%9C/%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8%20%EB%AA%A9%EB%A1%9D.py)
```python
# 빈 문자열을 변수로 지정할 때 예시
temp = ""
temp += "tkdqor"
print(temp)

temp = []
temp += "tkdqor"
print(temp)


temp = []
temp.append("tkdqor")
print(temp)

tkdqor
['t', 'k', 'd', 'q', 'o', 'r']
['tkdqor']
```

<br>

### 해시의 모든 키에서 값을 선택하는 경우의 수 구하기
- 해시에 여러 key가 있을 때, 각 key마다 속해있는 여러 value값들이 있다고 생각하자. 이 때, 해시의 모든 key에서 value 값을 선택하는 경우의 수는 **1개의 키에서 뽑을 수 있는 경우의 수(안 뽑는 경우도 포함) X 다른 1개의 키에서 뽑을 수 있는 경우의 수(안 뽑는 경우도 포함) X ... -1(다 안뽑는 경우는 없어야 하니까 -1해주기)** 이렇게 표현할 수 있다.
  - 모든 키에서 하나씩 뽑는 것이니까 모든 사건이 동시에 일어나야 한다. 그래서 곱의 법칙으로 경우의 수를 곱해준다고 보면 된다.
  - [곱의 법칙 관련 내용](https://mathbang.net/109)

- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%ED%95%B4%EC%8B%9C/%EC%9C%84%EC%9E%A5.py)
  - 관련 문제에서는, 해시의 key에 해당하는 value를 경우의 수로 생각해서 처음 key를 생성할 때 경우의 수를 2로 value를 설정한다. 해당 키에 속하는 value를 선택하는 경우와 아예 선택하지 않는 경우이기 때문이다. 그리고 이미 key가 있는데 value가 추가되는 경우는 1만 추가된다. 이렇게 key 별로 경우의 수를 value로 지정한 다음, 여러 사건이 동시에 일어나야 하니까 곱의 법칙에 따라 다 곱해주고 다 안뽑는 경우는 없어야 하니까 -1를 해준다.

<br>

## DFS와 BFS
- **문제 특징**
  - 어떤 것들이 연결되어 있다는 정보를 2차원 배열로 제시할 수 있다.
  - def solution 부분에서 DFS 또는 BFS 함수를 호출한다. 그래서 그 밑에 DFS 또는 BFS 함수를 정의한다.
  - DFS/BFS 함수 정의 예시를 확인해보면, 문제에서 제공하는 변수들이 전부 DFS/BFS 함수의 매개변수로 포함된다.
    - def BFS(n, computers, com, visited): -> 개수 / 배열 / 0부터 숫자 / 방문처리 리스트
    - def DFS(idx, numbers, target, value): -> 0부터 숫자 / 배열 / 찾는 숫자 / 만들 수 있는 숫자
  - 어떤 과정 또는 경로를 트리처럼 조금씩 다르게 탐색해야 할 수 있다.

<br>

### 함수에서 return 공백으로 재귀함수 1개 취소하기
- **함수 정의할 때 return 만 사용하고 아무것도 입력하지 않으면, 맥락 상 break와 유사한 효과를 내기 때문에 실행 중단의 의미가 된다. 즉, return 공백이면 실행되고있는 재귀함수 1개가 취소되는듯 하다.**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/DFS%EC%99%80BFS/%ED%83%80%EA%B2%9F%20%EB%84%98%EB%B2%84.py)
  - 계속 진행되고 있는 재귀함수를 종료시켜버리고 만약 index와 value라는 값이 둘다 5였다가 return 공백이 실행되면 재귀함수도 종료되고 값도 둘다 4로 다시 돌아간다.
  - [관련 블로그](https://munang.tistory.com/entry/%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-Python-None-%EB%A6%AC%ED%84%B4%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0-%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98-None-%EB%A6%AC%ED%84%B4)

<br>

### 1문제를 DFS 또는 BFS로 푸는 예시
- **1문제를 재귀함수를 이용한 DFS 방법으로도 풀어보고 / 재귀함수 및 BFS 방법으로도 풀어보기**
  - **보통 DFS는 스택 자료구조를 활용**
  - **보통 BFS는 큐 자료구조를 활용 / 처음 노드 방문 시 방문처리하고 -> 큐를 생성한 다음에는 큐에 넣었다가 pop(0) 이렇게 뺄 때 또 방문처리**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/DFS%EC%99%80BFS/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC.py)

<br>

### 방문여부를 확인하기 위한 리스트를 list comprehension으로 설정하기
- **DFS 또는 BFS로 문제 풀 때, visited라는 리스트 만들고 visited = [False for i in range(n)] 이렇게 하면 만약에 n이 3이면 visited = [False, False, False] 이렇게 된다.**

<br>

## ETC

### 주어진 이진수 사이에 있는 0의 개수 계산하기
- **이진수가 10010001 이렇게 있을 때 1과 1 사이에 있는 0의 개수를 파악하기 위해서는, 1이 있는 인덱스만 리스트에 추가하고 리스트[1] - 리스트[0] -1 이런식으로 계산하면 구할 수 있다.**
  - ex) 이진수 10010001, index_list = [0, 3, 7] 이렇게 리스트를 만들 수 있다. 그리고 index_list[1] - index_list[0] -1 = 2가 1과 1사이의 0 개수이고, index_list[2] - index_list[1] -1 = 3이 뒤에 있는 1과 1사이의 0 개수가 된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/%EB%B0%98%EB%B3%B5/binarygap.py)

<br>

### CSV 형태와 같은 데이터 파싱 문제
- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/codility/csv%ED%8C%8C%EC%8B%B1/csv%ED%8C%8C%EC%8B%B1%20%EB%AC%B8%EC%A0%9C.py)   
- 특정 데이터가 주어졌을 때, 해당 데이터를 정해진 조건의 이름으로 변경하는 문제 
- 해시로 key별로 그룹화 진행 후, value값 오름차순 정렬. 변경한 이름을 해시 value 리스트에 추가하고 문제에 맞게 정렬하는 과정

<br>

### 리스트의 인덱스를 어떤 수들의 합이라고 생각하기
- **요소를 전부 0으로 초기화한 리스트의 인덱스를 어떤 수들의 합이라고 생각할 수 있다.**
  - 그래서 해당 합이 되면, 리스트의 요소를 1씩 추가해주고 어떤 합이 가장 많이 나왔는지 확인할 수 있다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%EC%BD%94%EB%93%9C%20%EA%B5%AC%ED%98%84%EB%A0%A5%20%EA%B8%B0%EB%A5%B4%EA%B8%B0/%EC%A0%95%EB%8B%A4%EB%A9%B4%EC%B2%B4.py)

<br>

### 어떤 수가 주어졌을 때 그 수의 자릿수의 합을 구하기
- **어떤 수 x가 있을 때, 그 수의 자릿수의 합을 구하는 문제**
  - 첫번째로, x를 10으로 나눈 몫으로 바꿔주면서 x를 10으로 나눈 나머지를 계속 더해주면 된다. ex) 125를 10으로 나눈 나머지는 5가 되고 몫은 12가 된다. 12를 다시 10으로 나누면 나머지는 2가 되고 몫은 1이 된다. 마지막으로 1을 10으로 나누면 나머지는 1이 되고 몫은 0이 된다.
  - 두번째 방법은, 어떤 수 x를 str로 문자열로 바꾸고 for문으로 하나씩 뽑은 다음, 다시 int로 정수화해서 더해주면 된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%EC%BD%94%EB%93%9C%20%EA%B5%AC%ED%98%84%EB%A0%A5%20%EA%B8%B0%EB%A5%B4%EA%B8%B0/%EC%9E%90%EB%A6%BF%EC%88%98%EC%9D%98%20%ED%95%A9.py)

<br>

### 어떤 숫자가 주어질 때 1부터 그 숫자까지의 범위안에 소수 구하기
- 값이 모두 0인 리스트를 생성하고 이 리스트의 인덱스가 1부터 주어진 숫자까지라고 생각하기.
- 2부터 숫자 n까지 for문으로 뽑아서 리스트 요소가 0이면 소수 개수 변수를 1증가 시킨다. 그리고 2의 배수, 3의 배수 이렇게 배수들을 뽑아서 해당되는 리스트 인덱스에 값을 1로 바꿔준다. 최종적으로 리스트에 값이 0인 인덱스들이 소수가 된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%EC%BD%94%EB%93%9C%20%EA%B5%AC%ED%98%84%EB%A0%A5%20%EA%B8%B0%EB%A5%B4%EA%B8%B0/%EC%86%8C%EC%88%98.py)

<br>

### 어떤 숫자가 주어질 때 그 숫자를 뒤집은 숫자를 만들기
- **어떤 숫자 x가 주어질 때, 그 숫자를 뒤집은 숫자를 만들기 위한 방법**
  - t = x % 10으로 한 자리씩 선택하고 res = (res * 10) + t라는 식으로 기존의 뒤집은 숫자를 * 10해서 한자리씩 증가시켜주고 새롭게 뒤집은 수를 일의 자리로 하기 위해 더해준다. 그 다음 주어진 수 x를 x = x // 10으로 바꿔주고 반복하면 된다.
  - 최종적으로 res 값이 주어진 수 x를 뒤집은 수가 된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%EC%BD%94%EB%93%9C%20%EA%B5%AC%ED%98%84%EB%A0%A5%20%EA%B8%B0%EB%A5%B4%EA%B8%B0/%EB%92%A4%EC%A7%91%EC%9D%80%20%EC%86%8C%EC%88%98.py)

- **리스트에서 특정 인덱스부터 인덱스까지 뒤집으려면, 처음 인덱스와 끝 인덱스를 반복해서 바꿔주기**
  - 리스트의 0 인덱스부터 4 인덱스까지 있다면 -> 0인덱스와 4인덱스 요소를 바꾸고, 1인덱스와 3인덱스 요소를 바꾸고 2인덱스 요소는 가만히 두면 된다. 그러면 뒤집어지는 것이다.
  - 즉, 리스트의 2번째부터 7번째까지라면, (7-2)+1 // 2 = 3이니까 for문을 3번만 돌면 뒤접어진다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%ED%83%90%EC%83%89%EA%B3%BC%20%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98/%EC%B9%B4%EB%93%9C%20%EC%97%AD%EB%B0%B0%EC%B9%98.py)

<br>

### 특정 숫자가 소수인지 아닌지 확인하기
- 16이라는 수가 주어졌을 때, 소수인지 확인하려면 16이 약수가 있는지 보면 된다.
- 1과 16 자기자신을 빼고 약수는 자기자신 절반인 8까지에서 존재하게 된다. 16의 약수를 구하라고 하면 1\*16, 2\*8이니까 소수인지 확인할 때는 절반까지만 for문으로 확인하면 된다.
- 그래서 16를 2부터 8까지 차례대로 나눴을 때 나머지가 0이 하나라도 있다면 16은 약수가 있으니 소수가 될 수 없다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%EC%BD%94%EB%93%9C%20%EA%B5%AC%ED%98%84%EB%A0%A5%20%EA%B8%B0%EB%A5%B4%EA%B8%B0/%EB%92%A4%EC%A7%91%EC%9D%80%20%EC%86%8C%EC%88%98.py)

<br>

### 가산점을 고려한 총 점수를 계산하기
- **가산점을 고려한 총 점수를 계산하는 경우, 총 점수를 계산하는 sum이라는 변수와 가산점을 계산하는 cnt라는 변수로 나눠서 진행해보기**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%EC%BD%94%EB%93%9C%20%EA%B5%AC%ED%98%84%EB%A0%A5%20%EA%B8%B0%EB%A5%B4%EA%B8%B0/%EC%A0%90%EC%88%98%20%EA%B3%84%EC%82%B0.py)

<br>

### 리스트 인덱스가 없는 경우 예외처리 하기
- 코드 작성 중에 리스트 요소가 없어서 리스트 인덱스를 더이상 선택할 수 없게 되는 경우, 에러가 발생하게 된다.
- 그래서, 이런 경우에는 try - except로 예외처리를 진행해서 코드를 구성해보자.
- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/hackerrank/Jumping%20on%20the%20Clouds.py)

<br>

### 리스트에서 처음과 끝 요소 비교하기
- 리스트의 길이가 size일 때, size를 2로 나눈 몫으로 인덱스를 설정해서 if s[j] != s[-1-j]: 이렇게 리스트의 처음과 끝 요소, 그 다음 앞에 요소와 그 다음 뒤의 요소를 비교할 수 있다.

```python
for j in range(size//2):
  if s[j] != s[-1-j]:
    print("#%d NO" %(i+1))
    break
  else:
    print("#%d YES" %(i+1))
```
- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%ED%83%90%EC%83%89%EA%B3%BC%20%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98/%ED%9A%8C%EB%AC%B8%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%EA%B2%80%EC%82%AC.py)

<br>

### 리스트 요소 하나씩 꺼내서 자연수 만들기
- 리스트 요소를 for문으로 하나씩 뽑아서 숫자가 맞으면 res = 0, res = (res * 10) + int(x) 이러한 식으로 자연수를 만들어줄 수 있다.
  - 이렇게 하면 자동으로 첫자리에 0이 오는 것을 무시할 수 있다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%ED%83%90%EC%83%89%EA%B3%BC%20%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98/%EC%88%AB%EC%9E%90%EB%A7%8C%20%EC%B6%94%EC%B6%9C.py)

<br>

### 리스트에서 하나씩 뽑을 때 앞에 요소를 뽑고 해당 요소 바로 뒤부터 뽑기
```python
for x in range(len(a)):
    for y in range(x+1, len(a)):
```
- 이런식으로 코드를 구현할 수 있다.

<br>

### 리스트 인덱스를 가리키는 2개의 변수를 생성해서 연속적인 리스트 요소들의 합을 구하기
- [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B0%95%EC%9D%98/%ED%83%90%EC%83%89%EA%B3%BC%20%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98/%EC%88%98%EB%93%A4%EC%9D%98%20%ED%95%A9.py)


