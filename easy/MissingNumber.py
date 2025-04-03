class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summation = 0

        #Iterate over the range and sum all numbers
        for i in range(len(nums)+1):
            summation += i

        return summation - sum(nums) #Find the difference between expected sum and given sum
