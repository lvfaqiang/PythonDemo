# 丰富的 else 语句。

# 方案一
def showRange(num):
    if 0 < num < 10:
        print("%d 在 0..10 区间" % num)
    elif 10 < num < 100:
        print("%d 在 10..100 区间" % num)
    else:
        print("%d 在 100以外的区间" % num)


# while 配合 else
def showMaxFactor(num):
    "求最大约数"
    count = num // 2  # 求模
    while count > 1:
        if num % count == 0:  # 当 count >1 的所有条件中，没有进入到这里，最后会进入 else 语句
            print("%d最大约数是%d" % (num, count))
            break
        count -= 1
    else:
        print("%d是素数！" % num)


# try except 配合 else
def tryElse(num):
    try:
        print(int(num))  # 如果这里正常 则输出，并且进入 else 语句，有异常，则会进入异常信息中
    except Exception as rea:
        print("has a Exception. Cause By ：" + str(rea))
    else:
        print("完美~")


# num = int(input("请输入一个数字："))
# showRange(num)
# showMaxFactor(num)

num = input("请输入内容：")
tryElse(num)
