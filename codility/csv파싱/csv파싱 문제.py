# csv파싱 문제 => 해시로 그룹화 - 오름차순 정렬 - 변경한 이름 해시 value 리스트에 추가 - 문제에 맞게 정렬

def solution(S):
    # 먼저 주어진 문자열을 개행기준으로 짤라서 리스트로 만들기
    photos = S.split('\n')
    # hash_map으로 해시 정의하기
    hash_map = {}
    # 개행기준으로 짜른 리스트를 enumerate로 인덱스와 함께 for문 진행
    for i, photo in enumerate(photos):
        raw = []
        # 개행기준으로 짜른 리스트의 요소를 하나씩 콤마(구분자) 기준으로 짜르고, 그 짜른 걸 for문으로 하나씩 뽑기
        for item in photo.split(','):
            # 뽑은 요소들을 raw라는 리스트에 append하기 / 이 때, 그 요소의 양 옆 공백을 없애고 추가하기 위해 strip 함수 사용하기
            raw.append(item.strip(' '))
        # 그렇게 해서 raw 리스트 요소의 개수 len이 3개일 때, enumerate로 뽑은 인덱스를 raw 리스트 마지막에 추가해준다
        # raw = [‘photo.jpg’, ‘Warsaw’, ‘2013-09-05 14:08:15’, 0] 이런식의 상태가 된다
        if len(raw) == 3:
            raw.append(i)
            # 위의 상태에서 raw[1]이 hash_map에 없다면, hash_map[raw[1]] = [] 이런식으로 해당 도시를 key로 설정하고 빈 리스트를 value로 설정해준다
            if raw[1] not in hash_map:
                hash_map[raw[1]] = []
            # 그 다음 hash_map[raw[1]].append(raw) 이렇게 raw[1]에 해당하는 key와 연결된 value에 append로 raw를 추가해서 도시별 그룹화 진행
            # {‘Warsaw’: [[‘photo.jpg’, ‘Warsaw’, ‘2013-09-05 14:08:15’, 0], …]}
            # 그리고 for문이 돌 때 마다 이 raw가 다시 빈 리스트가 되면서 반복된다
            hash_map[raw[1]].append(raw)
    # 즉, 여기까지가 하나의 for문이고 hash_map이라는 해시에 key에는 도시가 들어가있고, 그 key에 해당하는 value는 그 도시에 찍은 사진 정보 리스트들이 
    # 2차원 배열로 들어가 있게 된다. raw = [] 이렇게 raw라는 빈 리스트를 만들고 주어진 리스트의 요소를 하나씩 나눠서 공백 제거해서 넣고 나중에는 그 raw를 
    # 해시의 value에 넣는 것이다.

    # 이제 그 다음 for문에서 해시의 key만 하나씩 뽑는다
    for key in hash_map.keys():
        # 그래서 해당 key에 대응되는 value 2차원 배열 리스트를 날짜기준으로 오름차순 정렬을 진행한다
        # 여기서 2차원 배열의 리스트 요소 1개씩을 x라고 생각하면 된다 / 그래서 그 리스트의 인덱스 2면 3번째이니까 날짜를 기준으로 오름차순 정렬이 되는 것이다
        # city = [[‘myFriends.png’, Warsaw’, ‘2013-09-05 14:07:13’], [], ..] 이런식으로 2차원 배열이 되고 날짜 기준 오름차순 정렬이 된다
        # 즉, 해시에 있는 key를 for문으로 하나씩 뽑아서 대응되는 value 리스트들을 기준에 맞게 정렬한 새로운 city라는 리스트를 정의하는 것이다
        city = sorted(hash_map[key], key = lambda x : x[2])
        # 하나의 key에 대응되는 value들을 다 정렬한 상태에서, 그 city 2차원 배열에서 enumerate로 인덱스와 요소들을 뽑아주기
        for j, info in enumerate(city):
            # 그러면 하나의 사진 정보 리스트가 나올텐데, 가장 앞에 있는 사진 제목에 접근하고 콤마를 기준으로 나눈뒤 [-1]로 가장 마지막에 있는 요소를 가져오면 
            # ext가 png와 같은 확장자가 된다. 
            ext = info[0].split('.')[-1]
            # 그 다음, 도시 이름 옆에 번호를 붙여야하는데 총 사진의 개수가 1자리 수이면 1,2,3,… 이렇게 되고 2자리 수이면 01,02,… 10, .. 이렇게 되어야 한다
            # 이렇게 하기 위해 위에서 정렬한 2차원 배열 리스트인 city의 개수를 구하고, 
            # 그 개수를 문자열로 만들어서 또 개수를 구하면 ==> 총 개수의 자릿수를 알 수 있게 된다
            # ex) 총 city의 개수가 10개라면 k는 2가 되어 2자릿수라는 것을 알 수 있다
            n = len(city)
            k = len(str(n))
            # 그 다음으로는 파일명을 바꿔주는 과정이다. 여기서 {0}, {1}, {2}는 format 함수 뒤에 변수들을 순서대로 의미하는 것이다
            # 바꿀 이름의 첫부분은 도시이름이 나와야 하니까 해시의 keys()로 해서 하나를 뽑은 key를 입력
            # 그 다음으로는 번호가 나와야 한다. rjust() 메서드를 이용해서 번호앞에 0을 붙일지 말지 로직을 구성
            # 그래서 지금은 원하는 문자열 길이가 자릿수를 의미하는 k이고, 출력하고자 하는 문자열은 1부터 시작하는 인덱스이니까 str(j+1)이 된다
            # 그리고 길이가 될 때까지 채우는 것은 “0” 이 된다 / 그래서 문자열 길이가 k가 될 때까지 문자열 왼쪽에 "0"이 추가된다
            # 그리고 파일 이름 마지막에는 확장자가 들어가면 되니까 {2} 부분에 해당하는 건 ext로 설정한다
            # ex) file = ‘Warsaw01.png’ 
            file = "{0}{1}.{2}".format(key, str(j+1).rjust(k,'0'), ext)
            # 아래 코드를 입력해서 우리가 지금 뽑은 city라는 2차원 배열에 인덱스로 접근한 리스트 마지막에 file 변수를 추가해준다.
            # city = [[‘myFriends.png’, ‘Warsaw’, ‘2013-09-05 14:07:13’, 2, ‘Warsaw01.png’], [], …] 이렇게 된다
            city[j].append(file)
            # 그래서 city라는 특정 key의 value들을 정렬한 2차원 배열에서 하나씩 뽑아서 위의 과정을 반복
            # 그러다가 특정 key를 뽑는 하나의 For문이 끝나면 hash_map[key] = city 이렇게 hash_map 해시의 value를 city로 대체해준다.
        hash_map[key] = city

    # 위의 과정까지 진행하면 hash_map이라는 해시는 도시이름 key별로 사진 정보가 오름차순 정렬된 리스트들이 2차원 배열로 value가 들어가 있는 상태
    # 이제 원래 인덱스 기준으로 정렬해서 출력하기
    output = []
    # output이라는 리스트를 정의하고, 위에서 정의한 hash_map 해시의 value들만 하나씩 for문으로 뽑기
    # 이 때, value는 key에 대응되는 value가 나오는 것이라서, 처음 for문에서 value를 뽑으면 ‘Warsaw’ key에 해당하는 value인 
    # [[‘myFriends.png’, ‘Warsaw’, ‘2013-09-05 14:07:13’, 2, ‘Warsaw01.png’], 
    # [‘photo.jpg’, ‘Warsaw’, ‘2013-09-05 14:08:15’, 0, ‘Warsaw02.png’], [], …]  ==> 이렇게 2차원 배열이 한꺼번에 뽑아진다
    for value in hash_map.values():
        # 그래서 이렇게 append가 아닌 extend를 해준다 / 그러면 output이라는 변수가 2차원 배열이 되고, 
        # extend이니까 요소만 계속 추가되어서 2차원 배열 형태가 유지되고, 큰 리스트 안에 사진정보 하나의 리스트씩 들어가있게 된다
        output.extend(value)
    
    # 이렇게 위에서 사진정보 리스트 1개씩이 들어간 output 2차원 배열 변수를 만든 상태에서 원래 인덱스를 기준으로 정렬을 해주면 된다
    # output 2차원 배열에서 요소 1개인 하나의 리스트가 x가 된다. 즉, 하나의 리스트에서 원래 인덱스를 나타내는 x[3]를 기준으로 오름차순 정렬을 진행하게 된다
    result = sorted(output, key = lambda x : x[3])
    # 이렇게 만든 result 리스트에서 1개 리스트씩 뽑아서 1개 리스트의 인덱스 4번을 출력해주면 우리가 원하는 형태의 이름인 Warsaw02.jpg를 한 줄씩 출력하게 된다.
    for item in result:
        print(item[4])

# 답을 형식에 따라 맞춰주면 된다.

S = 'photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'

solution(S)


