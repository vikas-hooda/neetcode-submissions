class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mtn=prices[0]
        ans=0
        for p in prices:
            ans=max(ans,p-mtn)
            mtn=min(mtn,p)
        return ans