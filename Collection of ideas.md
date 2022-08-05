## collection of ideas

### Codes
- len(array) / 리스트 요소 개수
- array.sort() / 리스트 오름차순 정렬
- array.count(i) / 리스트에서 i라는 요소의 개수
- for i in range(~, ~) / 범위 for문
- for _ in range(n+1) / 데이터 n개 for문
- max(~, ~) / 둘 중 최댓값
- min(~, ~) / 둘 중 최솟값
- dx = [0, 1, 0, -1] dy = [-1, 0, 1, 0] / 서남동북 행과 열 표시
- nx = x + dx[i] ny = y + dy[i] / (x, y)에서 좌표이동
- n, m = map(int, input().split()) / 숫자들을 공백 기준으로 따로 변수에 저장
- data = list(map(int, input().split())) / 숫자들을 공백 기준으로 입력받고 리스트로 저장
- for i in range(1, m+1) / 1부터 m까지 for문으로 뽑기

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
