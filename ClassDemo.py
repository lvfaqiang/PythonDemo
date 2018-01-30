## Demo 1

class Boll:

    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


# b = Boll()
# b.setName("发强")
# print(b.getName())

# c = Boll("发强")
# print(c.getName())


class Person:
    __name = "发强"  # 伪私有参数，

    def getName(self):
        return self.__name

    def __print(self):
        print("我是一个私有方法")


p = Person()
print(p.getName())
print(p._Person__name)  # 可通过此种方式获取 私有参数以及方法。
p._Person__print()


##---------------------------------------------------------

class A:
    pass


class B(A):
    pass


class C:
    pass


print(issubclass(B, A))  # B 是否是 A 的子类，
print(issubclass(B, B))
print(issubclass(B, object))  # object 为所有类的基类
print(issubclass(B, C))
print(issubclass(B, (C, B)))  # B 是否属于 元组中的某一个类的子类

print('---------------------')

b = B()
print(isinstance(B(), object))  # 类似于 issubclass


class E:
    def __init__(self, x=0):
        self.x = x


e = E()
print(hasattr(e, "x"))  # hasattr(obj , str)  obj 中是否有 str 属性。
getattr(e, 'y', '没有y')  # 获取属性 y ，没有则返回 默认值。

setattr(e, 'y', "发强")  # 设置属性，不存在则添加。
print(getattr(e, 'y'))
# delattr(E(), "y")


##---------------------------

print("---------------------------")


class C:
    def __init__(self, size=10):
        self.size = size

    def setSize(self, value):
        self.size = value

    def getSize(self):
        return self.size

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize, "用于操作 size")


c = C()
print(c.size)
print(c.x)
c.x = 20
print(c.x)