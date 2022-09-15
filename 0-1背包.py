# 二维
# def beibao_2D(size, weight, value):
#     dp = [[0 for _ in range(size + 1)] for _ in range(len(weight))]
#     for i in range(weight[0], size + 1):
#         dp[0][i] = value[0]
#     for i in range(1, len(weight)):
#         for j in range(1, size + 1):
#             if weight[i] > j:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
#     return dp
# weight = [1, 3, 4]
# value = [15, 20, 30]
# size = 4
# print(beibao_2D(size, weight, value))

# # 一维
# def beibao_1D(size, weight, value):
#     dp = [0 for _ in range(size + 1)]
#     for i in range(len(weight)):
#         for j in range(size, weight[i] - 1, -1):
#             dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
#     return dp
# weight = [1, 3, 4]
# value = [15, 20, 30]
# size = 4
# print(beibao_1D(size, weight, value))

# 1D的时候只能先遍历物品再遍历背包，而且遍历背包要逆序。