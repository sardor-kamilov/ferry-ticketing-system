from tkinter import*
from tkinter import Tk, StringVar, ttk
import random
import time;
import datetime

root = Tk()
root.geometry("1350x750+0+0")
root.title("Ferry Ticketing")
root.configure(background='black')

Tops = Frame(root, width = 1350, height = 100, relief = 'raise')
Tops.pack(side=TOP)

f1 = Frame(root, width = 900, height = 650, bd = 8, relief = 'raise')
f1.pack(side=LEFT)
f2 = Frame(root, width = 440, height = 650, bd = 8, relief = 'raise')
f2.pack(side=RIGHT)

ft2 = Frame(f2, width = 440, height = 650, bd = 12, relief = 'raise')
ft2.pack(side=LEFT)
fb2 = Frame(f2, width = 440, height = 50, bd = 16, relief = 'raise')
fb2.pack(side=BOTTOM)

f1a = Frame(f1, width = 900, height = 330, bd = 8, relief = 'raise')
f1a.pack(side=TOP)
f2a = Frame(f1, width = 900, height = 320, bd = 6, relief = 'raise')
f2a.pack(side=BOTTOM)

topLeft1 = Frame(f1a, width = 300, height = 200, bd = 16, relief = 'raise')
topLeft1.pack(side=LEFT)
topLeft2 = Frame(f1a, width = 300, height = 200, bd = 16, relief = 'raise')
topLeft2.pack(side=RIGHT)
topLeft3 = Frame(f1a, width = 300, height = 200, bd = 16, relief = 'raise')
topLeft3.pack(side=RIGHT)
#-----------------------------------------------------------------------------
bottomLeft1 = Frame(f2a, width = 450, height = 450, bd = 14, relief = 'raise')
bottomLeft1.pack(side=LEFT)

bottomLeft2 = Frame(f2a, width = 450, height = 450, bd = 14, relief = 'raise')
bottomLeft2.pack(side=RIGHT)
#-----------------------------------------------------------------------------
Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
lblTitle=Label(Tops, font=('arial', 40, 'bold'), text="Ferry Ticketing System", width=44, justify='center')
lblTitle.grid(row=0, column=0)
#---------------------------------Variables-------------------------------
varl = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
#---------------------------------Create Widget topLeft1-------------------------------
lblClass = Label(topLeft1, font=('arial', 22, 'bold'), text='Class', bd=8)
lblClass.grid(row=0, column=0, sticky=W, columnspan = 2)
chkStandard = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='Standard', variable = varl, onvalue=1, offvalue=0)
chkStandard.grid(row=1, column=0, sticky=W)
chkEconomy = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='Economy', variable = var2, onvalue=1, offvalue=0)
chkEconomy.grid(row=2, column=0, sticky=W)
chkFirstClass = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='First Class', variable = var3, onvalue=1, offvalue=0)
chkFirstClass.grid(row=3, column=0, sticky=W)
#---------------------------------Create Widget topLeft2-------------------------------
lblSelect = Label(topLeft3, font=('arial', 20, 'bold'), text='Destination Selector', bd=8)
lblSelect.grid(row=0, column=0, sticky=W)
lblDestination = Label(topLeft3, font=('arial', 20, 'bold'), text='Destination', bd=2)
lblDestination.grid(row=1, column=0, sticky=W)
cbodDestination=ttk.Combobox(topLeft3, textvariable = var4, state='readonly', font=('arial', 16, 'bold'), width=12)
cbodDestination['value']=('', 'Kuala Lumpur', 'Penang', 'LangKawi', 'Singapore', 'Bukit Jalil')
cbodDestination.current(0)
cbodDestination.grid(row=1, column=1)

