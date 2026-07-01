class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me=nums[0]
        runLen=1
        for n in nums[1:]:
            if runLen==0:
                    me=n
            if n==me:
                runLen+=1
            else:
                runLen-=1
                
        return me