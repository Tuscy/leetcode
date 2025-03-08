class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    
        while True: #Run until break
            if val in nums: #Checks if the value is in the list
                nums.remove(val) #Removes if ture
            else:
                break #If not true then ends the loop

        ##Can be shortend to this
        while val in nums:
            nums.remove(val)
        return len(nums)
    
    

   
        