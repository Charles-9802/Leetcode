class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        if n == 0 and m == 0:
            return 0
        if n == 0 and m != 0:
            return m
        if n != 0 and m == 0:
            return n

        Dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 初始化
        for i in range(n + 1):
            Dp[i][0] = i
        for j in range(m + 1):
            Dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] != word2[j - 1]:
                    Dp[i][j] = min(Dp[i-1][j] + 1, Dp[i][j - 1] + 1, Dp[i - 1][j - 1] + 1)
                else:
                    Dp[i][j] = min(Dp[i - 1][j] + 1, Dp[i][j - 1] + 1, Dp[i - 1][j - 1])
        return Dp[-1][-1]


def main():
    word1 = "horse"
    word2 = "ros"
    A = Solution()
    print(A.minDistance(word1, word2))


if __name__== "__main__":
    main()
