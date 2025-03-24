class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = 0
        for i in nums: #Xor each bit in the list
            XOR = XOR ^ i #This will cancel out every duplicate bit
        
        return XOR
        