class Solution:
    def canPartition(self, nums):
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        target = _sum // 2
        dp = [0 for _ in range(target + 1)]
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[-1] == target

def main():
    A = Solution()
    print(A.canPartition([2, 2, 1, 1]))


if __name__ == "__main__":
    main()