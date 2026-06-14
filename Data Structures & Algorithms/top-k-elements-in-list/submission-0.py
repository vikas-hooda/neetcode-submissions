class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=defaultdict(int)
        for n in nums:
            m[n]+=1
        h=[]
        for n in m:
            heapq.heappush(h,[m[n],n])
            if len(h)>k:
                heapq.heappop(h)
        return [n[1] for n in h]