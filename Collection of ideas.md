## collection of ideas

### Codes
- **len(array)** / 리스트 요소 개수
- **array.sort()** / 리스트 오름차순 정렬
- **array.count(i)** / 리스트에서 i라는 요소의 개수
- **for i in range(~, ~)** / 범위 for문
- **for _ in range(n+1)** / 데이터 n개 for문
- **max(~, ~)** / 둘 중 최댓값
- **min(~, ~)** / 둘 중 최솟값
- **dx = [0, 1, 0, -1] dy = [-1, 0, 1, 0]** / 서남동북 행과 열 표시
- **nx = x + dx[i] ny = y + dy[i]** / (x, y)에서 좌표이동
- **n, m = map(int, input().split())** / 숫자들을 공백 기준으로 따로 변수에 저장
- **data = list(map(int, input().split()))** / 숫자들을 공백 기준으로 입력받고 리스트로 저장
- **for i in range(1, m+1)** / 1부터 m까지 for문으로 뽑기
- **isinstance(1.2, float)** / 해당 매개변수가 지정한 타입이 맞는지 확인하는 함수
  - [관련 블로그](https://brownbears.tistory.com/155)
- **string = "Hello World!", string3 = string.split(' '), print(string3) 하게되면 ['Hello', 'World!']** / 문자열을 split를 이용해 나누게 되면 리스트 형태가 된다.
  - [관련 블로그](https://wikidocs.net/2839)
- **for idx, answer in enumerate(answers):** / enumerate 함수를 사용해서 자료형에서 인덱스와 함께 요소들을 뽑아낼 수 있다.
  - [관련 블로그](https://hckcksrl.medium.com/python-enumerate-b19ad6b94c00)
- **array[1:5]** 이렇게 슬라이싱하면, 인덱스 1부터 4까지 슬라이싱된다.
- ex) my_list = [“Mitch”, [3,6,7], [“yellow”, 5, 6]] 라고할 때, my_list[1][1:3]이면 -> [6,7] 슬라이싱
- **리스트를 정렬할 때 사용하는 sort 함수와 sorted 함수의 차이점**
  - sort 함수는 리스트명.sort() 형식으로 리스트의 원본값을 직접 수정하며 리턴값이 None이다. 
  - sorted 함수는 sorted(리스트명) 형식으로 리스트의 원본값은 그대로이고 새로운 리스트를 만들어 정렬값을 반환한다.
  - [관련 블로그](https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=wideeyed&logNo=221745416992&redirect=Dlog&widgetTypeCall=true&directAccess=false)
- **global 사용하기**
  - 함수밖에서 선언되는 변수를 “전역 변수”라고 하는데, 그 전역 변수의 값을 함수 안에서 변경하려면 global이라는 키워드를 사용해서 선언해주면 변경할 수 있다.
  - [관련 블로그](https://codingpractices.tistory.com/entry/Python-%EC%A0%84%EC%97%AD-%EB%B3%80%EC%88%98-%EC%A7%80%EC%97%AD-%EB%B3%80%EC%88%98-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%B4%9D-%EC%A0%95%EB%A6%AC-global-nonlocal)
- **|= 연산자 사용하기**
  - 병합 연산자로 union 즉, 합집합을 의미한다.
  - [관련 블로그](https://velog.io/@nayoon-kim/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%97%B0%EC%82%B0%EC%9E%90) 
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
- **list 함수 예시**
```python
n = "17"
print(list(n))

['1', '7']
```
- **set 함수 예시**
```python
print(set(range(0, 2)))

{0, 1}

print(set(range(0, 3)) - set(range(0, 2)))

{2}
```
- **range 함수의 마지막 매개변수는 range의 간격을 지정해준다**
  - print(list(range(1, 11, 2))) / [1, 3, 5, 7, 9]
  - 이렇게하면 원래는 1부터 10까지 출력되지만, 간격이 2이기 때문에 1부터 2씩 증가된 수가 출력된다
- **join 함수 사용하기**
  - ‘구분자’.join(리스트) / 이러한 원형으로 매개변수로 들어온 리스트에 있는 요소 하나하나 사이에 구분자를 넣어서 하나의 문자열로 합쳐주는 함수이다. 구분자는 공백일 수도 있다. 
  - [관련 블로그](https://blockdmask.tistory.com/468)
- **map 함수 사용하기**
  - map(적용할 함수, 반복 가능한 자료형)
  - map 함수를 활용하면 모든 반복가능 자료형 데이터 각각에 함수를 적용시킬 수 있다.
- **루트 계산 관련**
  - print(4 ** 0.5) / 2
  - 루트 4를 의미하니까 2가 출력된다
- **해시(Hash) 딕셔너리에 특정 키가 있는지 확인하기**
  - hash_map = {}, if temp in hash_map:
  - [관련 블로그](https://hashcode.co.kr/questions/59/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%ED%82%A4%EA%B0%80-%EC%9E%88%EB%8A%94%EC%A7%80-%ED%99%95%EC%9D%B8%ED%95%98%EA%B3%A0%EC%8B%B6%EC%96%B4%EC%9A%94)
- **12%1 = 0, 12//3 = 4, 12/3 = 4.0, 0%5 = 0, 1%5 = 1**
- **continue는 반복문에서 조건이 맞지 않을 때 반복문을 종료시키지 않고 맨 처음의 조건문으로 보내주는 역할을 한다.**
  - **pass는 어떤 조건문에 대해서 아무런 실행을 하지 않고 아래 코드를 이어서 실행하게 된다. 반면에 continue는 맨 처음 조건문으로 돌아가면서 아래 코드를 실행하지 않는다.**
  - [관련 블로그](https://securityspecialist.tistory.com/73)
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
- **문자열 반복하기**
  - print("6"*3, "10"*3, "2"*3) / 666 101010 222
- **DFS 또는 BFS로 문제 풀 때, visited라는 리스트 만들고 visited = [False for i in range(n)] 이렇게 하면 만약에 n이 3이면 visited = [False, False, False] 이렇게 된다.**


<br>

### Ideas
- "가장 큰 수", "최소 횟수", "최댓값" 등을 요구하는 문제가 나온다면 "그리디" 문제라고 생각해보기. 그래서 최소의 input으로 답이 나오게끔 생각
- **전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산** 
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/greedy/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4_p313_%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py)
- **리스트가 있을 때 첫 번째 원소만 따로 처리한 다음, 두 번째 원소부터 마지막까지 for문으로 처리**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/greedy/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4_p313_%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py)
- **if문에서 문자열과 숫자를 비교해야 할 때, if data[i] == '1': 이런식으로도 가능**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/greedy/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4_p313_%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py)
- **리스트에서 만들 수 없는 양의 정수 금액 중 최솟값**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/greedy/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4_p314_%EB%A7%8C%EB%93%A4%20%EC%88%98%20%EC%97%86%EB%8A%94%20%EA%B8%88%EC%95%A1.py)
- **A가 특정한 무게의 볼링공을 선택했을 때, 이어서 B가 볼링공을 선택하는 경우 -> A를 기준으로 무게가 낮은 볼링공부터 무게가 높은 볼링공까지 순서대로 확인하기**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/greedy/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4_p315_%EB%B3%BC%EB%A7%81%EA%B3%B5%20%EA%B3%A0%EB%A5%B4%EA%B8%B0.py)
- **로또 번호 순위 리스트에 미리 정의해놓기, 일치번호 개수와 불일치번호 개수로 나누기**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EB%A1%9C%EB%98%90%EC%9D%98%20%EC%B5%9C%EA%B3%A0%20%EC%88%9C%EC%9C%84%EC%99%80%20%EC%B5%9C%EC%A0%80%20%EC%88%9C%EC%9C%84.py)
- **루트 제곱근 계산 방법**
  - x를 제곱하여 a가 되었다면, x를 a의 제곱근이라고 부른다. 수학 라이브러리인 Math를 이용해서 제곱근을 구할 수 있다.
  - [관련 블로그](https://needneo.tistory.com/77)
- **리스트에서 원하는 값 제거하는 방법**
  - 리스트에 remove 함수 / 반복문 사용 / del 키워드 / pop 함수 / clear 함수를 이용해 원하는 값을 제거할 수 있다.
  - [관련 블로그](https://zeroaan.github.io/python/2020/05/02/Python-List%EC%97%90%EC%84%9C-%EC%9B%90%ED%95%98%EB%8A%94-%EA%B0%92-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0.html)
- **리스트에 특정 값이 있는지 없는지 확인하기**
  - ex) if item in list: / if item not in list: 
  - [관련 블로그](https://lelecoder.com/111)
- **slice로 문자열 순서 뒤집기**
  - [관련 블로그](https://codechacha.com/ko/python-reverse-string/)
- **리스트의 중복을 제거할 때는 set()을 사용할 생각해보기**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%ED%8F%B0%EC%BC%93%EB%AA%AC.py)
- **리스트가 여러 개 나올 때, 모든 리스트들을 sort()해서 비교하기**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80%20%EB%AA%BB%ED%95%9C%20%EC%84%A0%EC%88%98.py)
- **리스트로 풀었을 때 효율성 테스트가 실패하거나, 데이터를 빠르게 넣고 가져오려면 Hash 이용해보기(key - value pair를 의미)**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80%20%EB%AA%BB%ED%95%9C%20%EC%84%A0%EC%88%98.py)
- **어떤 리스트에 요소가 5개가 있고 그 5개가 순환주기로 계속 반복될 때 특정 인덱스가 어떤 요소를 가리키는지 확인해야 한다면, 인덱스 % 요소개수 = 인덱스 이렇게 구할 수 있다.**
  - ex) pattern1 = [1, 2, 3, 4, 5] 일 때, 인덱스 6인 요소는 6 % len(pattern1) = 1이니까 6번째는 2가 된다.
  - 어떤 수를 x로 나누면 나머지는 무조건 x보다 작다. 그래서 특정 범위 내 숫자를 구할 때 자주 사용된다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC.py)
