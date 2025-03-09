'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

'''


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []

        answer = [0]*len(temperatures)


        for curr in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[curr],curr))
                continue
            if stack[-1][0] > temperatures[curr]:
                stack.append((temperatures[curr], curr))
            
            else: 
                i = len(stack) -1

                while i >= 0:

                    if stack[i][0] < temperatures[curr]:
                        answer[stack[i][1]] =  curr - stack[i][1]
                        stack.pop()

                    i-= 1
                stack.append((temperatures[curr], curr))

        return answer


if __name__ == "__main__":
    solver = Solution()

    print(solver.dailyTemperatures([73,74,75,71,69,72,76,73]))
