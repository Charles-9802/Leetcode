import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        from sortedcontainers import SortedList
        st = SortedList()
        for i, num in enumerate(nums):
            st.add(num)
            index = bisect.bisect_left(st, num)
            if index < len(st) - 1 and st[index + 1] - st[index] <= t:
                return True
            if index > 0 and st[index] - st[index - 1] <= t:
                return True
            if len(st) > k:
                st.remove(nums[i - k])
        return False


def main():
    A = Solution()
    # print(A.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
    print(A.containsNearbyAlmostDuplicate([1, 2, 3, 1], k=3, t=0))


if __name__ == "__main__":
    main()
