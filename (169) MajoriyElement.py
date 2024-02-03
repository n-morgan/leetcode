class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ele_dict = {}
        for ele in nums:
            if ele not in ele_dict:
                ele_dict[ele] = 0
            else:
                ele_dict[ele] += 1 
        return max(ele_dict,key = ele_dict.get) 
        
test = Solution()
print(test.majorityElement([3,3,4]))