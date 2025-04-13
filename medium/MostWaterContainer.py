class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Pointers + output val
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right: #Until pointers cross
            currentArea = min(height[left], height[right]) * (right - left) #Calc the current area
            maxArea = max(maxArea, currentArea) #Compare max to current

            if height[left] < height[right]: #Move whichever pointer has the lowest height
                left += 1
            else:
                right -= 1

        return maxArea
            