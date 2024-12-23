"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


"""

import sys

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        print(nums, target)
        for p1,ele1 in enumerate(nums):
            compliment = target - ele1

            for p2,ele2 in enumerate(nums):
                if p1 != p2 and ele2 == compliment:
                    return [p1,p2]

if __name__ == "__main__":

    solver = Solution()
    
    print(solver.twoSum([3,3], 6))
    print("I EXECUTED")
