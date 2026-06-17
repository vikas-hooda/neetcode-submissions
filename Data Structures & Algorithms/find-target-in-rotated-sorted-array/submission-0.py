class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l,h):
            while l<=h:
                m=l+(h-l)//2
                if nums[m]==target:
                    return m
                elif nums[m]>target:
                    h=m-1
                else:
                    l=m+1
            return -1
        if nums[0]<=nums[-1]:
            return bs(0,len(nums)-1)
        l=0
        r=len(nums)-1
        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        r=bs(0,l-1)
        return bs(l,len(nums)-1) if r==-1 else r