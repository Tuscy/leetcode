class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        #Check each bill
        for i in bills:
            if i == 5: #If its a 5
                fives += 1            
            elif i == 10: #If its a 10 
                if fives > 0:
                    fives -= 1 #Give 5 in change
                else:
                    return False #Not enough change
                tens += 1
            else: #If its a 20 
                if fives > 0 and tens > 0: #Check theres enough change
                    fives -= 1
                    tens -= 1
                elif fives > 2: #Otherwise check change in 5s
                    fives -= 3
                else:
                    return False #Not enough change
                            
        return True
        