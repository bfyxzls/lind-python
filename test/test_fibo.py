def fib(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo [n]


# noinspection PyPackageRequirements
def fib2(n):
    if n <= 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

#print(fib2(40))

# 爬楼，加记忆性缓存
def climbStairs(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return n

    memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
    return memo[n]
#print(climbStairs(5))


# 打劫，不能偷相邻的房屋，否则会触发报警
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2=nums[0]
    prev1 = max(nums[0], nums[1])
    for i in range(2,len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = curr
    return prev1

print(rob([1,2,3,4]))