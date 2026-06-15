class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        l=0
        r=0
        m1=defaultdict(int)
        m2=defaultdict(int)
        for c in s1:
            m1[c]+=1
        
        while r<len(s1):
            m2[s2[r]]+=1
            r+=1
        r-=1
        if m1==m2:
            return True
        while r<len(s2)-1:
            r+=1
            m2[s2[r]]+=1
            m2[s2[l]]-=1
            if m2[s2[l]]==0:
                del m2[s2[l]]
            l+=1
            if m1==m2:
                return True
        return False
