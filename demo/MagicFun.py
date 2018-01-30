# __new__ 类中的方法，执行与 __init__() 之前

class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


string = CapStr("I am not a good man\"")


# print(string)

# -----------------------

# __del__ 方法， 当某对象没有被引用时，被垃圾回收机制清理时，执行 此方法

class A:
    def __init__(self):
        print(" 我是 A 的 init 方法")

    def __del__(self):
        print(" 我是 A 的 del 方法")

    def print(self):
        print("------End------")


A()  # 这里调用会执行 init 和 del 方法。因为 A() 并没有被引用

a = A()
print("-----")
a.print()  # 当这里执行完之后，a 会被释放，然后，A() 的 __del__ 方法被执行


# --------------------


# __radd()_____  反运算
class Nint(int):
    """
     方法前加 'r' 表示 反运算 。
     例如，加法 正常的是前面 加 后面的，反运算，就是后面的去加前面的。如果重写了实现，就另说了。

    """

    def __radd__(self, other):
        print("这是 int radd 方法， self :" + str(self))
        return int.__sub__(self, other)  # 重写了 radd 的实现。

    def __add__(self, other):
        print("这是 int add 方法， self :" + str(self))
        return int.__add__(self, other)

    def __str__(self):
        "在当前对象被输出的时候，会执行此方法。"
        print(" ------str 方法-")
        return ""


a = Nint(5)
b = Nint(3)
# 如果 a 对象中 有 add 方法，则执行 a 的 add 方法，反之，则调用 b 对象中的 反运算加法 也就是 __radd()__ 方法
# 所以，这里是执行 a 中的 int 的 add 方法。
print(a + b)

print(1 + b)  # 这里，因为 1 不是一个对象，里面并没有 add 方法，所以，是执行了 b 的 radd 方法，

print("--------------- 我是分割线-----------")


# __iadd()__  增量赋值运算
# 定义赋值加法的运算 等同于 +=


# __str()__ 方法是当对象被输出的时候，调用
# __repr()__ 用法如下：
class A():

    # def __repr__(self):
    #     print("这里是 repr 方法")
    #     return "执行了 repr 方法"
    #

    def __str__(self):
        print("this is str 方法")
        return "这是 str 方法"

    __repr__ = __str__


a = A()
print(repr(a))  # 执行这里的时候，repr 方法会被调用
