import random
import time

# 划分函数，用于将数组划分为两部分，一部分的元素都小于等于枢轴元素，另一部分的元素都大于枢轴元素
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# 快速排序函数
def quicksort(arr, low, high):
    if low < high:
        pivot_index = random_partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

# 随机划分函数，用于随机选择一个元素作为枢轴元素
def random_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)

import random

# 生成一个长度为1000000，值在0-10亿以内的数组
arr = [random.randint(0, 10**9) for _ in range(1000000)]
n = len(arr)

# 记录排序开始的时间
start_time = time.time()
# 对数组进行排序
quicksort(arr, 0, n - 1)
# 记录排序结束的时间
end_time = time.time()

# 打印排序后的数组
print("排序后的数组:", arr)
# 打印排序所用的时间
print("所用时间:", end_time - start_time, "秒")