# coding=UTF-8
import codecs


def saveFile(boy, girl, count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'
    boy_file = codecs.open(file_name_boy, 'w', 'UTF-8')
    girl_file = codecs.open(file_name_girl, 'w', 'UTF-8')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def splitFile(fileName):
    '实现文件切割逻辑'
    f = codecs.open(fileName, 'r', 'UTF-8')

    ##f = open('/Users/apple/Desktop/talking.txt')
    boy = []
    girl = []
    count = 1

    for each in f:
        if each[:6] != '======':
            (role, line_spoken) = each.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)

        else:
            saveFile(boy, girl, count)
            count += 1

            boy = []
            girl = []

    saveFile(boy, girl, count)

    f.close()


splitFile('../talking.txt')
