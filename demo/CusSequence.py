# 定制序列

class CusList:
    '定义一个不可变的列表'

    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)  # 定义一个字典，用于存放每个item 的访问次数

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]


# next(str("1"))


class MultiList:
    '定义一个可变的列表'

    def append(self, item):
        print("append")
        self.values.append(item)

    def __init__(self, *args):
        print("__init__")
        self.values = [x for x in args]
        self.count = {}.fromkeys(self.values, 0)

    def __len__(self):
        print("__len__")
        return len(self.values)

    def __getitem__(self, item):
        print("__getitem__")
        self.count[self.values[item]] += 1
        return self.values[item]

    def __setitem__(self, key, value):
        print("__setitem__")
        self.values.append(value)
        self.count.get(value, 0)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.values)

    def __delitem__(self, item):
        print("__delitem__")
        del self.values[item]
        del self.count[item]
