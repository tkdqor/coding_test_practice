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




A = [4,1,3,2]
# 이건 순열이 맞다.. 1부터 N까지의 요소가 다 있는 것.. 그래서 이 리스트가 순열인지 아닌지 체크 / 순열이면 1 반환