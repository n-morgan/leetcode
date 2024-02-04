class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1

        while( j > i ):
            # print(s[i], s[j])
            while i < len(s) - 1 and not s[i].isalpha():
                i += 1
            while j > 1 and not s[j].isalpha():
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1

            else: 
            
                return False
        
        return True


s = "A man, a plan, a canal: Panama"
s = ".,"
test = Solution()
print(test.isPalindrome(s))
