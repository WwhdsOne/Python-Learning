# 自然合并排序：自然合并排序是一种基于现有顺序的排序算法。它首先扫描整个数组，找出已经有序的部分（称为“自然的运行”），然后合并这些运行。
# 如果在扫描过程中发现整个数组已经有序，那么就可以立即停止排序。自然合并排序的分割是根据数据的实际情况来的，可能不均匀。

import time

def natural_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def get_runs(arr):
        runs, start = [], 0
        for end in range(1, len(arr)):
            if arr[end] < arr[end-1]:
                runs.append(arr[start:end])
                start = end
        runs.append(arr[start:])
        return runs

    runs = get_runs(arr)
    while len(runs) > 1:
        runs.append(merge(runs.pop(0), runs.pop(0)))
    return runs[0]

import random

# 生成一个长度为100000，值在0-10亿以内的数组
arr = [random.randint(0, 10**9) for _ in range(100000)]
start_time = time.time()
sorted_arr = natural_merge_sort(arr)
end_time = time.time()
execution_time = end_time - start_time
print("排序后的数组：", sorted_arr)
print("执行时间：", execution_time, "秒")