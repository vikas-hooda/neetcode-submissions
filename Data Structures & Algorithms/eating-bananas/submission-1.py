class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(k):
            return sum([x//k if not x%k else x//k + 1 for x in piles])<=h
        l=1
        r=sum(piles)
        while l<r:
            m=l+(r-l)//2
            if isValid(m):
                r=m
            else:
                l=m+1
        return l