class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1 #Set the final value index
        for x in reversed(nums): #Iterate backwards to avoid incorrect indexes
            if x == 0:
                nums.pop(index) #When 0 remove from list
                nums.append(0)  #Replace with a 0 at the end
            index -= 1 #Decrement current index