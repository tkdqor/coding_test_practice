price = int(input())    # 타로가 지불할 가격
remain = 1000 - price   # 1000엔에서 지불할 가격을 차감 --> 받아야 할 잔돈
count = 0               # 잔돈 개수


changes_list = [500, 100, 50, 10, 5, 1]   # 잔돈 종류를 리스트로 저장

for n in changes_list:     # 잔돈 종류 1개씩 빼서           
    count += remain // n   # 잔돈을 나눴을 때 몫을 잔돈 개수에 더하기
    remain = remain % n    # 잔돈을 나눴을 때 나머지가 다시 잔돈이 되게끔 설정

    if remain == 0:        # 만약 잔돈이 0원이면 잔돈 개수가 다 구해진거니까 for문 종료
        break

print(count)

