# 剑指 Offer II 060. 出现频率最高的 k 个数字
import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        heap = []
        for key, val in dic.items():
            if len(heap) == k:
                if val > heap[0][0]:
                    heapq.heapreplace(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        return [h[1] for h in heap]

def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    A = Solution()
    print(A.topKFrequent(nums, k))


if __name__ == "__main__":
    main()