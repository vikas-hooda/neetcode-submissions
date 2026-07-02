class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for s in strs:
            j=0
            while j< min(len(prefix), len(s)) and s[j]==prefix[j]:
                j+=1
            prefix=prefix[:j]
        return prefix