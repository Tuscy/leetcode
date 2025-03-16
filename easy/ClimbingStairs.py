class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1 #Return if 1 step
        if n == 2:
            return 2 #2 Steps
        
        a, b = 1, 2  #Using the fibonachi method
        for _ in range(2, n):
            a, b = b, a + b  
            
        return b
