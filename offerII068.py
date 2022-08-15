class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        return l


A = Solution()
print(A.searchInsert(nums = [1,3,5,6], target = 5))
print(A.searchInsert(nums = [1,3,5,6], target = 2))
print(A.searchInsert(nums = [1,3,5,6], target = 7))
print(A.searchInsert(nums = [1,3,5,6], target = 0))
print(A.searchInsert(nums = [1], target = 0))