class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        dict_rn = {"I": 1,"V": 5, "X" : 10, "L":50, "C":100, "D":500, "M":1000}
        for idx in range(len(s)):
            if idx > 0:
                if s[idx] == "V" or s[idx] == "X":
                    if s[idx - 1] == "I":
                        sum += dict_rn[s[idx]] - 2
                        continue
                if s[idx] == "L" or s[idx] == "C":
                    if s[idx - 1] == "X":
                        sum += dict_rn[s[idx]] - 20
                        continue
                if s[idx] == "D" or s[idx] == "M":
                    if s[idx - 1] == "C":
                        sum += dict_rn[s[idx]] - 200
                        continue
            sum += dict_rn[s[idx]]
        return sum
    

s = "MCMXCIV"
test = Solution()
print(test.romanToInt(s))