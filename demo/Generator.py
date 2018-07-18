# 生成器
# 生成器的关键字为 yield

# 下面是一个简单的生成器例子#

def myGenerator():
    print("生成器被执行！")
    yield 1  #
    yield 2


myG = myGenerator()
print(next(myG))  # 输出 1
print(next(myG))  # 输出 2


#     ---------------------------
def Fun1():
    a = 0
    b = 1
    while True:
        # 斐波那契数列
        a, b = b, a + b
        yield a


for i in Fun1():
    if i > 100:
        break
    print(i, end=" ")

a = [i for i in range(100) if not (i % 2) and i % 3]
print(a) # 输出 100 以内的 所有是 2 的倍数，却不是 3 的倍数的值。
