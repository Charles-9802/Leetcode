# 接雨水
# 双指针超时 列方向
# class Solution:
#     def trap(self, height) -> int:
#         res = 0
#         for i in range(len(height)):
#             if i == 0 or i == len(height) - 1:
#                 continue
#             Lhight = height[i-1]
#             Rhight = height[i+1]
#             for j in range(i-1):
#                 if height[j] > Lhight:
#                     Lhight = height[j]
#             for k in range(i+2, len(height)):
#                 if height[k] > Rhight:
#                     Rhight = height[k]
#             res1 = min(Lhight, Rhight) - height[i]
#             if res1 > 0:
#                 res += res1
#         return res


# # 接雨水
# 动态规划 列方向
# class Solution:
#     def trap(self, height) -> int:
#         leftheight = [0] * len(height)
#         rightheight = [0] * len(height)
#
#         leftheight[0] = height[0]
#         for i in range(1, len(height)):
#             leftheight[i] = max(leftheight[i - 1], height[i])
#         rightheight[-1] = height[-1]
#         for i in range(len(height) - 2, -1, -1):
#             rightheight[i] = max(rightheight[i + 1], height[i])
#
#         result = 0
#         for i in range(0, len(height)):
#             _sum = min(leftheight[i], rightheight[i]) - height[i]
#             result += _sum
#         return result


# 接雨水
# 单调栈 行方向 栈头（元素从栈头弹出）到栈底的顺序应该是从小到大的顺序
class Solution:
    def trap(self, height) -> int:
        # stack储存index，用于计算对应的柱子高度
        stack = [0]
        result = 0
        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)

            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)

            else:
                # 抛出所有较低的柱子
                while stack and height[i] > height[stack[-1]]:
                    # 栈顶就是中间的柱子：储水槽，就是凹槽的地步
                    mid_height = height[stack[-1]]
                    stack.pop()
                    if stack:   # 保证还有左边的柱子
                        right_height = height[i]
                        left_height = height[stack[-1]]
                        h = min(right_height, left_height) - mid_height
                        w = i - stack[-1] - 1
                        result += h * w
                stack.append(i)
        return result


def main():
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [3, 2, 1, 3, 4]
    A = Solution()
    print(A.trap(height))


if __name__ == "__main__":
    main()
