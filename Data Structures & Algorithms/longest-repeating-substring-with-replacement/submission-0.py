class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        ans=mf=0
        m=defaultdict(int)
        for r in range(len(s)):
            m[s[r]]+=1
            mf=max(m.values())
            if r-l+1-mf>k:
                m[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans