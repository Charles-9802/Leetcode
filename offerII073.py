# 狒狒吃香蕉
# 狒狒喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。
# 狒狒可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉，下一个小时才会开始吃另一堆的香蕉。
# 狒狒喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
# 返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

class Solution:
    def check(self, piles, mid):
        tmp = 0
        for i in range(len(piles)):
            if piles[i] % mid == 0:
                tmp += piles[i] // mid
            else:
                tmp += (piles[i] // mid + 1)
        return tmp

    def minEatingSpeed(self, piles, h):
        piles.sort()
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            if self.check(piles, mid) <= h:
                r = mid - 1
            else:
                l = mid + 1
        return r + 1


A = Solution()
# print(A.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
# print(A.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
# print(A.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
print(A.minEatingSpeed([312884470], 312884469))