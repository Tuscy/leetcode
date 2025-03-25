class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: #Nums is empty
            return []
        
        ranges = [] #Final list of ranges
        start = nums[0] #Pointer for current start of range

        for i in range(1, len(nums)): 
            if nums[i] != nums[i-1] + 1: #If the consecutive numbers stop
                if start == nums[i-1]: #If the start is the same as the end
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(nums[i-1])) #When there is a range bigger than 1 add ->
                start = nums[i] #Set the new start

        #Taking care of the final range (due to the previous for loop missing out the very last digit)
        if start == nums[-1]: 
            ranges.append(str(start)) #If the final number is a single
        else:
            ranges.append(str(start) + "->" + str(nums[-1])) #If the final range is not a single

        return ranges
