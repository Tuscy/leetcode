class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxtotal = float('-inf') #Output val set to max -ve (so that any initial -ve will be higher)
        current = 0 #Current sum

        for x in nums: #Iterate over all the numbers
            current += x #Add current number to the current total

            if current > maxtotal: #If the current sum is more than the stored max
                maxtotal = current #Set the current to max

            if current < 0: #If the current became <0 then reset
                current = 0

        return maxtotal