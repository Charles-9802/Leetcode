# 最长重复子数组
# 连续
class Solution:
    def findLength(self, nums1, nums2) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        result = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
            print(dp)
        return result


# class Solution:
#     def findLength(self, nums1, nums2) -> int:
#         dp = [0] * (len(nums2) + 1)
#         result = 0
#         for i in range(1, len(nums1) + 1):
#             for j in range(len(nums2), 0, - 1):
#                 if nums1[i - 1] == nums2[j - 1]:
#                     dp[j] = dp[j - 1] + 1
#                 else:
#                     dp[j] = 0   # 注意这里不相等的时候要有赋0的操作
#                 print(dp)
#                 result = max(result, dp[j])
#         return result

def main():
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    A = Solution()
    print(A.findLength(nums1, nums2))


if __name__== "__main__":
    main()
