class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        k=1
        def cp(l,r):
            nonlocal k
            if l>=r:
                return True
            if s[l]!=s[r]:
                if not k:
                    return False
                k-=1
                return cp(l+1,r) or cp(l,r-1)
            return cp(l+1,r-1)
        return cp(l,r)
                