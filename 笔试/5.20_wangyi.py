# n = input()
# n = int(n)
# num = list(map(int, input().split()))
# def solu(num):
#     nums1 = []
#     nums2 = []
#     for i in range(len(num)):
#         if i % 2 == 0:
#             nums1.append(num[i])
#         else:
#             nums2.append(num[i])
#     _max1 = max(nums1)
#     _max2 = max(nums2)
#     res = 0
#     if _max2 != _max1:
#         res = res + _max1 * len(nums1) - sum(nums1)
#         res = res + _max2 * len(nums2) - sum(nums2)
#     else:
#         if len(nums1) < len(nums2):
#             res = res + _max1 * len(nums1) - sum(nums1)
#             res = res + _max2 * len(nums2) - sum(nums2)
#             res += len(nums1)
#         else:
#             res = res + _max1 * len(nums1) - sum(nums1)
#             res = res + _max2 * len(nums2) - sum(nums2)
#             res += len(nums2)
#     return res
# print(solu([1,1,4,5,1,4]))

# def solu(num):
#     count = 0
#     for i in range(len(num)):
#         for j in range(i + 2, len(num)):
#             if num[i] == num[j]:
#                 for k in range(i + 1, j):
#                     if num[k] < num[i]:
#                         count += 1
#     return count
#
#
# num = [3,1,3,4,3,4]
# print(solu(num))
