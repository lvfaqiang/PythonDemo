# 我们每次打开文件，输入输出流之类的，都需要在最后的 finally 中进行调用 close 方法，以释放相关资源。
# 在 python 中，我们可以使用 with 来简化每次的 finally 操作。

# 方式一： 常规的 fianlly 写法
def method1():
    try:
        f = open("data.txt", "w")
        for each in f:
            print(each)
    except Exception as rea:
        print("Exception : " + str(rea))
    finally:
        f.close()


# 方式二： 利用 with 关键字的写法
def method2():
    try:
        with open("data.txt", "w") as f:    # 这里使用 with 关键字，系统检测到当 f 什么时候不用了，就自动释放掉
            for each in f:
                print(each)
    except Exception as rea:
        print("Exception : " + str(rea))
