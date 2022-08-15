class Solution:
    def subsets(self, nums):
        res = []
        result = []
        def backtracking(nums, index):
            result.append(res[:])

            for i in range(index, len(nums)):
                res.append(nums[i])
                backtracking(nums, i + 1)
                res.pop()
        backtracking(nums, 0)
        return result
A = Solution()
print(A.subsets([1, 2, 3]))