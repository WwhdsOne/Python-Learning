import random
import time

# 生成一个长度为1000000，值在0-10亿以内的数组
arr = [random.randint(0, 10**9) for _ in range(1000000)]
n = len(arr)

def quick_sort(nums, l, r):
    if l >= r:
        return
    split = nums[random.randint(l,r)]
    i, j = l - 1, r + 1
    while i < j:
        while True:
            i += 1
            if nums[i] >= split:
                break
        while True:
            j -= 1
            if nums[j] <= split:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    quick_sort(arr, l, j)
    quick_sort(arr, j+1, r)


# 记录排序开始的时间
start_time = time.time()
# 对数组进行排序
quick_sort(arr, 0, len(arr) - 1)
# 记录排序结束的时间
end_time = time.time()

# 打印排序后的数组
print("排序后的数组:", arr)
# 打印排序所用的时间
print("所用时间:", end_time - start_time, "秒")