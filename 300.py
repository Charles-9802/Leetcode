class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            _max = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    _max = max(dp[j], _max)
                    dp[i] = _max + 1
        return max(dp)


def main():
    # nums = [0, 1, 0, 3, 2, 3]
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [7, 7, 7, 7, 7, 7, 7]
    A = Solution()
    print(A.lengthOfLIS(nums))


if __name__== "__main__":
    main()
