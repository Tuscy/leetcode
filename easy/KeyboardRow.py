class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        #All letters mapped to their keyboard row
        letters = {
            'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
            'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
            'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3
        }

        for i in words:
            lowercase = i.lower()  #For every word, store its lowercase version
            row = letters[lowercase[0]] #Store the keyboard row of the first letter 

            if all(letters[char] == row for char in lowercase): #If all the letters are the same row as "row"
                output.append(i) #Append it to the output list
                
        return output