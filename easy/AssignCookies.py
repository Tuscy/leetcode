class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        total = 0
        
        #Sort both lists
        g.sort()
        s.sort()

        for i in s:
            if i >= g[total]: #For each cookie check if its size >= each childs need
                total += 1
                if total == len(g): #When the child index reaches the length of the list its complete
                    break

        return total