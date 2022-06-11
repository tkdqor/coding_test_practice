## 점프 투 파이썬 정리(if문)

### if문의 기본 구조

```python
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
```

- **조건문을 테스트해서 참이면 if문 바로 다음 문장(if 블록)들을 수행하고, 조건문이 거짓이면 else문 다음 문장(else 블록)들을 수행하게 된다. 그러므로 else문은 if문 없이 독립적으로 사용할 수 없다.**

<br>

### 조건문 다음에 콜론(:)을 잊지 말자
- if 조건문 뒤에는 반드시 콜론(:)이 붙는다. 어떤 특별한 의미가 있다기보다는 파이썬의 문법 구조이다. 왜 하필 콜론(:)인지 궁금하다면 파이썬을 만든 귀도에게 직접 물어보아야 할 것이다. 앞으로 배울 while이나 for, def, class문에도 역시 문장의 끝에 콜론(:)이 항상 들어간다. 초보자들은 이 콜론(:)을 빠뜨리는 경우가 많으니 특히 주의하자.

- 파이썬이 다른 언어보다 보기 쉽고 소스 코드가 간결한 이유는 바로 콜론(:)을 사용하여 들여쓰기(indentation)를 하도록 만들었기 때문이다. 하지만 이는 숙련된 프로그래머들이 파이썬을 처음 접할 때 제일 혼란스러워하는 부분이기도 하다. 다른 언어에서는 if문을 { } 기호로 감싸지만 파이썬에서는 들여쓰기로 해결한다는 점을 기억하자.

<br>

### if 조건문
- if 조건문에서 "조건문"이란 참과 거짓을 판단하는 문장을 말한다.

- **비교연산자**
  - 이번에는 **조건문에 비교연산자(<, >, ==, !=, >=, <=)를 쓰는 방법에 대해 알아보자.**

<img width="297" alt="image" src="https://user-images.githubusercontent.com/95380638/173182417-0ed609bb-3e1a-4141-9270-3f6801e6ea3a.png">


<br>

### if 조건문 예시

```python
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
걸어가라
```

- money >= 3000 조건문이 거짓이 되기 때문에 else문 다음 문장을 수행하게 된다.

<br>

### and, or, not

<img width="352" alt="image" src="https://user-images.githubusercontent.com/95380638/173182849-72a3d470-cf0d-40f9-86dd-e89356de9c5e.png">

- 조건을 판단하기 위해 사용하는 다른 연산자로는 and, or, not이 있다. 각각의 연산자는 다음처럼 동작한다.


<br>

### x in s, x not in s
- 더 나아가 파이썬은 다른 프로그래밍 언어에서 쉽게 볼 수 없는 재미있는 조건문을 제공한다.

<img width="253" alt="image" src="https://user-images.githubusercontent.com/95380638/173182884-0c0c981b-4220-48df-8474-a3a56f86a7d4.png">


```python
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')


True
False
True
True
```

<br>

### 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
- 가끔 조건문의 참, 거짓에 따라 실행할 행동을 정의할 때, 아무런 일도 하지 않도록 설정하고 싶을 때가 있다. **그럴 때는 pass를 사용할 수 있다.**
  - "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라." 라는 예시가 있다면, 

```python
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

```
- **이렇게 코드를 짤 수 있다. 그래서 pocket 리스트 안에 money 문자열이 있기 때문에 if문 다음 문장인 pass가 수행되고 아무 결괏값도 보여 주지 않는다.**


<br>

### 다양한 조건을 판단하는 elif
- if와 else만으로는 다양한 조건을 판단하기 어렵다. 그래서 파이썬에서는 다중 조건 판단을 가능하게 하는 elif를 사용한다. elif는 이전 조건문이 거짓일 때 수행된다.

```python
If <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
   ... 
```

- elif는 개수에 제한 없이 사용할 수 있다.

<br>

### if문을 한 줄로 작성하기
- **if문 다음에 수행할 문장이 한 줄이고, else문 다음에 수행할 문장도 한 줄밖에 되지 않는 경우,**

```python
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
```

- 위와 같은 코드를,

```python
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
```

- **이렇게 if문 다음 수행할 문장을 콜론(:) 뒤에 바로 적어주고 else 문도 그렇게 해줄 수 있다.**


<br>

### 조건부 표현식(conditional expression)

```python
if score >= 60:
    message = "success"
else:
    message = "failure"
```

- 다음과 같은 코드가 있을 경우, 파이썬의 조건부 표현식(conditional expression)을 사용해서 더 간결하게 작성할 수 있다.

```python
message = "success" if score >= 60 else "failure"
```

- 이렇게 조건부 표현식은 
```python
조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
```

- 이러한 구조로 작성할 수 있다.
