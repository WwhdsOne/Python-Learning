# 导入时间模块
import time

# 定义自然合并排序函数
def natural_merge_sort(arr):
    # 如果数组长度小于等于1，直接返回
    if len(arr) <= 1:
        return arr

    # 定义合并函数，用于合并两个有序数组
    def merge(left, right):
        merged, i, j = [], 0, 0
        # 当两个数组都有元素时，比较并取出较小的元素
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # 将剩余的元素添加到结果数组中
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    # 定义获取运行函数，用于获取数组中的有序部分
    def get_runs(arr):
        runs, start = [], 0
        # 遍历数组，找出有序部分
        for end in range(1, len(arr)):
            if arr[end] < arr[end-1]:
                runs.append(arr[start:end])
                start = end
        # 添加最后一个有序部分
        runs.append(arr[start:])
        return runs

    # 获取数组的有序部分
    runs = get_runs(arr)
    # 当有序部分数量大于1时，进行合并
    while len(runs) > 1:
        runs.append(merge(runs.pop(0), runs.pop(0)))
    # 返回排序后的数组
    return runs[0]

# 导入随机模块
import random

# 生成一个长度为100000，值在0-10亿以内的数组
arr = [random.randint(0, 10**9) for _ in range(100000)]
# 记录排序开始时间
start_time = time.time()
# 对数组进行自然合并排序
sorted_arr = natural_merge_sort(arr)
# 记录排序结束时间
end_time = time.time()
# 计算排序执行时间
execution_time = end_time - start_time
# 打印排序后的数组和执行时间
print("排序后的数组：", sorted_arr)
print("执行时间：", execution_time, "秒")