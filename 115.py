# 不同子序列，只用删除
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for j in range(len(t) + 1):
            dp[0][j] = 0
        dp[0][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

                #   bagg 和 bag
                #   用 bag 和 ba
                #   不用 bag 和 bag

                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


def main():
    s = "rabbbit"
    t = "rabbit"
    A = Solution()
    print(A.numDistinct(s, t))


if __name__ == "__main__":
    main()
