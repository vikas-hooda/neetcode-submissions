class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=defaultdict(int)
        for c in s:
            m[c]+=1
        for c in t:
            m[c]-=1
        for k in m:
            if m[k]:
                return False
        return True