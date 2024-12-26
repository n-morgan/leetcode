"""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """




        def suffix(array):
            suffix_memo = {}
            output = []

            for i in range(len(array)-1,-1,-1):
                if i == len(array)-1:
                    output.insert(0,4)
                    suffix_memo[i] = array[len(array)-1]
                else: 
                    curr = array[i]*suffix_memo[i+1]
                    suffix_memo[i] = curr
                    output.insert(0,curr)
            

            return suffix_memo

        def prefix(array):
            prefix_memo = {}
            output = []

            for i in range(len(array)):
                if i == 0:
                    output.append(0)
                    prefix_memo[i] = array[i]
                else: 
                    curr = array[i] * prefix_memo[i-1]
                    prefix_memo[i] = curr 
                    output.append(curr)

            return prefix_memo

        def compute_sum(array):
            suffix_memo = suffix(array)
            prefix_memo = prefix(array)
            
            output = []
            for i in range(len(array)):
                if i == 0:
                    output.append(suffix_memo[i+1])
                elif i == len(array)-1:
                    output.append(prefix_memo[i-1])
                else: 
                    output.append(prefix_memo[i-1]*suffix_memo[i+1])

            return output

        return compute_sum(nums)


if __name__ == "__main__":
    
    solver = Solution()
    print(solver.productExceptSelf([1,2,3,4]))

