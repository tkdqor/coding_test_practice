# # def solution(S):
# #     # write your code in Python 3.6
# #     hash_map = {}
# #     hash_map[1] = "ba"
# #     return hash_map

# # print(solution('aabbb'))


# def solution(S):
#     # write your code in Python 3.6
#     photos = S.split('\n')
#     old_photos = []
#     new_photos = []
#     hash_map = {}
#     order = [0,0,0]
#     result = []
#     # 먼저 사진들을 오름차순하고 그룹나누기.. 정렬할 때 key 기준을 시간으로...
#     # photos = sorted(photos, key = lambda x : )
    
#     # 하나만 되면 while 붙여주면 됨
#     for photo in photos:
#         element = photo.split(',')
#         old_photos.append(element)
#         new_photos.append(element)
    
#     new_photos = sorted(new_photos, key = lambda x : x[2])

#     for new_photo in new_photos:
#         for old_photo in old_photos:
#             if new_photo[1] == old_photo[1] == " Warsaw" and new_photo[2] == old_photo[2]:
#                 order[0] += 1
#                 result.append("Warsaw" + str(order[0]))
#             if new_photo[1] == old_photo[1] == " London" and new_photo[2] == old_photo[2]:
#                 order[1] += 1
#                 result.append("London" + str(order[1]))
#             if new_photo[1] == old_photo[1] == " Paris" and new_photo[2] == old_photo[2]:
#                 order[2] += 1
#                 result.append("Paris" + str(order[2]))
    
#     return old_photos

# S = 'photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'
# # print(solution(S))



# # csv파싱 문제
# # 그룹화를 해시로 하기 -> key가 도시이고, value로 2차원 배열로 하기
# # split로 기준에 맞게 나누기
# # 해시에서 keys랑 values만 빼기
# # 맨 마지막은 [-1]로 뺴기
# # format으로 문자열을 변수로 사용하기
# # extend 사용하기
# def solution(S):
#     photos = S.split('\n')
#     hash_map = {}
#     for i, photo in enumerate(photos):
#         raw = []
#         for item in photo.split(','):
#             raw.append(item.strip(' '))
#         if len(raw) == 3:
#             raw.append(i)
#             if raw[1] not in hash_map:
#                 hash_map[raw[1]] = []
#             hash_map[raw[1]].append(raw)
#     for key in hash_map.keys():
#         city = sorted(hash_map[key], key = lambda x : x[2])
#         for j, info in enumerate(city):
#             ext = info[0].split('.')[-1]
#             n = len(city)
#             k = len(str(n))
#             file = "{0}{1}.{2}".format(key, str(j+1).rjust(k,'0'), ext)
#             city[j].append(file)
#         hash_map[key] = city

#     output = []
#     for value in hash_map.values():
#         # 리스트안에 요소가 계속 늘어나게 됨
#         output.extend(value)
    
#     # 원래 인덱스 기준으로 정렬하기
#     result = sorted(output, key = lambda x : x[3])
#     for item in result:
#         print(item[4])

# # 답을 형식에 맞추기


# today = "오늘 합격 각"
# print(f"{today}")

# temp = ""
# temp += "tkdqor"
# print(temp)




########### 일단 보류!!!
# def solution(S):
#     # write your code in Python 3.6
#     count = 0
#     road = list(S)

#     for i in range(len(road)):
#         before = road.count(1)
#         if road[i] == 'X':
#             road[i] = 1
#         if road[i+1] == 'X':
#             road[i+1] = 1
#         if road[i+2] == 'X':
#             road[i+2] = 1
#         after = road.count(1)
        
#         if before != after:
#             count += 1
#         if road.count('X') == 0:
#             return count


#### 1번
# def solution(A):
#     # write your code in Python 3.6
#     A = sorted(A)
#     answer = False

#     while A:
#         try:
#             a = A.pop()
#             b = A.pop()
#         except:
#             return False
        
#         if a == b:
#             answer = True
#     return answer




#### 2번
# def solution(S):
#     # write your code in Python 3.6
#     count = 0
#     road = list(S)

#     for i in range(0, len(road), 3):
#         if road[i] or road[i+1] or road[i+2] == 'X':
#             for j in range(i, i+3):
#                 try:
#                     if road[j]:
#                         road[j] = 'O'
#                 except IndexError:
#                     continue
#             count += 1    
#         if road.count('X') == 0:
#             break
#     return count


# print(solution('.X..X'))



### 3번
# def solution(R, V):
#     # write your code in Python 3.6
#     bank = list(R)
#     x, y = 0, 0
#     balance = [x,y]
#     balance_sum = balance[0] + balance[1]
#     result = balance_sum * (len(V)+1)
#     # 이 result랑 매 거래 후 잔액을 다 더했을 때 금액이랑 같아야 한다
#     result2 = 0

#     for i in range(len(V)):
#         if R[i] == 'B':
#             balance[1] += V[i]
#             balance[0] -= V[i]
#         else:
#             balance[0] += V[i]
#             balance[1] -= V[i]
#         result2 += balance[0] + balance[1]
    
#     for i in range(1, 10001):
#         for j in range(1, 10001):
#             balance[0] = i
#             balance[1] = j
#             if result == result2:
#                 return [balance[0], balance[1]]



# ### 틀린 3번 제출 답
# def solution(R, V):
#     # write your code in Python 3.6
#     bank = list(R)
#     balance = [0,0]
#     # 이 result랑 매 거래 후 잔액을 다 더했을 때 금액이랑 같아야 한다
#     result2 = 0

#     for i in range(1, 10001):
#         for j in range(1, 10001):
#             balance[0] = i
#             balance[1] = j

#             for i in range(len(V)):
#                 if R[i] == 'B':
#                     balance[1] += V[i]
#                     balance[0] -= V[i]
#                 else:
#                     balance[0] += V[i]
#                     balance[1] -= V[i]
#                 balance_sum = balance[0] + balance[1]
#                 result = balance_sum * (len(V)+1)
#                 result2 += balance[0] + balance[1]
#                 if result == result2:
#                     return [balance[0], balance[1]]
            

# print(solution('BAABA', [2, 4, 1, 1, 2]))

def solution(new_id):
    result = ''
    result2 = ''
    for i in new_id:
        if i.isupper():
            j = i.lower()
            result += j
        elif i in ['!', '@', '#', '*']:
            pass
        elif i == '.':
            result += i
        else:
            result += i
    for idx, k in enumerate(result):
        if result[idx-1] == '.' and k == '.':
            continue
        result2 += k
    return result2

print(solution("...!@BaT#*..y.abcdefghijklm"))

