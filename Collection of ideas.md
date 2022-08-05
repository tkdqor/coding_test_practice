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

<br>

### Ideas
- "가장 큰 수", "최소 횟수", "최댓값" 등을 요구하는 문제가 나온다면 "그리디" 문제라고 생각해보기. 그래서 최소의 input으로 답이 나오게끔 생각
- **전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산** 
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/greedy/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4_p313_%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py)
- **리스트가 있을 때 첫 번째 원소만 따로 처리한 다음, 두 번째 원소부터 마지막까지 for문으로 처리**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/greedy/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4_p313_%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py)
- **if문에서 문자열과 숫자를 비교해야 할 때, if data[i] == '1': 이런식으로도 가능**
  - [관련 문제](https://github.com/tkdqor/coding_test_practice/blob/master/greedy/%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4_p313_%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py)



