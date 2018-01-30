## 方式一
def method1():
    try:
        f = open("这是一个假的文件.txt")
        print(f.read())
        f.close()
    except FileNotFoundError as reason:
        print("文件出错了 T_T , 错误原因： " + str(reason))


## 方式二
def method2():
    try:
        int("abc")  # 这里出现异常之后，以下代码不会继续执行，所以 "分割线" 不会输出。
        print("分割线")
        f = open("这是一个假的文件.txt")
        print(f.read())
        f.close()
    except (FileNotFoundError, ValueError):
        print("文件出错了，")


## 方式三
def method3():
    try:
        f = open("exceptionile.txt", "w")
        print(f.write("我是内容~"))
        int("abc")
    except Exception as rea:
        print("文件出错 T_T， Cause By:" + str(rea))
    finally:
        print("最终执行")
        f.close()


## 方式四 自定义异常

def method4():
    value = int(input("请输入一个大于 10 的数字："))
    if value < 10:
        raise ValueError("value must be > 10")


method4()
