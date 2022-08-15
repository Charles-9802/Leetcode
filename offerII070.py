class Solution:
    def singleNonDuplicate(self, nums):
        slow = 0
        fast = 1
        while slow < len(nums) and fast < len(nums):
            if nums[slow] == nums[fast]:
                slow += 2
                fast += 2
            else:
                return nums[slow]
        return nums[-1]


A = Solution()
print(A.singleNonDuplicate([1]))
print(A.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
