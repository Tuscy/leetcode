class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for count, i in enumerate(image): #Iterates over image lists
            i.reverse() #Reverses each list
            for index, x in enumerate(i): #Iterates over each int in each list
                image[count][index] = x^1 #XOR with 1 mask to inverse the bits

        return image