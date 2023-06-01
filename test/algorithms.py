# 斐波那契数列


class Simple():
    def fibonacci(num):
        if num <= 1:
            return num
        else:
            return Simple.fibonacci(num - 1) + Simple.fibonacci(num - 2)
    def twoSum(self, nums, target):
        hashdict = {}
        for i, item in enumerate(nums):
            if (target - item) in hashdict:
                return (hashdict[target - item], i)
            hashdict[item] = i
        return (-1, -1)
# 菲波那切数列
print("fibonacci=%d"  %(Simple.fibonacci(6)))

# 两数之合
print(Simple.twoSum([2, 7, 11, 15], 9))