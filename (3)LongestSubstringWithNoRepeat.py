"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def not_repeating(snippet):
            return len(set(snippet)) == len(snippet)
        
        l = 0
        longest = float("-inf")
        
        for r in range(len(s)+1):
            if not_repeating(s[l:r]):
                if r - l > longest:
                    longest = r - l 
            else:
                l += 1 
        return longest



if __name__ == "__main__":

    solver = Solution()
    example = "bbbbb"
    print(solver.lengthOfLongestSubstring(example))


