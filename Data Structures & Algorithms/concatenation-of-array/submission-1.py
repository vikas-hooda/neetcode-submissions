class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2*len(nums)):
            j=i if i<len(nums) else i-len(nums)
            ans.append(nums[j])
        return ans