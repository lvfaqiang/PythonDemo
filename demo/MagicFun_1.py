class A:
    def __getattr__(self, item):
        "当用户试图获取一个不存在的属性时的行为。"
        print("getattr , " + str(item))

    def __getattribute__(self, item):
        "获取属性名称为 item 的属性值 。如果未获取到该属性，则会进入 __getattr__ 方法"
        print("__getattribute__ , " + str(item))
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        "当一个属性被设置值时的行为"
        print("__setattr__ , " + str(key) + ", " + str(value))
        super().__setattr__(key, value)

    def __delattr__(self, item):
        "当一个属性被删除时的行为"
        print("__delattr__ , " + str(item))
        super().__delattr__(item)


a = A()
print("result: ", a.x) # 执行结果依次是：1，（ __getattribute__ , x ）  2，（getattr , x ） 3，（result:  None）
print("-----------------")
a.x = 10    # 执行结果 __setattr__ , x, 10

print("result 1 : ", a.x)   # 执行结果：  1 ,(__getattribute__ , x) 2，（result 1 :  10）
print("-----------------")
del a.x # 执行： __delattr__ , x
