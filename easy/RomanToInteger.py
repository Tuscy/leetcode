class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        ## Very slow solution (use a Dictionary/Hashmap)
        total=0
        for i, letter in enumerate(s):
            print (total)
            if letter == "I":
                total += 1
            elif letter == "V":
                if s[i-1] =="I" and (i-1) >= 0:
                    total += 3
                else:
                    total += 5
            elif letter == "X":
                if s[i-1] =="I" and (i-1) >= 0:
                    total += 8
                else:
                    total += 10
            elif letter == "L":
                if s[i-1] =="X" and (i-1) >= 0:
                    total += 30
                else:
                    total += 50
            elif letter == "C":
                if s[i-1] =="X" and (i-1) >= 0:
                    total += 80
                else:
                    total += 100
            elif letter == "D":
                if s[i-1] =="C" and (i-1) >= 0:
                    total += 300
                else:
                    total += 500
            elif letter == "M":
                if s[i-1] =="C" and (i-1) >= 0:
                    total += 800
                else:
                    total += 1000
        return total