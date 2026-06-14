class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m=defaultdict(list)
        for s in strs:
            t=[0]*26
            for c in s:
                t[ord(c)-ord('a')]+=1
            m[tuple(t)].append(s)
        ans=[]
        for k in m:
            ans.append(m[k])
        return ans