class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Binary search method
        start = 0 #Start pointer
        end = len(nums) - 1 #End pointer

        while start <= end: #Runs until the start pointer is more than the end pointer
            mid = (start + end) // 2 #Middle

            if nums[mid] == target:
                return mid #When the middle is the target
            elif nums[mid] > target:
                end = mid - 1 #When the middle is higher, make mid-1 the new end
            else:
                start = mid + 1 #If the middle is lower, make the start mid+1
        
        return start #When the start > end then this must be where the number would go if it was in the list