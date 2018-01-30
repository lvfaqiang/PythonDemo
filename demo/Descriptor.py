class MyDescriptor:
    def __get__(self, instance, owner):
        # self 当前描述符 本身，
        # instance 当前所在的对象的引用
        # owner 当前所在的对象 #
        print("get", self, instance, owner)

    def __set__(self, instance, value):
        # self 当前描述符 本身，
        # instance 当前所在的对象的引用
        # value 设置的值 #
        print("set", self, instance, value)

    def __delete__(self, instance):
        print("delete", self, instance)


class A:
    x = MyDescriptor()


a = A()
print(a.x)  # 调用 a.x 时，执行了 MyDescriptor 的 get 方法
a.x = 100  # 执行 MyDescriptor 的 set 方法
del a.x  # 执行 MyDescriptor 的 delete 方法

print("-------------------")


class MyProperty:
    """
    自定义一个 property 方法
    """

    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class B:
    def __init__(self):
        self._x = None

    def getX(self):
        print("getX")
        return self._x

    def setX(self, value):
        print("setX", value)
        self._x = value

    def delX(self):
        print("dexX")
        del self._x

    x = MyProperty(getX, setX, delX)


b = B()
b.x = "设置内容"
print("b.x", b.x, "b._x", b._x)
