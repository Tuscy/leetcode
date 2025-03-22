class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        #Traverse the list from the last element to the first
        for i in range(len(digits)-1, -1, -1):
            #If the current digit is 9, set it to 0
            if digits[i] == 9:
                digits[i] = 0
            else:
                #Otherwise increment it by 1 and return the list
                digits[i] = digits[i] + 1
                return digits
        #If all numbers were 9 in the list add 1 to the start of the list
        return [1] + digits