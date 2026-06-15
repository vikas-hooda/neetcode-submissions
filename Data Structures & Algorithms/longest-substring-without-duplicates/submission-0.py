class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        l=r=ans=0
        while r<len(s):
            while s[r] in d:
                d.remove(s[l])
                l+=1
            d.add(s[r])
            ans=max(ans,r-l+1)
            r+=1
        return ans