class Solution:
    def peakIndexInMountainArray(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return i - 1


A = Solution()
print(A.peakIndexInMountainArray([0, 1, 0]))