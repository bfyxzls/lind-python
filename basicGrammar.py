import hello


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print("name:%s,age:%d" % (self.name, self.age))

class Solution():
    def twoSum(self, nums, target):
        hashdict = {}
        for i, item in enumerate(nums):
            if (target - item) in hashdict:
                return (hashdict[target - item], i)
            hashdict[item] = i
        return (-1, -1)

if __name__ == '__main__':  # 如果是主程序，就执行下面的代码
    hello.printName("zzl")
    data = {}
    data['name'] = 'zzl'
    data['age'] = 18
    data['gender'] = 'male'
    print(data)
    addr = []
    addr.append('beijing')
    addr.append('shanghai')
    addr.append('guangzhou')
    print(addr)
    subject = []
    subject.append(['math', 'english', 'chinese'])
    subject.append(['math', 'wuli', 'huaxue'])
    print(subject)
    for line in subject:
        print("行显示：%s" % line)
    stu = Student('zzl', 18)
    stu.printInfo();
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))