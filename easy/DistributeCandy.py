class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        toEat = len(candyType)/2 #Find n
        output = 0
        eaten = {}

        for i in candyType: #For each candy 
            if output < toEat: #Check n has not been reached
                if i not in eaten: #If the candy has NOT been eaten
                    eaten[i] = 1 #Add candy to hashmap
                    output += 1 #Increase eaten
            else:
                break

        return output 
    
    ##This can be done faster using sets - this version is better for memory usage