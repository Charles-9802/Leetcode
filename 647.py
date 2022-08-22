# 回文子串
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         dp = [[False for _ in range(len(s))] for _ in range(len(s))]
#         result = 0
#         for i in range(len(s) - 1, -1, -1):
#             for j in range(i, len(s)):  # i<=j
#                 if s[i] == s[j]:
#                     if j - i <= 1:
#                         result += 1
#                         dp[i][j] = True
#                     elif dp[i+1][j-1]:
#                         result += 1
#                         dp[i][j] = True
#         print(dp)
#         return result


class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.extend(s, i, i, len(s))  # 以i为中心
            result += self.extend(s, i, i + 1, len(s))  # 以i和i+1为中心
        return result

    def extend(self, s: str, i: int, j: int, n: int) -> int:
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res


def main():
    s = "abc"
    A = Solution()
    print(A.countSubstrings(s))


if __name__ == "__main__":
    main()
