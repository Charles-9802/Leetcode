# 编辑距离

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # 初始化
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] != word2[j - 1]:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]


def main():
    word1 = "horse"
    word2 = "ros"
    A = Solution()
    print(A.minDistance(word1, word2))


if __name__== "__main__":
    main()
