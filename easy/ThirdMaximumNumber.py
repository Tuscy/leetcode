class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')

        for x in nums:
            if x > third and x != second and x!= first:
                if x > second:
                    if x > first:
                        third = second
                        second = first
                        first = x                        
                    else:
                        third = second
                        second = x
                else:
                    third = x

        if third > float('-inf'):
            return third
        else:
            return first