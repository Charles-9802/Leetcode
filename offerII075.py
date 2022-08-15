class Solution:
    def relativeSortArray(self, arr1, arr2):
        dic = {}
        result = []
        for num in arr1:
            dic[num] = dic.get(num, 0) + 1
        for i in range(len(arr2)):
            if arr2[i] in dic.keys():
                for _ in range(dic[arr2[i]]):
                    result.append(arr2[i])
        arr1.sort()
        for ch in arr1:
            if ch not in arr2:
                result.append(ch)
        return result

A = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(A.relativeSortArray(arr1, arr2))