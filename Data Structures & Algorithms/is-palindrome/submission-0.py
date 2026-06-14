class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s=[c.lower() for c in s if c.isalnum()]
        print(s)
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True