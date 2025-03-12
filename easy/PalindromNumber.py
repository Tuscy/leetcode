class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): #Check for minus numbers and any numbers ending in 0 but not 0
            return False
        reverseNum = 0
        while x > reverseNum: #While the new number is smaller than x
            reverseNum = reverseNum * 10 + x % 10 #Add on the modulo of the number in increments of 10 (each digit) 
            x //= 10 #Then remove the digit from x
        return x == reverseNum or x == reverseNum // 10 #Return true if its equal/equal without the middle number (odd number)