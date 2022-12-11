"""
http://www.pythontip.com/
基础算法训练174道
"""
def add_ab():#输入整数相加
    a=int(input())
    b=int(input())
    if(a==b):
        num=a+b
    else:
        num=(a+b)*2
    return num

def num_reverse():#python自带函数.sort用于数组排序
    l = [8, 2, 50, 3, 2]
    l.sort()#数组.sort()用于排序
    print(l)

def str_reserve():#str[::-1]用于字符串反转
    a ='xydz'
    a=a[::-1]
    print(a)
    print(a[-1])
    print(a[-2])
    print(a[:-1])
    # lista=list(a)
    # lista.reverse()
    # a=str(lista)
    # print(a)
    # for c in reversed(a):
    #     b.format(c)
    #
    # print(b)
    # print(str(reversed(a)))
    # for i in (len(a)-1,1):
    #     print(a[i])
    # # print(a[len(a)-1])

def print_key():
    #给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key按照字典序升序排列(注意key可能是字符串）。
    #例如：a={1:1,2:2,3:3}, 则输出：1,2,3
    #http://www.pythontip.com/coding/code_oj_case/5
    #正确答案:
    """
    def solve_it():
    list1 = []
    for key in a:
        list1.append(str(key))
    return ",".join(list1)
    '''
    pythontip oj不同于传统oj，代码里面直接使用变量，无需要提前声明，免去复杂的输入解析
    life is short, so i user python~
    '''
    print(solve_it())  # 答案需要输出
    :return:
    """
    a = {1: 1, 6: 2, 3: 3}
    # for key in a:
    b=list(a.keys())
    b.sort()
    print(str(b).replace('[','').replace(']',''))

def str_odd():
    """
    第5题：输出字符奇数位置的字符串,中等
    题目描述：
    给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）。
    例如：a=‘xyzwd’
    则输出:xzd
    :return:
    """
    # a='asdoihfuheh'
    a = "0123456789"
    print(list(a))
    for i in range(0,len(a),2):
        print(a[i],end='')

def primerNumber_print():
    """
    第6题：求解100以内的所有素数
    中等
    题目描述：
    输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。
    :return:
    """
    list2=[]
    for i in range(2, 101):
        list = []
        for j in range(2, i):
            if (i % j != 0):
                a = 0
            else:
                a = 1
            # index=sum(a)
            list.append(a)
        if(sum(list)==0):
            list2.append(i)
    for n in list2:
        if(n!=list2[len(list2)-1]):
          print(n,end=' ')
        else:print(n)
    #         list2.append(str(i))
    # print(' '.join(list2))
    # print(list2)
    # print(str(list2).replace('[','').replace(']','').replace(',',' '))

def area_rectangle():
    """
    第7题：求矩形面积
    中等
    题目描述：
    已知矩形长a,宽b,输出其面积和周长，面积和周长以一个空格隔开。
    例如：a = 3, b = 8
    则输出：24 22
    """
    a=3
    b=8
    print(a*b,'',(a+b)*2)

