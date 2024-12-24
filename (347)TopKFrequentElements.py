"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1 

        
        inv_freq = {}
        for key,value in freq.items():
            if value not in inv_freq:
                inv_freq[value] = []
            inv_freq[value].append(key) 

        sorted_freq = sorted(inv_freq.keys())
        output = []
        
        iters = k
        
        while iters  >0 and sorted_freq: # empty array is Falsy 
            top = sorted_freq.pop() 
            for elt in inv_freq[top]:
                output.append(elt)
                iters -= 1
        return output
        
    


if __name__ == "__main__":
    solver = Solution()
    print(solver.topKFrequent([1,1,1,1,2,2,3],2))



    


    
