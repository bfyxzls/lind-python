from optparse import OptionParser

import hello

# 定义一个类
from utils.tool import load_text


class Student:
    # 定义构造函数
    def __init__(self, name, age):
        # self表示的是Student类的实例本身
        self.name = name
        self.age = age
        self.address = None  # python里None表示空，相当于java里的null

    # 定义一个方法
    def printInfo(self):
        # 格式化输出
        print("name:%s,age:%d" % (self.name, self.age))


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
    name = "../resources/json.txt"
    path = f'{name}'
    print(load_text(path))  # 调用utils包里的tool.py里的load_text方法

def t1(param1, *param2):
    print(param1)
    print(param2)

def t2(param1, **param2):
    print(param1)
    print(param2)

class people:
    name=''
    age=0
    __weight=0 # 私有属性
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        # 调用父类的构函
        people.__init__(self,n,a,w)
        self.grade=g
    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" %(self.name,self.age,self.grade))

# 如果是主程序（自已程序是入口，而非其它包调用这个文件），就执行下面的代码
if __name__ == '__main__':
    hello.printName("zzl")

    # 字典的增删改查
    data = {}
    data['name'] = 'zzl'
    data['age'] = 18
    data['gender'] = 'male'
    print(data)
    data.update({'name': 'zzl2', 'data': "新加的字段"})
    print(data)

    # 定义一个列表，并添加元素，并通过for循环遍历
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

    # 实例伦一个类型，并调用它的方法
    stu = Student('zzl', 18)
    stu.printInfo();

    # 数组遍历
    arr=[1, 3, 5, 7, 9];
    forArray(arr)
    arr.extend([11,13,15,17,19])
    forArray(arr)

    # 测试slice操作
    forSlice([1, 3, 5, 7, 9])

    # try except测试
    tryExcept();

    # 读json文件
    readFile();

    # 三元运算符，如果a>b，就返回1，否则返回2
    a = 3
    b = 4
    result = 1 if a > b else 2
    print(result)

    # 输入参数测试,python .\basicGrammar.py --mode=prod
    parser = OptionParser()
    parser.add_option("--mode", dest="mode", help="interaction mode: training, test")
    (options, args) = parser.parse_args()
    # assert options.mode is not None, "missing mode"
    if options.mode == 'svt':
        print("测试环境")
    elif options.mode == 'prod':
        print("生产环境")
    else:
        print("未知环境")

    # 测试*和**的用法
    t1(1, 2, 3, 4)
    t2(1, a=2, b=3)

    studnet= student('zzl', 18, 100, 3)
    studnet.speak()