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





