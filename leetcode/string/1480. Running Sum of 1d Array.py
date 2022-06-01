# Leetcode를 VSCode로 옮길 때 이렇게 List를 import 해주기
from typing import List

# LeetCode는 이렇게 클래스와 함수를 기본으로 주고
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        
        for i in range(len(nums)):
            answer.append(sum(nums[0:i+1]))
        
        return answer
# 여기까지 작성하게끔 되어있다.

# 이걸 VSCode에서 실행하기 위해 인스턴스를 만들고 함수를 실행시켜주기 - nums는 예시로 [1,2,3,4]를 넣어주기
result = Solution()
print(result.runningSum([1,2,3,4]))
