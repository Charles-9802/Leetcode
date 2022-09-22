class Solution:
    def lastStoneWeightII(self, stones) -> int:
        _sum = sum(stones)
        mid = _sum // 2
        dp = [0] * (mid + 1)
        for i in range(len(stones)):
            for j in range(mid, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return _sum - dp[-1] * 2

def main():
    A = Solution()
    print(A.lastStoneWeightII([2, 7, 4, 1, 8, 1]))


if __name__ == "__main__":
    main()