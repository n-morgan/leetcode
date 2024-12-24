"""

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

"""



class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        

        def isanagram(s, t):

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
        anagrams = {}
        for word in strs:
            x = False
            for anagram in anagrams.keys():
                if isanagram(word, anagram):
                    anagrams[anagram].append(word)
                    x = True

            if not x:
                anagrams[word] = [word]
        output = [] 
        for group in anagrams.values():
            output.append(group)

        return output 


if __name__ == "__main__":
    
    solver = Solution()

    print(solver.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))





            


