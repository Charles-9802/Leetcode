import random


class Solution:
    def __init__(self, w):
        self.preSum = [0 for _ in range(len(w))]
        self.preSum[0] = w[0]
        self.n = len(w)
        for i in range(1, len(w)):
            self.preSum[i] = self.preSum[i - 1] + w[i]
        self.total = self.preSum[len(w) - 1]

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)  # 左闭右闭
        index = self.binarySearch(rand)
        return index

    def binarySearch(self, target: int) -> int:
        l = 0
        r = self.n - 1
        while l <= r:
            mid = (l + r) // 2
            if self.preSum[mid] == target:
                return mid
            elif self.preSum[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l


A = Solution([1, 2, 4, 3])
print(A.pickIndex())
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()