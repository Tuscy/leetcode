class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0 

        for i in range(len(grid)): #Iterate through the rows
            for j, water in enumerate(grid[i]): #For each row find the value and its index
                if water == 1: #Check if each cell contains land

                    #Then check each adjoining cell if there is water OR if it is a border
                    if (j > 0 and grid[i][j-1] == 0) or j == 0:
                        perimeter += 1 #Add one when either is true

                    if (i > 0 and grid[i-1][j] == 0) or i == 0:
                        perimeter += 1
                    
                    if (j < (len(grid[0]) - 1) and grid[i][j+1] == 0) or j == len(grid[0]) - 1:
                        perimeter += 1
                    
                    if (i < (len(grid) - 1) and grid[i+1][j] == 0) or i == len(grid) - 1:
                        perimeter += 1

        return perimeter #Return the total 