import time as t


# 版本1 常规调用流程。
class MyTimer1:

    def start(self):
        self.start = t.localtime()  # 记录开始时间
        print("计时开始...")

    def stop(self):
        self.stop = t.localtime()  # 记录结束时间
        self.result = ""
        for each in range(6):
            self.result += str(self.stop[each] - self.start[each])

        print("计时结束 ," + self.result)


# 版本2 调整：执行 >>> t2 时输出时长。
class MyTimer2:
    """
    # 执行效果
    
    >>> t2 = MyTimer2()
    >>> t2.start()
    计时开始...
    >>> t2.stop()
    计时结束
    >>> print(t2)
    这是测试Str输出
    >>> t2
    总共执行了：000007
    >>> t2.stop
    time.struct_time(tm_year=2018, tm_mon=1, tm_mday=30, tm_hour=9, tm_min=20, tm_sec=19, tm_wday=1, tm_yday=30, tm_isdst=0)
    >>> t2.stop()
    Traceback (most recent call last):
      File "<pyshell#12>", line 1, in <module>
        t2.stop()
    TypeError: 'time.struct_time' object is not callable

    """

    def start(self):
        self.start = t.localtime()  # 记录开始时间
        print("计时开始...")

    def stop(self):
        self.stop = t.localtime()  # 记录结束时间
        self._calculate()
        print("计时结束")

    def _calculate(self):
        '计算计时时长'
        self.result = "总共执行了："
        for each in range(6):
            self.result += str(self.stop[each] - self.start[each])

    def __repr__(self):
        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> t2 
        return self.result  # 输出计时时长

    def __str__(self):
        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> print(t2) 
        return "这是测试Str输出"


#    __repr__ = __str__ # 类似于方法重定向。在执行到 __repr__ 方法时，执行的是 __str__ 方法


# 版本3，
# 调整：初始化之后，直接输出 t3 提示未开始计时。并且设置 执行 t2 或者 print(t2) 都执行输出时长
class MyTimer3:
    """
    # 在 IDEL中的执行效果
        >>> t3 = MyTimer3()
        >>> t3
        未开始计时
        >>> t3.start()
        计时开始...
        >>> t3.stop()
        计时结束
        >>> t3
        总共执行了：000005
        >>> print(t3)
        总共执行了：000005
    """

    def __init__(self):
        self.result = "未开始计时"
        self.begin = 0
        self.end = 0

    def start(self):
        self.begin = t.localtime()  # 记录开始时间
        print("计时开始...")

    def stop(self):
        self.end = t.localtime()  # 记录结束时间
        self._calculate()
        print("计时结束")

    def _calculate(self):
        '计算计时时长'
        self.result = "总共执行了："
        for each in range(6):
            self.result += str(self.end[each] - self.begin[each])

    #    def __repr__(self):
    #        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> t2
    #        return self.result # 输出计时时长

    def __str__(self):
        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> print(t2) 
        return self.result  # 输出计时时长

    __repr__ = __str__  # 这是里为了设置 不管执行 t2 还是  print(t2) 都执行的是 str 方法


# 版本4，
#    添加时间单位
class MyTimer4:
    """
    >>> t4 = MyTimer4()
    >>> t4
    未开始计时
    >>> t4.start()
    计时开始...
    >>> t4.stop()
    >>> t4.stop()
    count 0
    count 0
    count 0
    count 0
    count 0
    count 6
    计时结束
    >>> t4
    总共执行了：6秒

    """

    def __init__(self):
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        self.result = "未开始计时"
        self.begin = 0
        self.end = 0

    def start(self):
        self.begin = t.localtime()  # 记录开始时间
        print("计时开始...")

    def stop(self):
        self.end = t.localtime()  # 记录结束时间
        self._calculate()
        print("计时结束")

    def _calculate(self):
        '计算计时时长'
        self.result = "总共执行了："
        for each in range(6):
            self.count = self.end[each] - self.begin[each]
            if self.count > 0:  # 如果是0 就不显示。
                self.result += str(self.count)
                self.result += self.unit[each]
            print("count " + str(self.count))

    #    def __repr__(self):
    #        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> t2
    #        return self.result # 输出计时时长

    def __str__(self):
        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> print(t2) 
        return self.result  # 输出计时时长

    __repr__ = __str__  # 这是里为了设置 不管执行 t2 还是  print(t2) 都执行的是 str 方法


