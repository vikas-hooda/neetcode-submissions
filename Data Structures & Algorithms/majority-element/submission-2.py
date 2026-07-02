class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me=nums[0]
        c=1
        for n in nums:
            if c==0:
                me=n
            if me==n:
                c+=1
            else:
                c-=1
        return me