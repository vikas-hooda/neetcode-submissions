class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm={}
        for ind,n in enumerate(nums):
            if n in hm and ind-hm[n]<=k:
                return True
            hm[n]=ind
        return False