class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*n
        suf=[1]*n
        t=1
        for i in range(n):
            t*=nums[i]
            pre[i]=t
        t=1
        for i in range(n-1,-1,-1):
            t*=nums[i]
            suf[i]=t
        ans=[1]*n
        for i in range(n):
            if i>0:
                ans[i]=pre[i-1]
            if i<n-1:
                ans[i]*=suf[i+1]
        return ans