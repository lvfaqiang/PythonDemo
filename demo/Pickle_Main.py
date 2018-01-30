import pickle  # 永久存储列表，集合等对象数据（以二进制形式）


def saveList(list, fileName):
    pikle_file = open(fileName, "wb")  # 参数一是保存的文件名称，参数二，必须有 'b' 二进制  wb：以二进制形式写入
    # 进行存储
    pickle.dump(list, pikle_file)
    pikle_file.close()  # 关闭文件


def getList(fileName):
    file = open(fileName, "rb")
    list = pickle.load(file)
    return list


myList = [123, 3.14, "发强", ["another list"]]
fileName = "../myList.pkl" # 文件名后缀可以随意，无限制。

saveList(myList, fileName)  # 调用保存

list1 = getList(fileName)  # 获取列表

print(list1)
