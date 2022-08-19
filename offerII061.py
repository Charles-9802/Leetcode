# class Solution:
#     def kSmallestPairs(self, nums1, nums2, k: int):
#         result = []
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 result.append([nums1[i], nums2[j]])
#         result.sort(key=lambda x: x[0]+x[1])
#         return result[0:k]

import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        Q = []
        n = 0
        for a in nums1[:k]:
            for b in nums2[:k]:
                heapq.heappush(Q, (-a - b, [a, b]))
                if n < k:
                    n += 1
                else:
                    heapq.heappop(Q)
        return [q for _, q in Q]


def main():
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    A = Solution()
    print(A.kSmallestPairs(nums1, nums2, k))


if __name__ == "__main__":
    main()
