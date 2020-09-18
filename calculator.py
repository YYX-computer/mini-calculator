# magic remark
# -*- encoding:utf-8 -*-
try:
	import math
except:
	print('please install math lib')
	print('use `pip install math` to do it')
	print('and use `python -c "import math"` to double-check it')
try:
	import tkinter as tk
	import tkinter.messagebox as msg
except:
	import Tkinter as tk
	import tkMessageBox as msg
base = tk.Tk()
n = 0
keys = ['+/-','x+y','x-y','x*y','x/y','x!','x√y','log x(y)','x^y']
tk.Label(base,text='x:').grid(column = 0,row = 0)
tk.Label(base,text='y:').grid(column = 2,row = 0)
x = tk.StringVar()
y = tk.StringVar()
entry_x = tk.Entry(base,textvariable=x)
entry_y = tk.Entry(base,textvariable=y)
entry_x.grid(column = 1,row = 0)
entry_y.grid(column = 3,row = 0)
def factorial(x):
	res = 1
	for i in range(1,x + 1):
		res *= i
	return res
root = lambda x,y:pow(x,y / 1)
log = math.log
def cal(op):
	global x,y
	_x = x.get()
	_y = y.get()
	if(op in ['+/-','x!','x√y','log x(y)','x^y']):
		if(op == '+/-'):
			op = '-x'
		elif(op == 'x!'):
			op = 'factorial(x)'
		elif(op == 'x√y'):
			op = 'root(x,y)'
		elif(op == 'log x(y)'):
			op = 'log(x,y)'
		elif(op == 'x^y'):
			op = 'x**y'
	op = op.replace('x',_x)
	op = op.replace('y',_y)
	try:
		_x = eval(op)
		x.set(str(_x))
		y.set('')
	except:
		msg.showerror('expression error','expression error')
tk.Button(base,text = '+/-',command = lambda:cal('+/-')).grid(column = 0,row = 1)
tk.Button(base,text = 'x+y',command = lambda:cal('x+y')).grid(column = 1,row = 1)
tk.Button(base,text = 'x-y',command = lambda:cal('x-y')).grid(column = 2,row = 1)
tk.Button(base,text = 'x*y',command = lambda:cal('x*y')).grid(column = 3,row = 1)
tk.Button(base,text = 'x/y',command = lambda:cal('x/y')).grid(column = 4,row = 1)
tk.Button(base,text = 'x!',command = lambda:cal('x!')).grid(column = 5,row = 1)
tk.Button(base,text = 'x√y',command = lambda:cal('x√y')).grid(column = 6,row = 1)
tk.Button(base,text = 'log x(y)',command = lambda:cal('log x(y)')).grid(column = 7,row = 1)
tk.Button(base,text = 'x^y',command = lambda:cal('x^y')).grid(column = 8,row = 1)
tk.mainloop()
