from tkinter import *
import math

window = Tk()
window.title("Calculator")
window.geometry("398x568")
s = ""

entry = Entry(window)
entry.grid(column=0, row=0, stick='wens', columnspan=5)

def onClick(n):
    global s
    s += n
    entry.insert(END, n)
def ac():
    global s
    s = ""
    entry.delete(0, END)
def delete():
    global s
    x = len(s) - 1
    s = s[:x]
    entry.delete(0, END)
    entry.insert(0, s)
def eXit():
    exit(0)
def formatter():
    global s
    sq = s.count('√')
    si = s.count("sin")
    co = s.count("cos")
    tg = s.count("tg")
    ctg = s.count("ctg")
    deg = s.count('^')
    tg -= ctg
    while si != 0:                 #sin
        ind = s.find("sin")
        ind2 = ind + 4
        while s[ind2] != ')':
            ind2 += 1
        num = float(s[(ind+4):ind2])
        num = math.sin(num * (math.pi / 180))
        if ind2 == len(s) - 1:
            old = s[ind:]
        else:
            old = s[ind:ind2 + 1]
        new = str(num)
        si -= s.count(old)
        s = s.replace(old, new)
    while co != 0:                 #cos
        ind = s.find("cos")
        ind2 = ind + 4
        while s[ind2] != ')':
            ind2 += 1
        num = float(s[(ind+4):ind2])
        num = math.cos(num * (math.pi / 180))
        if ind2 == len(s) - 1:
            old = s[ind:]
        else:
            old = s[ind:ind2 + 1]
        new = str(num)
        co -= s.count(old)
        s = s.replace(old, new)
    while ctg != 0:                     #ctg
        ind = s.find("ctg")
        ind2 = ind + 4
        while s[ind2] != ')':
            ind2 += 1
        num = float(s[(ind+4):ind2])
        num = math.cos(num * (math.pi / 180)) / math.sin(num * (math.pi / 180))
        if ind2 == len(s) - 1:
            old = s[ind:]
        else:
            old = s[ind:ind2 + 1]
        new = str(num)
        ctg -= s.count(old)
        s = s.replace(old, new)
    while tg != 0:                 #tg
        ind = s.find("tg")
        ind2 = ind + 3
        while s[ind2] != ')':
            ind2 += 1
        num = float(s[(ind+3):ind2])
        num = math.tan(num * (math.pi / 180))
        if ind2 == len(s) - 1:
            old = s[ind:]
        else:
            old = s[ind:ind2+1]
        new = str(num)
        tg -= s.count(old)
        s = s.replace(old, new)
    while sq != 0:  #sqrt
        ind = s.find('√')
        ind2 = ind + 2
        while s[ind2] != ')':
            ind2 += 1
        num = float(s[(ind+2):ind2])
        num = math.sqrt(num)
        if ind2 == len(s) - 1:
            old = s[ind:]
        else:
            old = s[ind:ind2 + 1]
        new = str(num)
        sq -= s.count(old)
        s = s.replace(old, new)
    while deg != 0:
        ind = s.find('^')
        ind1 = ind
        ind2 = ind
        while s[ind1] not in "+-*/()" and ind1 != 0:
            ind1 -= 1
        while s[ind2] not in "+-*/()" and ind2 != len(s) - 1:
            ind2 += 1
        if ind1 == 0:
            num1 = float(s[:ind])
        else:
            num1 = float(s[ind1 + 1:ind])
        if ind2 == len(s) - 1:
            num2 = float(s[ind+1:])
        else:
            num2 = float(s[ind+1:ind2+1])
        new = str(num1**num2)
        if num1 % 1 == 0:
            num1 = int(num1)
        if num2 % 1 == 0:
            num2 = int(num2)
        old = str(num1) + '^' + str(num2)
        deg -= s.count(old)
        s = s.replace(old, new)

def count():
    global s
    try:
        formatter()
        s = eval(s)
        entry.delete(0, END)
        entry.insert(0, s)
    except BaseException:
        entry.delete(0, END)
        entry.insert(0, "Error")

