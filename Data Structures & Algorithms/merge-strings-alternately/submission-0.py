class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        is1=True
        l1=0
        l2=0
        ans=[]
        while l1<len(word1) or l2<len(word2):
            if is1:
                if l1<len(word1):
                    ans.append(word1[l1])
                l1+=1
            else:
                if l2<len(word2):
                    ans.append(word2[l2])
                l2+=1
            is1= not is1
        return "".join(ans)