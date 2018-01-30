# 写法一：
class Rectangle:
    "正方形"

    def __init__(self, width, height):
        # ①
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == "square":
            self.width = value
            self.height = value
        else:
            # ②
            print("setattr: ", key, value)
            self.key = value

    def _getArea(self):
        "获取面积"
        return self.width * self.height


##
# 此处代码造成的结果是 死循环。
# Cause By，init 方法执行给属性设置值（代码片段①），进入 setattr 方法，
# 然后执行到 ② 位置再次进行 设置值，又再次回到了 setattr 方法，这样就形成了一个无限递归。直到当前系统分配的递归层次执行完成。
#         ##
# print("-------方式1------")
# a = Rectangle(4, 5)


# 以上代码调整写法 写法二
class Rectangle1:
    "正方形"

    def __init__(self, width, height):
        # ①
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == "square":
            self.width = value
            self.height = value
        else:
            # ②
            print("setattr: ", key, value)
            # self.key = value
            super().__setattr__(key, value)  # 修改此处代码为调用父类的 setattr 方法

    def getArea(self):
        "获取面积"
        return self.width * self.height


print("-------方式2------")
a = Rectangle1(4, 5)
print(a.getArea())
# 执行结果
# setattr:  width 4
# setattr:  height 5
# 20

print("-------------")

a.square = 10
print(a.getArea())
# 执行结果
# setattr:  width 10
# setattr:  height 10
# 100

print("-------方式3------")
# dict 获取对象中的所有属性参数 #
print(a.__dict__)  # 输出 {'width': 10, 'height': 10}


# 改法三
class Rectangle2:
    "正方形"

    def __init__(self, width, height):
        # ①
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == "square":
            self.width = value
            self.height = value
        else:
            # ②
            print("setattr: ", key, value)
            # self.key = value
            self.__dict__[key] = value

    def getArea(self):
        "获取面积"
        return self.width * self.height


a = Rectangle2(4, 5)
print(a.getArea())
