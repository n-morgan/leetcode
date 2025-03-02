'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true 

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = [] 
        openings  = set(["(","[","{"])
        closures = set([")","]","}"])

        matches = {")": "(",
                   "]":"[",
                   "}":"{"}


        for elt in s:
            if elt in openings:
                stack.append(elt)
            elif elt in closures: 
                if not stack:
                    return False
                if stack[-1] ==  matches[elt]:
                    stack.pop()
                else: 
                    return False
        
        if len(stack) == 0:
            return True
        return False
        

if  __name__ == "__main__":
    solver = Solution()
    print(solver.isValid("["))