btn1 = Button(window, text="1", bd=3, font='Times 15', command=lambda: onClick('1')).grid(column=0, row=1, stick='wens', padx=2, pady=2)
btn2 = Button(window, text="2", bd=3, font='Times 15', command=lambda: onClick('2')).grid(column=1, row=1, stick='wens', padx=2, pady=2)
btn3 = Button(window, text="3", bd=3, font='Times 15', command=lambda: onClick('3')).grid(column=2, row=1, stick='wens', padx=2, pady=2)
btn4 = Button(window, text="4", bd=3, font='Times 15', command=lambda: onClick('4')).grid(column=0, row=2, stick='wens', padx=2, pady=2)
btn5 = Button(window, text="5", bd=3, font='Times 15', command=lambda: onClick('5')).grid(column=1, row=2, stick='wens', padx=2, pady=2)
btn6 = Button(window, text="6", bd=3, font='Times 15', command=lambda: onClick('6')).grid(column=2, row=2, stick='wens', padx=2, pady=2)
btn7 = Button(window, text="7", bd=3, font='Times 15', command=lambda: onClick('7')).grid(column=0, row=3, stick='wens', padx=2, pady=2)
btn8 = Button(window, text="8", bd=3, font='Times 15', command=lambda: onClick('8')).grid(column=1, row=3, stick='wens', padx=2, pady=2)
btn9 = Button(window, text="9", bd=3, font='Times 15', command=lambda: onClick('9')).grid(column=2, row=3, stick='wens', padx=2, pady=2)
btn0 = Button(window, text="0", bd=3, font='Times 15', command=lambda: onClick('0')).grid(column=1, row=4, stick='wens', padx=2, pady=2)
btnCount = Button(window, text="=", bd=3, font='Times 15', command=count).grid(column=4, row=5, stick='wens', padx=2, pady=2)
btnPlus = Button(window, text="+", bd=3, font='Times 15', command=lambda: onClick('+')).grid(column=3, row=1, stick='wens', padx=2, pady=2)
btnMinus = Button(window, text="-", bd=3, font='Times 15', command=lambda: onClick('-')).grid(column=3, row=2, stick='wens', padx=2, pady=2)
btnMultiply = Button(window, text="*", bd=3, font='Times 15', command=lambda: onClick('*')).grid(column=3, row=3, stick='wens', padx=2, pady=2)
btnDivision = Button(window, text="/", bd=3, font='Times 15', command=lambda: onClick('/')).grid(column=3, row=4, stick='wens', padx=2, pady=2)
btnRadical = Button(window, text="√", bd=3, font='Times 15', command=lambda: onClick('√(')).grid(column=0, row=5, stick='wens', padx=2, pady=2)
btnDegree = Button(window, text="^", bd=3, font='Times 15', command=lambda: onClick('^')).grid(column=1, row=5, stick='wens', padx=2, pady=2)
btnSin = Button(window, text="Sin", bd=3, font='Times 15', command=lambda: onClick("sin(")).grid(column=4, row=3, stick='wens', padx=2, pady=2)
btnCos = Button(window, text="Cos", bd=3, font='Times 15', command=lambda: onClick("cos(")).grid(column=4, row=4, stick='wens', padx=2, pady=2)
btnTg = Button(window, text="Tg", bd=3, font='Times 15', command=lambda: onClick('tg(')).grid(column=2, row=5, stick='wens', padx=2, pady=2)
btnCtg = Button(window, text="Ctg", bd=3, font='Times 15', command=lambda: onClick('ctg(')).grid(column=3, row=5, stick='wens', padx=2, pady=2)
btnBracketL = Button(window, text="(", bd=3, font='Times 15', command=lambda: onClick('(')).grid(column=0, row=4, stick='wens', padx=2, pady=2)
btnBracketR = Button(window, text=")", bd=3, font='Times 15', command=lambda: onClick(')')).grid(column=2, row=4, stick='wens', padx=2, pady=2)
btnAC = Button(window, text="AC", bd=3, font='Times 15', command=ac).grid(column=4, row=1, stick='wens', padx=2, pady=2)
btnDel = Button(window, text="<-", bd=3, font='Times 15', command=delete).grid(column=4, row=2, stick='wens', padx=2, pady=2)
btnDot = Button(window, text='.', bd=3, font='Times 15', command=lambda: onClick('.')).grid(column=0, row=6, stick='wens', padx=2, pady=2)
btnExit = Button(window, text="Exit", bd=3, font='Times 15', command=eXit).grid(column=1, row=6, stick='wens', columnspan=4, padx=2, pady=2)

window.grid_columnconfigure(0, minsize=80)
window.grid_columnconfigure(1, minsize=80)
window.grid_columnconfigure(2, minsize=80)
window.grid_columnconfigure(3, minsize=80)
window.grid_columnconfigure(4, minsize=80)

window.grid_rowconfigure(0, minsize=30)
window.grid_rowconfigure(1, minsize=90)
window.grid_rowconfigure(2, minsize=90)
window.grid_rowconfigure(3, minsize=90)
window.grid_rowconfigure(4, minsize=90)
window.grid_rowconfigure(5, minsize=90)
window.grid_rowconfigure(6, minsize=90)

window.mainloop()
    