class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm=defaultdict(int)
        for c in s:
            hm[c]+=1
        for c in t:
            hm[c]-=1
        for k,v in hm.items():
            if v:
                return False
        return True