chkAdult = Checkbutton(topLeft3, font=('arial', 20, 'bold'), text='Adult', variable = var4, onvalue=1, offvalue=0)
chkAdult.grid(row=2, column=0, sticky=W)
chkChild = Checkbutton(topLeft3, font=('arial', 20, 'bold'), text='Child', variable = var5, onvalue=1, offvalue=0)
chkChild.grid(row=3, column=0, sticky=W)
#---------------------------------Ticket-------------------------------
lblClass = Label(topLeft2, font=('arial', 22, 'bold'), text='Ticket Type', bd=8)
lblClass.grid(row=0, column=0, sticky=W)
chkSingle = Checkbutton(topLeft2, font=('arial', 20, 'bold'), text='Single', variable = var6, onvalue=1, offvalue=0)
chkSingle.grid(row=1, column=0, sticky=W)
entSingle = Entry(topLeft2, font=('arial', 20, 'bold'), textvariable = var5, bd=2, width=8)
entSingle.grid(row=1, column=1, sticky=W)
chkReturn = Checkbutton(topLeft2, font=('arial', 20, 'bold'), text='Return', variable = var7, onvalue=1, offvalue=0)
chkReturn.grid(row=2, column=0, sticky=W)
entReturn = Entry(topLeft2, font=('arial', 20, 'bold'), textvariable = var6, bd=2, width=8)
entReturn.grid(row=2, column=1, sticky=W)
lblCommit = Label(topLeft2, font=('arial', 22, 'bold'), text='Comment', bd=8)
lblCommit.grid(row=3, column=0, sticky=W)
entCommit = Entry(topLeft2, font=('arial', 20, 'bold'), textvariable = var7, bd=2, width=8)
entCommit.grid(row=3, column=1, sticky=W)
#---------------------------------Calculator-------------------------------
text_Input=StringVar()
txtDisplay = Entry(bottomLeft2, font=('arial', 10, 'bold'), textvariable=text_Input, bd=8, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="7", bg="powder blue", command = lambda:btnClick(7)).grid(row=2, column=0)
btn8=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="8", bg="powder blue", command = lambda: btnClick(8)).grid(row=2, column=1)
btn9=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="9", bg="powder blue", command = lambda: btnClick(9)).grid(row=2, column=2)
Addition=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="+", bg="powder blue", command = lambda: btnClick("+")).grid(row=2, column=3)
#-------------------------------------------------------------------------
btn4=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="4", bg="powder blue", command = lambda: btnClick(4)).grid(row=3, column=0)
btn5=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="5", bg="powder blue", command = lambda: btnClick(5)).grid(row=3, column=1)
btn6=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="6", bg="powder blue", command = lambda: btnClick(6)).grid(row=3, column=2)
Subtracktion=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="-", bg="powder blue", command = lambda: btnClick("-")).grid(row=3, column=3)
#-------------------------------------------------------------------------
btn1=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="1", bg="powder blue", command = lambda: btnClick(1)).grid(row=4, column=0)
btn2=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="2", bg="powder blue", command = lambda: btnClick(2)).grid(row=4, column=1)
btn3=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="3", bg="powder blue", command = lambda: btnClick(3)).grid(row=4, column=2)
Multiply=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="*", bg="powder blue", command = lambda: btnClick("*")).grid(row=4, column=3)
#-------------------------------------------------------------------------
btn0=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="0", bg="powder blue", command = lambda: btnClick(0)).grid(row=5, column=0)
btnClear=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="C", bg="powder blue").grid(row=5, column=1)
btnEquals=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="=", bg="powder blue").grid(row=5, column=2)
Division=Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'), text="/", bg="powder blue", command = lambda: btnClick("/")).grid(row=5, column=3)
#------------------------------------------Tax Sub Total-------------------------------
lblStateTax = Label(bottomLeft1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)
txtStateTax = Entry(bottomLeft1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="#ffffff", justify='right')
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(bottomLeft1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(bottomLeft1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="#ffffff", justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = Label(bottomLeft1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(bottomLeft1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="#ffffff", justify='right')
txtTotalCost.grid(row=5, column=3)

#-------------------------------------------------------------------------












6








root.mainloop()
