'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 
'''
from heapq import heapify, heappush, heappop

class MinStack(object):

    def __init__(self):
        
        self.stack = [] 
        self.heap = []
        heapify(self.heap)


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        heappush(self.heap, val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        heappop(self.heap)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """

        return self.heap[0]

        

if __name__ == "__main__":
# Your MinStack object will be instantiated and called as such:

    minStack = MinStack()
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    print(minStack.getMin()); # return -3
    minStack.pop();
    print(minStack.top());  # return 0
    print(minStack.getMin()); # return -2




