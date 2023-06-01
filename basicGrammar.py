import hello


# 定义一个类
from utils.tool import load_text


class Student:
    # 定义构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = None  # python里None表示空，相当于java里的null

    # 定义一个方法
    def printInfo(self):
        # 格式化输出
        print("name:%s,age:%d" % (self.name, self.age))


class Solution():
    def twoSum(self, nums, target):
        hashdict = {}
        for i, item in enumerate(nums):
            if (target - item) in hashdict:
                return (hashdict[target - item], i)
            hashdict[item] = i
        return (-1, -1)


def forArray(nums):
    # 遍历数组,index是下标，item是值
    for index, item in enumerate(nums):
        print("index:%d,value:%d" % (index, item))


# 列表，字符串，元组都支持slice操作
# 测试数据 [1 , 3 , 5 , 7 , 9]
# 正索引	0 , 1 , 2 , 3 , 4 [1,3,5,7,9]
# 负索引	-5,-4,-3,-2,-1 [9,7,5,3,1]

# 测试slice操作
def forSlice(a):
    print(a[1])  # 结果3
    print(a[-3])  # 结果5
    print(a[:])  # 从左往右 结果[1, 3, 5, 7, 9]
    print(a[::])  # 从左往右 结果[1, 3, 5, 7, 9]
    print(a[:: -1])  # 从右往左 结果[9, 7, 5, 3, 1]
    print(a[1:5:-1])  # step=-1，决定了从右往左取值，而start_index=1到end_index=5决定了从左往右取值，互相矛盾 结果[ ]
    print(a[:-3:-1])  # step=-1，从右往左取值，从“终点”开始一直取到end_index=5 结果[9, 7]

def tryExcept():
    try:
        print(1 / 0)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally")

def readFile():
    name = "json.txt"
    path = f'{name}'
    print(load_text(path)) # 调用utils包里的tool.py里的load_text方法

# 如果是主程序（自已程序是入口，而非其它包调用这个文件），就执行下面的代码
if __name__ == '__main__':
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
    forArray([1, 3, 5, 7, 9])
    forSlice([1, 3, 5, 7, 9])
    tryExcept();
    readFile();
