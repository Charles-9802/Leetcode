class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        res = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                res = max(count, res)
                count = 1
        res = max(count, res)
        return res


def main():
    # nums = [1, 3, 5, 4, 7]
    # nums = [2, 2, 2, 2, 2]
    nums = [1, 3, 5, 7]
    A = Solution()
    print(A.findLengthOfLCIS(nums))


if __name__== "__main__":
    main()
