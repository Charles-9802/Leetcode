class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True


def main():
    A = Solution()
    print(A.canFinish(numCourses=6, prerequisites=[[5, 3], [5, 4], [3, 0], [3, 1], [4, 1], [4, 2]]))


if __name__ == "__main__":
    main()


# i == 0 ： 干净的，未被 DFS 访问
# i == -1 ：其他节点启动的 DFS 访问过了，路径没问题，不需要再访问了
# i == 1  ：本节点启动的 DFS 访问过了，一旦遇到了也说明有环了
