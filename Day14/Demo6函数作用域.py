#_author: liuz
#date: 2017/12/8

#函数作用域

'''
python中的作用域分4种情况：
L：local，局部作用域，即函数中定义的变量；
E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的； 外层作用域
G：globa，全局变量，就是模块级别定义的变量；                                            全局作用
B：built-in，系统固定模块里面的变量，比如int, bytearray等。 系统定义                     python内置作用域
搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。
'''
x = int(2.9)  # int built-in
g_count = 0  # global        全局变量
def outer():
    o_count = 1  # enclosing
    def inner():
        i_count = 2  # local
        print(i_count)
    # print(i_count) 找不到
    inner()
outer()

#局部作用域变量不能修改全局作用域变量
#如果直接在内部修改 相当于在内部重新创建了一个同名变量和全局变量没有任何关系
#如果想修改全局 必须使用 global关键字 声明

'''
def getcount():
    global g_count  #局部内修改全局变量  必须使用global声明
    print(g_count)
    g_count=5
    print(g_count)
getcount()
'''
'''
def Changeen():
    num=10
    def inner():
        nonlocal num  #局部内修改 外层作用域 使用关键字nonlocal声明
        print(num)
        num=20
    inner()
    print(num)
Changeen()
'''

'''
总结
（1）变量查找顺序：LEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；

（2）只有模块、类、及函数才能引入新作用域；

（3）对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；

（4）内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，
     嵌套作用域变量要使用nonlocal关键字。nonlocal是python3新增的关键字，
     有了这个 关键字，就能完美的实现闭包了。 

'''