def mid_number():
    """
    第8题：求中位数
    中等
    题目描述：
    给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。
    例如： L=[0,1,2,3,4]
    则输出：2
    :return:
    """
    # L = [0, 13, 52, 32, 34,]
    L=[1,2,3,4,5,6,7,8]
    L.sort()
    if(len(L)%2==1):
        print(L[len(L)//2])#python除法取整：
    else:
        print(((len(L)/2)+(len(L)/2+1))/2)

def question_9(a,b):
    """
    第9题：最大公约数
    中等
    题目描述：
    给你两个正整数a和b， 输出它们的最大公约数。
    例如：a = 3, b = 5
    则输出：1
    :return:
    """
    # a=1200
    # b=19208
    print(divisor_list(a))
    print(divisor_list(b))
    for i in divisor_list(a)[::-1]:
        if(i in divisor_list(b)):
            print(i)
            break
    # 一个数的约数list1[]
    # list1 = []
    # list2=[]
    # i = 1000
    # for j in range(1, i + 1):
    #     if (i % j == 0):
    #         list1.append(j)
    # print(list1)

#求最大公约数Greatest common divisor
def divisor_list(i):
    list1=[]
    for j in range(1, i + 1):
        if (i % j == 0):
            list1.append(j)
    return list1

def question_10():
    def divisor(a, b):
        for i in divisor_list(a)[::-1]:
            if (i in divisor_list(b)):
                break
        return i
    """
    第10题：最小公倍数
    中等
    题目描述：给你两个正整数a和b， 输出它们的最小公倍数。
    例如：a = 3, b = 5  则输出：15
    :return:
    """
    """
    最大公因数和最小公倍数之间的性质：
    两个自然数的乘积等于这两个自然数的最大公约数和最小公倍数的乘积。
    最小公倍数的计算要把三个数的公有质因数和独有质因数都要找全，最后除到两两互质为止。
    最小公倍数特点：倍数的只有最小的没有最大，因为两个数的倍数可以无穷大。
    :return: 
    """
    a = int(input())
    b = int(input())
    return int(a * b / int(divisor(a, b)))  # your answer

def question_11():
    """
    第11题：结尾0的个数
    中等
    题目描述：
    给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。
    例如： L=[2,8,3,50],
    则输出：2
    :return:
    """
    # 10=5*2,数10的个数只用考虑2*5
    # print(divisor_list(100))
    # print(divisor_list(1000))
    # print(divisor_list(1000000))
    # L = [4, 2, 25, 100, 3]
    L = [2, 8, 3, 50,10,10,1000]
    l=[]
    n2=0
    n5=0
    for i in L:
        while(i%2==0):
            n2+=1
            i=i/2
        l.append(int(i))
    for i in l:
        while(i%5==0):
            n5+=1
            i=i/5
        # l.append(int(i))
    print(n2,n5)
    print(n2 if n2<n5 else n5)#精简判断写法
    print(l)
    # a=1
    # for n in L:
    #     a=a*n
    # print(a)

def question_12():
    """
    给你一个正整数列表 L, 判断列表内所有数字乘积的最后一个非零数字的奇偶性。如果为奇数输出1,偶数则输出0.。
    例如：L=[2,8,3,50]
    则输出：0
    :return:
    """
    # 就是每个数分解2，看最后有多少个2
    L = [2, 8, 3, 50,2,4,6]
    l=[]
    n=0
    for i in L:
        while(i%2==0):
            i=i/2
            n+=1
        l.append(int(i))
    print(l)
    print(n)
    print('1' if (n % 2 == 1) else '0')#n%2!=1

def question_13():
    """
    第13题：光棍的悲伤
    中等
    题目描述：
    光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。
    小Py光棍几十载，光棍自有光棍的快乐。让我们勇敢地面对光棍的身份吧，
    现在就证明自己：
    给你一个整数a，数出a在二进制表示下1的个数，并输出。
    例如：a=7
    则输出：3
    :return: 简单的和1一样
    """
    a=12
    print(str(bin(a)).replace('0b','').count('1'))#使用二进制转换函数bin()

def question_14():
    """
    第14题：Python之美
    中等
    题目描述：输出Python之禅。
    注意：输出python之禅的源码即可，不要转换为英文。（小小的提示：print this.s)
    :return:
    """
    import this#答案提交只写这一句，不用def函数

def question_15():
    """
    第15题：大小写转换
    简单
    题目描述：
    给定一个字符串a, 将a中的大写字母 转换成小写，其它字符不变，并输出。
    例如：a="aaaaaabbbDDDDD"
    则输出：aaaaaabbbddddd
    :return:
    """
    a = "aaaaaabbbDDDDD"
    print(a.lower())

def question_16():
    """
    第16题：人民币金额打印
    困难
    题目描述：
    银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
    在中文大写方式中，0到10以及100、1000、10000被依次表示为：    零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾 佰 仟 万
    以下的例子示范了阿拉伯数字到人民币大写的转换规则：
    1	壹圆
    11	壹拾壹圆
    111	壹佰拾壹圆
    101	壹佰零壹圆
    -1000	负壹仟圆
    1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆
    现在给你一个整数a(|a|<100000000), 请你打印出人民币大写表示.
    例如：a=1
    则输出：壹圆
    注意：请以Unicode的形式输出答案。提示：所有的中文字符，在代码中直接使用其Unicode的形式即可满足要求，中文的Unicode编码可以通过如下方式获得：u'壹'。
    注意：代码无需声明编码！！不要在代码头部声明文件编码，否则会导致语法错误！
    Note：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
    :return:
    """

question_16()
# question_15()
# question_14()
# question_13()
# question_12()
# question_11()
# question_10()
# question_9()
# mid_number()
# area_rectangle()
# primerNumber_print()
# str_odd()
# print(add_ab())
# num_reverse()
# print_key()