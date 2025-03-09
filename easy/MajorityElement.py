class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Intial Try
        numHash = {}
        for x in nums:
            if x in numHash:
                numHash[x] += 1
            else:
                numHash[x] = 1
            if numHash[x] > (len(nums)/2):
                return x
            
        ##Best solution
                count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate