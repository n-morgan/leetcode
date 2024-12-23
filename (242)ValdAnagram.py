"""

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

"""

import sys

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False 


        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1

        for letter in t:
            if letter not in letters:
                return False
            if letters[letter] == 0:
                return False

            letters[letter] -= 1

        return True
             


if __name__ == "__main__": 

    solver = Solution()
    print(solver.isAnagram(sys.argv[1], sys.argv[2]))
