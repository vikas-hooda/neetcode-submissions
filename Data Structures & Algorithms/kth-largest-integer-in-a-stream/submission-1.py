class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.mh=nums[:k]
        heapq.heapify(self.mh)
        for n in nums[k:]:
            heapq.heappush(self.mh,n)
            heapq.heappop(self.mh)

    def add(self, val: int) -> int:
        heapq.heappush(self.mh,val)
        if len(self.mh)>self.k:
            heapq.heappop(self.mh)
        return self.mh[0]
