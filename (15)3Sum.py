"""

Given an integer numsay nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        output = []
        seen = set()
        for i in range(1, len(nums)-1):


            l = 0
            r = len(nums) -1
        
            while l < i and i < r:

                curr_sum = nums[l] + nums[i] + nums[r]
            

                if curr_sum == 0:
                    if l != i and i != r:
                        triplet = tuple(sorted([nums[l],nums[i],nums[r]]))
                        if triplet not in seen:
                            output.append([nums[l],nums[i],nums[r]])
                            seen.add(triplet)

                    l += 1
                    r -=1

                  

                elif curr_sum > 0:
                    r -= 1

                else:
                    l += 1



        return output


if __name__ == "__main__":
    solver = Solution()
    print(solver.threeSum([0,0,0]))
