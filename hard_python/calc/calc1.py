#turtle库是基于tkinter库开发而来的
from tkinter import *
import re

#验证输入是否合法
#-228.12
#首先是+-开头,但也可以没有符号
#1到多个数字
#可以有.，也可以没.
#1到多个数字，也可以没有
# '^[+-]?[\d]+[.]?[\d]*$'
def validate_input():
    reg = '^[+-]?[\d]+[.]?[\d]*$'
    r1 = re.match(reg,op1.get())
    r2 = re.match(reg,op2.get())
    return r1 and r2



def cmd_math(ops):
    is_valid = validate_input()
    if(is_valid):
        op1_value = float(op1.get())
        op2_value = float(op2.get())
        if(ops == '+'):
            res = op1_value + op2_value
        elif(ops == '-'):
            res = op1_value - op2_value
        elif(ops == '*'):
            res = op1_value * op2_value
        elif(ops == '/'):
            res = op1_value / op2_value
        elif(ops == '%'):
            res = op1_value % op2_value
        elif(ops == '//'):
            res = op1_value // op2_value
        elif(ops == '**'):
            res = op1_value ** op2_value
        elif(ops == 'clear'):
            res = op1_value + op2_value

        res_var.set(round(res, 2))
    else:
        res_var.set('请输入正确的操作数')

def clear():
    op1.delete(0, END)
    op2.delete(0, END)   

def calc_art():
    ex = op_art.get()
    res = eval(ex)
    res_str.set(res)


#1. 创建1个根窗口对象
root = Tk() 

menubar = Menu(root)
menu1 = Menu(menubar)
menu1.add_command(label='普通', command=lambda:f1.tkraise())
menu1.add_command(label='文艺', command=lambda:f2.tkraise())
menubar.add_cascade(label='模式', menu=menu1)
root.config(menu=menubar)

#画布2
f2 = Frame(root)
f2.grid(row=0, column=0, sticky='news')
op_art = Entry(f2)
btn_art = Button(f2, text='计算', command=calc_art)
res_str = StringVar()
res_str.set('计算结果显示在这里')
Label_art = Label(f2, textvariable=res_str)
op_art.pack(fill=BOTH)
btn_art.pack(fill=BOTH)
Label_art.pack(fill=BOTH)


#画布1
f1 = Frame(root)
f1.grid(row=0, column=0, sticky='news')

#2. 创建组件对象，创建组件的时候一定要指定组件所在的容器
# 组件：Entry对象, button对象, Label对象
op1 = Entry(f1)
op2 = Entry(f1)

btn_add = Button(f1, text='+', padx=50, pady=10, command=lambda:cmd_math('+'))
btn_sub = Button(f1, text='-', padx=50, pady=10, command=lambda:cmd_math('-'))
btn_mul = Button(f1, text='*', padx=50, pady=10, command=lambda:cmd_math('*'))
btn_div = Button(f1, text='/', padx=50, pady=10, command=lambda:cmd_math('/'))
btn_mod = Button(f1, text='%', padx=50, pady=10, command=lambda:cmd_math('%'))
btn_f_d = Button(f1, text='//', padx=50, pady=10, command=lambda:cmd_math('//'))
btn_exp = Button(f1, text='**', padx=50, pady=10, command=lambda:cmd_math('**'))
btn_clr = Button(f1, text='clear', padx=50, pady=10, command=clear)

#创建变量对象
res_var = StringVar()

res_var.set('Show Result')
result = Label(f1, textvariable=res_var, pady=50)
# lbl_op1 =Label(root, text='操作数1') 
# lbl_op2 =Label(root, text='操作数2') 

#3. 需要把组件显示出来：grid，pack
# op1.pack()
# op2.pack()
op1.grid(row=0, column=0, columnspan=4, sticky='WE')
op2.grid(row=1, column=0, columnspan=4, sticky='WE')

btn_add.grid(row=2, column=0, sticky='WE')
btn_sub.grid(row=2, column=1, sticky='WE')
btn_mul.grid(row=2, column=2, sticky='WE')
btn_div.grid(row=2, column=3, sticky='WE')
btn_mod.grid(row=3, column=0, sticky='WE')
btn_f_d.grid(row=3, column=1, sticky='WE')
btn_exp.grid(row=3, column=2, sticky='WE')
btn_clr.grid(row=3, column=3, sticky='WE')

result.grid(row=4, column=0, columnspan=4, sticky='WE')
# lbl_op1.grid(row=0, column=0,)
# lbl_op2.grid(row=1, column=0,)

#root.geometry('500x500')

#刷新
mainloop()