def puke(nums):
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        return nums
    result = [nums[-1]]
    for i in range(len(nums) - 2, -1, -1):
        result = [nums[i]] + result
        result = result[len(result)-1:len(result)] + result[0:len(result)-1]
        result = result[len(result) - 1:len(result)] + result[0:len(result) - 1]
    return result
print(puke([3,1,5,2,4]))


