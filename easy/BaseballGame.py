class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out = [] #Temp value store
        count = -1
        total = 0

        for i in operations:
            if i == "C": #When C remove the last value and decrement count
                out.remove(out[count])
                count -= 1
            elif i == "D": #When D double the last value and increment count
                out.append(out[count]*2)
                count += 1
            elif i == "+": #When + sum last 2 values and increment count
                out.append(out[count] + out[count-1])
                count += 1
            else: #Otherwise must be a number, add number as int to list and increment count
                out.append(int(i))
                count += 1
        
        for i in out:
            total += i
        
        return total