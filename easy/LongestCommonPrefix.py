class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        
        for i in strs:
            if not i.startswith(common):
                for x in reversed(range(len(common))):
                    if i.startswith(common[:x]):
                        common = common[:x]
                        break

        return common