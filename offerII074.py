class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if (intervals[i][0] >= result[-1][0]) and (intervals[i][1] <= result[-1][1]):
                continue
            if intervals[i][0] <= result[-1][1]:
                tmp = result.pop()
                result.append([tmp[0], intervals[i][1]])
            else:
                result.append(intervals[i])
        return result


A = Solution()
print(A.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(A.merge([[1, 4], [4, 5]]))
print(A.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
print(A.merge([[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]))

