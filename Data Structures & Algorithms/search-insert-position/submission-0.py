class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #last index of num <= target
        l=0
        r=len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l