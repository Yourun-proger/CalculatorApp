from tkinter import *


def action(act):
    global stack
    stack += act
    n.configure(text=stack)


def result():
    global stack
    if stack != '':
        stack = str(eval(stack))
        n.configure(text=stack)


def clear():
    global stack
    stack = ''
    n.configure(text=stack)


def form0():
    action('0')


def form1():
    action('1')


def form2():
    action('2')


def form3():
    action('3')


def form4():
    action('4')


def form5():
    action('5')


def form6():
    action('6')


def form7():
    action('7')


def form8():
    action('8')


def form9():
    action('9')


def formpl():
    action('+')


def formmin():
    action('-')


def formum():
    action('*')


def formdev():
    action('/')


def formpoint():
    action('.')


calc = Tk()
calc.title("Calculator")
calc.geometry("425x348")
stack = ''
title = Label(calc, text="Calculator", font=("Segoe UI", 15))
title.grid(column=1, row=0)
calc.resizable(0, 0)
x = (calc.winfo_screenwidth() - calc.winfo_reqwidth()) / 2.5
y = (calc.winfo_screenheight() - calc.winfo_reqheight()) / 2.5
calc.wm_geometry('+%d+%d' % (x, y))
n = Label(calc, text=stack, font=("Segoe UI", 15))
n.grid(column=1, row=1)

but = Button(calc, text="\n\t7\t\n", command=form7)
but.grid(column=0, row=2)
but = Button(calc, text="\n\t8\t\n", command=form8)
but.grid(column=1, row=2)
but = Button(calc, text="\n\t9\t\n", command=form9)
but.grid(column=2, row=2)
but = Button(calc, text="\n\t/\t\n", command=formdev)
but.grid(column=3, row=2)

but = Button(calc, text="\n\t4\t\n", command=form4)
but.grid(column=0, row=3)
but = Button(calc, text="\n\t5\t\n", command=form5)
but.grid(column=1, row=3)
but = Button(calc, text="\n\t6\t\n", command=form6)
but.grid(column=2, row=3)
but = Button(calc, text="\n\t*\t\n", command=formum)
but.grid(column=3, row=3)

but = Button(calc, text="\n\t1\t\n", command=form1)
but.grid(column=0, row=4)
but = Button(calc, text="\n\t2\t\n", command=form2)
but.grid(column=1, row=4)
but = Button(calc, text="\n\t3\t\n", command=form3)
but.grid(column=2, row=4)
but = Button(calc, text="\n\t-\t\n", command=formmin)
but.grid(column=3, row=4)

but = Button(calc, text="\n\t.\t\n", command=formpoint)
but.grid(column=0, row=5)
but = Button(calc, text="\n\t0\t\n", command=form0)
but.grid(column=1, row=5)
but = Button(calc, text="\n\tC\t\n", command=clear)
but.grid(column=2, row=5)
but = Button(calc, text="\n\t+\t\n", command=formpl)
but.grid(column=3, row=5)

but = Button(calc, text="\n\t=\t\n", command=result)
but.grid(column=1, row=6)

if __name__ == '__main__':
    calc.mainloop()
