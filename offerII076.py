# 从大到小排序->快速排序
# class Solution:
#     def partition(self, nums, l, r):
#         tmp = nums[l]
#         while l < r:
#             while l < r and nums[r] <= tmp:
#                 r -= 1
#             nums[l] = nums[r]
#             while l < r and nums[l] >= tmp:
#                 l += 1
#             nums[r] = nums[l]
#         nums[l] = tmp
#         return l
#
#     def findKthLargest(self, nums, k):
#         r = len(nums) - 1
#         l = 0
#         while True:
#             index = self.partition(nums, l, r)
#             if index == k - 1:
#                 return nums[index]
#             elif index > k - 1:
#                 r = index - 1
#             else:
#                 l = index + 1
# A = Solution()
# print(A.findKthLargest([3, 2, 1, 5, 6, 4], 2))

# 堆排序
# 建小根堆, 大小为K
class Solution:
    def sift(self, nums, low, high):
        i = low
        j = 2 * i + 1
        tmp = nums[low]
        while j <= high:
            if j + 1 <= high and nums[j+1] < nums[j]:
                j = j + 1
            if nums[j] < tmp:
                nums[i] = nums[j]
                i = j
                j = 2 * i + 1
            else:
                break
        nums[i] = tmp

    def findKthLargest(self, nums, k):
        heap = nums[0:k]
        # 建堆，大小为K
        for i in range((k - 2) // 2, -1, -1):
            self.sift(heap, i, k - 1)
        # 往堆里加剩下的n-k个数，并重新变为小根堆
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                self.sift(heap, 0, k - 1)
        # 堆顶为第K大数
        return heap[0]

# # 建大根堆
# class Solution:
#     def sift(self, nums, low, high):
#         i = low
#         j = 2 * i + 1
#         tmp = nums[low]
#         while j <= high:
#             if j + 1 <= high and nums[j+1] > nums[j]:
#                 j = j + 1
#             if nums[j] > tmp:
#                 nums[i] = nums[j]
#                 i = j
#                 j = 2 * i + 1
#             else:
#                 break
#         nums[i] = tmp
#
#     def findKthLargest(self, nums, k):
#         n = len(nums)
#         for i in range((n - 2) // 2, -1, -1):
#             self.sift(nums, i, n - 1)
#         for i in range(n - 1, -1, -1):
#             nums[0], nums[i] = nums[i], nums[0]
#             self.sift(nums, 0, i - 1)
#         return nums[-k]


A = Solution()
print(A.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
