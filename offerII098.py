class Solution:
    # 1 1
    # 1 2
    # 1
    def uniquePaths(self, m: int, n: int) -> int:
        maze = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            maze[0][i] = 1
        for j in range(m):
            maze[j][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                maze[j][i] = maze[j][i-1] + maze[j-1][i]
        return maze[-1][-1]
A = Solution()
print(A.uniquePaths(3, 7))
