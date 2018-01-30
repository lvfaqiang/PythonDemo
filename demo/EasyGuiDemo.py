from easygui import *
import sys

while 1:
    message = "这里有一个小游戏，你想来试试么？"

    msgbox(message)  # 输出 ok

    title = "发强版提示"
    okBtn = "确定"
    msg = "请选择其中一项"

    chooice = ["xxoo", "codeing", "playing", "sleeping"]
    # choiceResult = indexbox(msg, title, chooice)
    choiceResult = choicebox(msg, title, chooice)
    print(choiceResult)
    if choiceResult in chooice:
        print(msgbox("你选择的结果是：" + str(choiceResult)))
    else:
        if ynbox("是否继续？"):
            pass
        else:
            sys.exit(0)

    msg = "你希望重新开始小游戏么？"

    # if ccbox(msg, "请选择"):
    #     pass
    # else:
    #     sys.exit(0)

    if boolbox(msg):  # boolbox 有点类似于 ynbox()
        pass
    else:
        sys.exit(0)
