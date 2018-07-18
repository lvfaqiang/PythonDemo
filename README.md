# PythonDemo
#### 2018年02月02日
[生成器](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/Generator.py)<br/>
#### 2018年01月30日
[python 描述符](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/Descriptor.py)<br/>
[描述符示例1](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/Temp.py)<br/>
[描述符示例2（改进版）](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/Temp_1.py)<br/>
```
示例说明：
一个温度类，有两个属性：摄氏度、华氏度。
摄氏度或者华氏度改变时，另一个也要随之改变。（摄氏度 * 1.8 + 32 = 华氏度）
```

[属性方法的死循环误区:](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/Rectangle.py)
```
示例介绍：
定义一个矩形类，默认有长宽属性。
如果为一个 square 属性赋值，那么矩形则变成正方形，边长为 square 的值

示例中定义了三种写法。
写法一 是陷入无限递归的写法（易犯错写法）。
然后给出了两种解决方法，分别是利用对象的 __dict__ ，和通过 super() 调用基类的对应方法

附：__dict__  ：以字典的形式显示对象中的所有属性以及其对应的值。 
```
[属性相关魔法方法](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/MagicFun_1.py)<br/>
```
介绍内容相关： __getattr__ ， __getattribute__  ，__setattr__ ， __delattr__
```
[由浅入深的实现一个计时器（1-6）](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/TimerDemo.py)<br/>
```
计时器介绍：基础用法
>>> t1 = MyTimer()
>>> t1.start() 启动计时器
>>> t1.stop() 停止计时器
>>> t1 输出计时时间

>>> t2 = MyTimer()
    ...
>>> t1 + t2 输出两个计时器所计时的总和
```

#### 2018年01月29日
[基础魔法方法测试：](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/MagicFun.py)<br/>
```
测试内容有：__new__() ,__init__() ,__del__() , 
反运算,增量赋值运算 ,__str__() ,__repr__() 
```
[class 的伪私有属性和方法，以及部分相关方法](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/ClassDemo.py)<br/>
#### 2018年01月28日
[EasyGui 简单测试](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/EasyGuiDemo.py)<br/>
[With 关键字](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/Key_With.py) - 简化我们每次在 finally 中进行 close 操作<br/>
[丰富的 else ](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/MoreElse.py) - （if elif else , while else , try except else ）<br/>
[Exception 的几种写法](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/ExceptionMain.py)<br/>
[Pickle 本地持久化存储数据](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/Pickle_Main.py)<br/>
[文件创建，读取，保存](https://github.com/lvfaqiang/PythonDemo/blob/master/demo/File_Main.py)