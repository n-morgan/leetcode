
""" 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        longest = 0 
        elts_set = set(nums)
        starters = []
        for elt in nums: 
            
            if (elt -1) not in elts_set:
                starters.append(elt)


        for elt in starters:
            curr_length  = 0
            
            while elt + curr_length in elts_set: 
                curr_length += 1

            longest = max(longest, curr_length)

        return longest 




if __name__ == "__main__":
    solver = Solution()
    
    print(solver.longestConsecutive([1,2,3,100,4,10]))
            
                
