class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        
        for i in range(len(s)-1):
            # s의 마지막 데이터를 제외하고 나머지를 검토
            num = dic[s[i]]
            nextNum = dic[s[i+1]]
            if (num>=nextNum):
                result += num
            else:
                result -= num
        
        # s의 마지막 데이터를 검토해서 숫자 더하기
        result += dic[s[len(s)-1]]

        return (result)

answer = Solution()
print(answer.romanToInt("MCMXCIV"))

# range(4) 이러면 0,1,2,3까지 출력
