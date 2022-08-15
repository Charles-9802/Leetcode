class Solution:
    def combine(self, n, k):
        res = []
        result = []
        def backtracking(n, k, index):
            if len(res) == k:
                result.append(res[:])
                return

            for i in range(index, n + 1):
                res.append(i)
                backtracking(n, k, i + 1)
                res.pop()
        backtracking(n, k, 1)
        return result
S = Solution()
print(S.combine(4, 2))