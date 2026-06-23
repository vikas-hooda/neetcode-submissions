class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            if not a==b:
                heapq.heappush(stones,-abs(abs(a)-abs(b)))
        return -stones[0] if len(stones) else 0