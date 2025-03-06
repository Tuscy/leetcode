class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        x = 1 #Sets the pointer to 1 as the first number in the list is already unique
        for i in range(1, len(nums)): #Iterates over the numbers in the list starting from index 1
            if nums[i] != nums[i-1]: #If current number is NOT equal to the previous number
                nums[x] = nums[i] #Make that the next value in the list
                x += 1 #Increase the pointer value by 1
        return x