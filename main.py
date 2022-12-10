# This is a sample Python script.
import datetime
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def keywods_print():  # 打印python关键字
    import keyword
    keyword.kwlist
    for i in keyword.kwlist:
        print(i, end=' ')


def str_print():
    str1 = """ 
         Python 中单引号 ' 和双引号 " 使用完全相同。
         使用三引号可以指定一个多行字符串。
         反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
         按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
         字符串可以用 + 运算符连接在一起，用 * 运算符重复。
         Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
         Python 中的字符串不能改变。
         Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
         字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
        """
    print(str1)
    print(str1.__len__())

    """
            Ctrl+Alt+L：快速整理代码
            Ctrl+Shif+左右键：快速选中，并进行移动 
            Tab键将选中部分整体右移
            
            Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：

            
            """


def acc():
    import sys
    sys.stdout.write('输出一行字符串' + '\d' + '\n')
    pass


def random_number():
    a = []
    for i in range(0, 20):
        v = random.randint(1, 6)
        a.extend(str(v))
    print(a)


def time_print():#import datetime函数可以将系统函数实例化为一个变量
    from datetime import datetime
    a =datetime.now()
    # month=datetime.now()
    # print(a,"今天是%s月%s日" % a.month %a.day)
    print(a)
    print("今天是%s年%s月%s日，现在是%s时%s分%s秒"%(a.year,a.month,a.day,a.hour,a.minute,a.second))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    keywods_print()
    str_print()
    acc()
    random_number()
    time_print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
