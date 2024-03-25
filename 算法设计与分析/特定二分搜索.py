# 定义二分搜索函数
def binary_search(nums, target):
    # 初始化左右指针
    left = 0
    right = len(nums) - 1

    # 当左指针小于等于右指针时，执行循环
    while left <= right:
        # 计算中间位置
        mid = (left + right) // 2

        # 如果中间位置的值等于目标值，返回中间位置
        if nums[mid] == target:
            return mid
        # 如果中间位置的值小于目标值，将左指针移动到中间位置的右边
        elif nums[mid] < target:
            left = mid + 1
        # 如果中间位置的值大于目标值，将右指针移动到中间位置的左边
        else:
            right = mid - 1

    # 如果没有找到目标值，返回-1
    return -1

# 测试代码
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
# 调用二分搜索函数，打印结果
result = binary_search(nums, target)
print(f"目标值 {target} 在列表中的索引为 {result}。")

target = 11
# 调用二分搜索函数，打印结果
result = binary_search(nums, target)
if result == -1:
    print(f"目标值 {target} 不在列表中。")
else:
    print(f"目标值 {target} 在列表中的索引为 {result}。")