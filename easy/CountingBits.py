class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] #Sets initial bit to 0

        for i in range(1, n+1):
            binary = bin(i)[2:] #Get the binary value without the 0b start
            count = 0 #1s Counter
            for x in binary: #For every 1 in the binary value add 1
                if int(x) == 1: 
                    count += 1
            bits.append(count) #Append to list

        return bits
    
    ##Fastest way would be to use odd and even values to determine number of 1s
    