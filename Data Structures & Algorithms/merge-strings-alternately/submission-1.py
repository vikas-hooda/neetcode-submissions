class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        m=len(word1)
        n=len(word2)
        i=j=0
        while i<m or j<n:
            if i<m:
                ans.append(word1[i])
            if j<n:
                ans.append(word2[j])
            i+=1
            j+=1
        return "".join(ans)