- **2차원 배열에서 리스트 뽑기**
  - 2차원 배열에서 리스트 뽑을 때는 for문을 사용하면 된다. ex) commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]] 일 때, for command in commands: i,j,k = command 이렇게하면 i = 2, j = 5, k = 3 이렇게 변수 지정 가능.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/K%EB%B2%88%EC%A7%B8%20%EC%88%98.py)
- **while문을 사용해서 하루씩 증가할 때 완료된 모든 업무의 개수를 count + 이미 들어가있는 리스트에서 완료될때마다 pop(0) 진행 + 자료구조 큐와 유사**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EA%B8%B0%EB%8A%A5%EA%B0%9C%EB%B0%9C.py)
- **함수 정의할 때 return 만 사용하고 아무것도 입력하지 않으면, 맥락 상 break와 유사한 효과를 내기 때문에 실행 중단의 의미가 된다. 즉, return 공백이면 실행되고있는 재귀함수 1개가 취소되는듯 하다.**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%ED%83%80%EA%B2%9F%20%EB%84%98%EB%B2%84.py)
  - 계속 진행되고 있는 재귀함수를 종료시켜버리고 만약 index와 value라는 값이 둘다 5였다가 return 공백이 실행되면 재귀함수도 종료되고 값도 둘다 4로 다시 돌아간다.
  - [관련 블로그](https://munang.tistory.com/entry/%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-Python-None-%EB%A6%AC%ED%84%B4%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0-%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98-None-%EB%A6%AC%ED%84%B4)
- **소수를 구하는 방법**
  - 소수란, 1과 자기 자신외의 약수를 가지지 않는 1보다 큰 자연수를 의미한다. 이론상으로 단일 숫자가 소수인지 판단하는 방법은, 숫자 n이 소수인지 알아보기 위해 2부터 n-1까지의 숫자를 반복하며, 나누어 떨어지는 숫자가 있는지 확인하고 만일 없다면, 소수가 된다.
  - 더 효율적으로 소수를 구하는 공식이 있는데, 바로 **에라토스테네스의 체**라는 방법이다.
    - 소수를 구하고자 하는 범위 2에서 n이 있을 때, 2~n의 제곱근에 해당하는 범위 안의 소수의 배수들을 계속 제외하면 결국 소수만 남는다는 이론이다.
    - ex) 이를테면 n=100일 때, 100까지의 소수를 구하고 싶다면, 2에서 100까지 숫자에서 -> 100의 제곱근이 10이니까 2~10까지의 범위 안에 소수의 배수인 2의 배수 제외, 3의 배수 제외, 5의 배수 제외, 7의 배수 제외를 진행한다는 것이다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%86%8C%EC%88%98%20%EC%B0%BE%EA%B8%B0.py)
  - [관련 블로그](https://velog.io/@jakeseo_me/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-14-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4)
- **문제에서 주어진 리스트 요소들을 해시(Hash) 딕셔너리에 value가 1이 되게끔 추가해서 문제풀기**
- **빈 문자열을 변수로 지정하고 해당 변수에 한 문자열씩 더해서 문제풀기**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8%20%EB%AA%A9%EB%A1%9D.py)
```python
# 빈 문자열을 변수로 지정할 때 예시
temp = []
temp += "tkdqor"
print(temp)


temp = []
temp.append("tkdqor")
print(temp)

['t', 'k', 'd', 'q', 'o', 'r']
['tkdqor']
```
- **문제에서 사각형과 그 안에 격자로 이루어져 있다면 ==> 사각형 가로 * 세로 = 갈색 격자 개수 + 노란색 격자 개수 라는 식을 세울 수 있다.**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EC%B9%B4%ED%8E%AB.py)
- **문자형태의 숫자를 비교할 때 \*로 문자열의 길이를 늘려서 비교해볼 수도 있다**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EA%B0%80%EC%9E%A5%20%ED%81%B0%20%EC%88%98.py)
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

- **리스트가 있을 때, 오름차순 정렬을 한 다음에 총 개수에서 특정 인덱스를 차감하면 -> 특정 인덱스 데이터 포함해서 남은 리스트 요소의 개수가 된다. 그리고 남은 리스트 요소들은 특정 인덱스 값보다 크다는 것을 알 수 있다.**
  - ex)정렬된 상태라고 생각하고 총 5개에서 인덱스 2를 빼면 -> 3이니까 인덱스 2 데이터 포함해서 뒤에 3개가 남아있다.
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/H-Index.py)
- **우선순위와 관련된 문제를 while문 안에있는 for문으로 구하는 과정**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%ED%94%84%EB%A6%B0%ED%84%B0.py) 
- **1문제를 재귀함수를 이용한 DFS 방법으로도 풀어보고 / 재귀함수 및 BFS 방법으로도 풀어보기**
  - **보통 DFS는 스택 자료구조를 활용**
  - **보통 BFS는 큐 자료구조를 활용 / 처음 노드 방문 시 방문처리하고 -> 큐를 생성한 다음에는 큐에 넣었다가 pop(0) 이렇게 뺄 때 또 방문처리**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/programmers/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC.py)
