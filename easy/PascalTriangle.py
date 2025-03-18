class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #Returning the base values
        if numRows == 0:
            return [] 
        if numRows == 1:
            return [[1]]

        lastRows = self.generate(numRows - 1) #Calls the function for each row decrementing each time
        lastRow = lastRows[-1] #Stores the last row
        row = [1] #Add the intial one to the current row

        for i in range(1, numRows-1):
            row.append(lastRow[i-1] + lastRow[i]) #Find the sum of the 2 numbers from the previous row
        
        row.append(1) #Add the last one
        lastRows.append(row)

        return lastRows