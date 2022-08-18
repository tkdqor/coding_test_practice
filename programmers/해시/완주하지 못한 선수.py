# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 1번째 방법 = 두 리스트를 sorting하고 completion 리스트의 length만큼 돌면서 participant 리스트에 존재하지 않는 선수 찾기
# for문으로 돌다가 if문으로 participant 리스트에는 없는 요소가 있다면 그게 바로 완주하지 못한 선수가 된다
# 그렇게 다 돌아도 없을 경우에는, 마지막 주자가 완주하지 못한 선수가 된다

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[len(participant) - 1]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

# 2번째 방법 = Hash를 이용해서 문제 풀기
# participant 리스트에 있는 선수들을 가지고 hash 맵을 하나 만든다. 선수들의 이름을 가지고 hash 값을 만들고 그 hash 값을 key / 선수들의 이름을 value로 하는
# 하나의 딕셔너리를 만드는 것이다. 
# ex) participant = ['C', 'A', 'B']라면, { key = 17 : value = C }, { key = 5 : value = A }, { key = 13 : value = B } 이렇게 만들어준다
# 이렇게 hash 맵을 만들고나서 key 값들을 다 합쳐준다. 여기서는 총 35가 된다. (즉, participant 리스트의 hash를 구하고, hash 값을 더한다)
# 그 다음으로는 completion 배열을 쭉 돌면서 선수들의 key 값들을 뺴주는 것이다. (즉, completion 리스트의 hash를 빼준다)
# Ex) completion = ['C', 'B']라면, 총 35에서 C인 17를 빼주고 -> B의 13을 빼주면 5가 된다. 
# 우리가 만들어놓은 hash 맵에서 5라는 key를 가지고 쫓아가보면 완주하지 못한 선수 A가 나오게 된다. 

def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    for comp in completion:
        sumHash -= hash(comp)
    
    return hashDict[sumHash]  