# 版本5，
#    调整，未开始计时，直接调用stop 提示调用 start() 方法，
#  调用 start 方法后，未调用 stop 直接输出 timer 提示。
class MyTimer5:
    """
    >>> t5 = MyTimer5()
    >>> t5.stop()
    提示：请先调用 start() 方法开始计时
    >>> t5.start()
    计时开始...
    >>> t5.start()
    正在计时中...
    >>> t5
    提示：请先调用 stop() 方法停止计时
    >>> t5.stop()
    count 0
    count 0
    count 0
    count 0
    count 2
    count -35
    计时结束
    >>> t5
    总共执行了：2分钟-35秒
    """

    def __init__(self):
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        self.lasted = []
        self.result = "未开始计时"
        self.begin = 0
        self.end = 0

    def start(self):
        if not self.begin:
            self.begin = t.localtime()  # 记录开始时间
            self.result = "提示：请先调用 stop() 方法停止计时"
            print("计时开始...")
        else:
            print("正在计时中...")

    def stop(self):
        if not self.begin:
            print("提示：请先调用 start() 方法开始计时")
        else:
            self.end = t.localtime()  # 记录结束时间
            self._calculate()
            print("计时结束")

    def _calculate(self):
        '计算计时时长'
        self.result = "总共执行了："
        for each in range(6):
            self.lasted.append(self.end[each] - self.begin[each])
            if self.lasted[each]:  # 如果是0 就不显示。0 表示 false ,true 表示1
                self.result += (str(self.lasted[each]) + self.unit[each])
        #            print("count "+str(self.count))
        self.begin = 0  # 初始化计时数据
        self.end = 0

    #    def __repr__(self):
    #        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> t2
    #        return self.result # 输出计时时长

    def __str__(self):
        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> print(t2) 
        return self.result  # 输出计时时长

    __repr__ = __str__  # 这是里为了设置 不管执行 t2 还是  print(t2) 都执行的是 str 方法


# 版本6，
#  重写 __add__ 方法，输出两个 timer 相加的总数
class MyTimer6:
    """
    # t1

    >>> t1 = MyTimer6()
    >>> t1.stop()
    提示：请先调用 start() 方法开始计时
    >>> t1.start()
    计时开始...
    >>> t1.start()
    正在计时中...
    >>> t1.stop()
    计时结束
    >>> t1
    总共执行了：4秒

    # t2

    >>> t2 = MyTimer6()
    >>> t2.start()
    计时开始...
    >>> t2.stop()
    计时结束
    >>> t2
    总共执行了：6秒

    # t1+t2

    >>> t1+t2
    '总共运行了：10秒'
    >>> print(t1+t2)
    总共运行了：10秒

    """

    def __init__(self):
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        self.lasted = []
        self.result = "未开始计时"
        self.begin = 0
        self.end = 0

    def __add__(self, other):
        totalCount = "总共运行了："
        result = []
        for each in range(6):
            result.append(self.lasted[each] + other.lasted[each])
            if result[each]:
                totalCount += (str(result[each]) + self.unit[each])
        return totalCount

    def start(self):
        if not self.begin:
            self.begin = t.localtime()  # 记录开始时间
            self.result = "提示：请先调用 stop() 方法停止计时"
            print("计时开始...")
        else:
            print("正在计时中...")

    def stop(self):
        if not self.begin:
            print("提示：请先调用 start() 方法开始计时")
        else:
            self.end = t.localtime()  # 记录结束时间
            self._calculate()
            print("计时结束")

    def _calculate(self):
        '计算计时时长'
        self.result = "总共执行了："
        for each in range(6):
            self.lasted.append(self.end[each] - self.begin[each])
            if self.lasted[each]:  # 如果是0 就不显示。0 表示 false ,true 表示1
                self.result += (str(self.lasted[each]) + self.unit[each])
        #            print("count "+str(self.count))
        self.begin = 0  # 初始化计时数据
        self.end = 0

    #    def __repr__(self):
    #        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> t2
    #        return self.result # 输出计时时长

    def __str__(self):
        # 在 IDLE 的 Shell 中，此方法执行的情况是以下方式 >>> print(t2) 
        return self.result  # 输出计时时长

    __repr__ = __str__  # 这是里为了设置 不管执行 t2 还是  print(t2) 都执行的是 str 方法
