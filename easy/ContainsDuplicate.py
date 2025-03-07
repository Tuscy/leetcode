class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set()
        for x in nums:
            if x in numSet:
                return True
            else:
                numSet.add(x)
        return False