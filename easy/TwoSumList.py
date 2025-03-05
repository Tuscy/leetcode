
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #My Solution (Accepted but very slow)
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y:
                    if nums[x] + nums[y] == target:
                        return[x, y]
        

        #The best solution
        num_map = {}  # Hash table to store number and its index
        for i, num in enumerate(nums): ####Used to iterate a list with a counter (i)
            complement = target - num  # Find the complement
            if complement in num_map:
                return [num_map[complement], i]  # Return indices of complement and current number
            num_map[num] = i  # Store the number with its index