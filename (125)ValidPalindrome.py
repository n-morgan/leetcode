"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """



        def strip_string(string):
            output = ""
            valid=set("abcdefghijklmnopqrstuvwxyz")
            for elt in string:
                normalized = elt.lower()
                if normalized in valid:
                    output+= normalized
            return output

        def flip_compare(stripped):
            
            stripped_reversed = stripped [::-1]
            print(f"{stripped} \n {stripped_reversed}")
            return stripped==stripped_reversed



        stripped = strip_string(s)
        return flip_compare(stripped)


if __name__ == "__main__":

    solver = Solution()
    print(solver.isPalindrome("A man, a plan, a canal: Panama"))
