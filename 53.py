class Solution:
    def maxSubArray(self, nums) -> int:
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # result = dp[0]
        # for i in range(1, len(nums)):
        #     dp[i] = max(dp[i-1] + nums[i], nums[i])
        #     result = max(result, dp[i])     # result 保存dp[i]的最大值
        # return result
        result = nums[0]
        sum = result
        for i in range(1, len(nums)):
            if sum <= 0:
                sum = 0
            sum += nums[i]
            result = max(result, sum)
        return result


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    # nums = [5, 4, -1, 7, 8]
    A = Solution()
    print(A.maxSubArray(nums))


if __name__ == "__main__":
    main()

