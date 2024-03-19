def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# 测试代码
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(nums, target)
print(f"目标值 {target} 在列表中的索引为 {result}。")

target = 11
result = binary_search(nums, target)
if result == -1:
    print(f"目标值 {target} 不在列表中。")
else:
    print(f"目标值 {target} 在列表中的索引为 {result}。")