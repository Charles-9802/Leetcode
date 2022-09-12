import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.minHeap = []
        for x in nums:
            heapq.heappush(self.minHeap, x)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
