class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = list(set(nums))
        nums.sort()
        _max = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
               res += 1
            else:
                _max = max(res, _max)
                res = 1
            _max = max(res, _max)
        return _max

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         s, res = set(nums), 0
#         for num in nums:
#             if num - 1 not in s:
#                 t = 1
#                 next = num + 1
#                 while next in s:
#                     t += 1
#                     next += 1
#                 res = max(res, t)
#         return res


def main():
    A = Solution()
    print(A.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))


if __name__ == "__main__":
    main()
