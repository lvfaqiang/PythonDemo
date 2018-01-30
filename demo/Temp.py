# 使用场景
# 一个温度类，有摄氏度，华氏度，两个属性，修改任意一个属性值，另外的会跟随变化
# #

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


class Temp:
    def __init__(self):
        self.she = None  # 摄氏度
        self.hua = None  # 华氏度

    def getShe(self):
        if hasattr(self, "she"):
            return self.she
        else:
            return None

    def setShe(self, sValue):
        if hasattr(self, "she"):
            self.she = sValue
            self.hua = int(sValue) * 10 + 32
        else:
            print("该属性不存在")

    def delShe(self):
        del self.she

    def getHua(self):
        if hasattr(self, "hua"):
            return self.hua
        else:
            return None

    def setHua(self, hValue):
        if hasattr(self, "hua"):
            self.hua = hValue
            if hasattr(self, "she"):
                self.she = str((int(hValue) - 32) / 10)
        else:
            print("属性'hua'不存在")

    def delHua(self):
        del self.hua

    def __str__(self):
        return str("摄氏度：" + str(self.she) + " , 华氏度：" + str(self.hua))

    __repr__ = __str__

    s = MyProperty(getShe, setShe, delShe)
    h = MyProperty(getHua, setHua, delHua)
