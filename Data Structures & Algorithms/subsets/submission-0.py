class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subsets=[[]]
        for n in nums:
            subsets+=[s+[n] for s in subsets]
        return subsets