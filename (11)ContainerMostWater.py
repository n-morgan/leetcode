"""

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height)-1


        maximum = float('-inf')

        def cal_area(i,j):
            return (min(height[i],height[j])*abs(j-i))

        while l < r:
            curr_area = cal_area(l, r)
            maximum = max(curr_area, maximum)

            l_height = height[l]

            r_height = height[r]

            if r_height > l_height:
                l += 1
            elif l_height  > r_height:
                r -= 1
            else:
                l += 1 
                r -= 1 

        return maximum
            

if __name__ == "__main__":

    solver = Solution()
    print(solver.maxArea([1,8,6,2,5,4,8,3,7]))
