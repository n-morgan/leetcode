class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                del nums[idx]
                count += 1 
            
            else:
                idx += 1
        return count

    
sol = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 0
print(sol.removeElement(nums, val))
print(nums)