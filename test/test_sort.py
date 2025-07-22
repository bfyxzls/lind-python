# 快速排序的思想就是分治思想，把一个数组，选择一个基准值叫做pivot，用它来把数组分成两个子数组，左边的都比它小，右边的比它大，然后递归下去。
# 所以他是先分后递归，和归并排序不一样，归并排序应该是直接分分到最后才开始排。
# 他先分的时候用的想法就是要把一个数组分成两半，用了两个序号，比他小的数据况要看情况，如果前面有比他大的数据，就把小的数据和大的数据交换，否则的话，小的就不动，只有后指针加一，如果遇到大的就都不动，最后，把基准值和这个大的值交换就可以了。用到了双指针，前面的指针指向数组的序号，后面的指针指向最后一个比它小的数据，一旦要交换大的，或者要交换基准值
def quick_sort(arr):
    """
    快速排序主函数
    :param arr: 待排序的列表
    :return: 排序后的列表
    """
    # 如果列表长度小于等于1，直接返回（递归终止条件）
    if len(arr) <= 1:
        return arr

    # 选择基准值（pivot） - 这里取中间元素
    pivot = arr[len(arr) // 2]

    # 划分三个列表
    left = [x for x in arr if x < pivot]  # 小于基准值的元素
    middle = [x for x in arr if x == pivot]  # 等于基准值的元素
    right = [x for x in arr if x > pivot]  # 大于基准值的元素

    # 递归排序左右部分，然后合并结果
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_in_place(arr, low=0, high=None):
    """
    原地快速排序（节省内存空间）
    :param arr: 待排序的列表
    :param low: 子列表起始索引
    :param high: 子列表结束索引
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 划分数组并获取分区点
        pivot_index = partition(arr, low, high)

        # 递归排序左半部分
        quick_sort_in_place(arr, low, pivot_index - 1)
        # 递归排序右半部分
        quick_sort_in_place(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    划分函数（原地操作）
    :return: 基准值的最终位置
    """
    # 选择基准值（这里取最右边的元素）
    pivot = arr[high]
    i = low  # 指向小于基准值区域的末尾

    # 遍历当前分区
    for j in range(low, high):
        if arr[j] < pivot:
            # 将小于基准值的元素交换到左侧区域
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # 将基准值放到正确的位置
    arr[i], arr[high] = arr[high], arr[i]
    return i


def test_quick_sort():
    """测试快速排序算法"""
    # 测试用例
    test_cases = [
        [3, 6, 8, 10, 1, 2, 1],  # 普通测试
        [],  # 空列表
        [5],  # 单元素列表
        [9, 7, 5, 3, 1],  # 逆序列表
        [1, 2, 3, 4, 5],  # 已排序列表
        [4, 4, 4, 4, 4],  # 全相同元素
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]  # 包含重复元素
    ]

    for test in test_cases:
        # 测试普通快速排序
        sorted_arr = quick_sort(test.copy())
        # 测试原地快速排序
        arr_copy = test.copy()
        quick_sort_in_place(arr_copy)

        # 验证两个排序结果都正确
        assert sorted_arr == sorted(test), f"普通快速排序失败: {test} -> {sorted_arr}"
        assert arr_copy == sorted(test), f"原地快速排序失败: {test} -> {arr_copy}"

        print(f"原始: {test} \n排序: {sorted_arr} \n原地排序: {arr_copy}\n{'-' * 40}")


if __name__ == "__main__":
    test_quick_sort()
    print("所有测试用例通过！")