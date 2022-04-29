# N = int(input())
# bags = [5, 3]
# count = 0

# for bag in bags:
#     count += N // bag
#     N = N % bag

#     if 0 < N < 3:
#         count -= 1

#     if N == 0:
#         break

# print(count)

###################### 실패한 풀이.. #######################

# N = int(input())
# bags = [5, 3]
# count = 0

# for bag in bags:
#     if (N % bag) % 3 == 0:
#         count += N // bag
#         N = N % bag
#     else:
#         pass

#     if N == 0:
#         break

# print(count)

###################### 또 실패... #######################


### 블로그 답안

sugar = int(input())

bag = 0                      # 봉지 개수
while sugar >= 0 :           # 5의 배수가 될 때까지 sugar를 3씩 차감할 때 sugar가 양수 및 0일 때만 반복
    if sugar % 5 == 0 :      # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 개수에 추가
        print(bag)
        break
    sugar -= 3  
    bag += 1                 # 5의 배수가 될 때까지 설탕-3, 봉지+1 (즉, 5의 배수가 될 때까지 3킬로그램 봉지 1개씩 사용)
else :
    print(-1)                # 5의 배수가 될 때까지 sugar를 3씩 차감하는데 마이너스라면 정확하게 N킬로그램이 되지 않은 거니까 -1 출력



