import tkinter as tk
from tkinter.font import Font
from math import sqrt

####################################################################################################
root = tk.Tk()
root.title('calcuration')
root.resizable(False, False) # 不可縮放
####################################################################################################
# 顯示
font = Font(family='微軟正黑體', size=15)

formula = tk.StringVar(value = '')
tk.Label(root, textvariable = formula, anchor = 'w',
    font = font, height = 1).grid(row = 0, columnspan = 4, sticky = 'ew')

ans = tk.StringVar(value = 0)
tk.Label(root, textvariable = ans, anchor = 'w',
    font = font, height = 1).grid(row = 1, columnspan = 4, sticky = 'ew')

####################################################################################################
# 按鈕
font = Font(family='微軟正黑體', size=25)

next = True  # 是否已輸入數字
AC   = False # 是否能刪除算式
last = ''    # 最後一項
########################################
def allClean():
    global next, AC, last
    formula.set('')
    ans.set('0')
    next, AC, last = True, False, ''

def clean():
    global next, AC, last
    if AC or ans.get() == '0':
        allClean()
    ans.set('0')
    next = True

def addNumber(number):
    global next, AC, last
    if AC:
        allClean()
    ans.set(ans.get() + number if ans.get() != '0' else number)
    next = True

def addPoint():
    global next, AC
    if AC:
        allClean()
    if '.' not in ans.get():
        ans.set(ans.get() + '.')
        next = True

def addOperator(operator):
    global next, AC, last
    formulaStr = formula.get()
    last = operator
    # 已按過等於   -> 以答案作為算式繼續
    # 已按過運算子 -> 取代運算子
    if next or AC:
        if AC: # 已按過等於
            formulaStr = ''
            AC = False
        formula.set(formulaStr + ans.get() + operator)
        ans.set(0)
    else:
        formula.set(formulaStr[0:-1] + operator)
    next = False

def calculate():
    global next, AC, last
    if AC: # 已按過等於
        formula.set(ans.get() + last)
    else:
        last = last + ans.get()
        formula.set(formula.get() + ans.get())
    
    try:
        ans.set(eval(formula.get().replace('×', '*').replace('÷', '/')))
    except:
        ans.set('錯誤!')
    formula.set(formula.get() + '=')
    next, AC = False, True
########################################
# 按鍵配置
#
# C ← √ ÷
# 7 8 9 ×
# 4 5 6 -
# 1 2 3 +
# 0 . % =

# C (clean)
tk.Button(root, text = 'C', font = font, width = 3,
    command = clean).grid(row = 2, column = 0, sticky = 'ew')
# ← (BackSpace)
tk.Button(root, text = '←', font = font, width = 3,
    command = lambda: ans.set(ans.get()[:-1])).grid(row = 2, column = 1, sticky = 'ew')
# √ 
tk.Button(root, text = '√', font = font, width = 3,
    command = lambda: ans.set('sqrt(' +ans.get()+ ')')).grid(row = 2, column = 2, sticky = 'ew')
# ÷
tk.Button(root, text = '÷', font = font, width = 3,
    command = lambda: addOperator('÷')).grid(row = 2, column = 3, sticky = 'ew')

# row 1
# 7
tk.Button(root, text = '7', font = font, width = 3,
    command = lambda: addNumber('7')).grid(row = 3, column = 0, sticky = 'ew')
# 8
tk.Button(root, text = '8', font = font, width = 3,
    command = lambda: addNumber('8')).grid(row = 3, column = 1, sticky = 'ew')
# 9
tk.Button(root, text = '9', font = font, width = 3,
    command = lambda: addNumber('9')).grid(row = 3, column = 2, sticky = 'ew')
# ×
tk.Button(root, text = '×', font = font, width = 3,
    command = lambda: addOperator('×')).grid(row = 3, column = 3, sticky = 'ew')

# row 2
# 4
tk.Button(root, text = '4', font = font, width = 3,
    command = lambda: addNumber('4')).grid(row = 4, column = 0, sticky = 'ew')
# 5
tk.Button(root, text = '5', font = font, width = 3,
    command = lambda: addNumber('5')).grid(row = 4, column = 1, sticky = 'ew')
# 6
tk.Button(root, text = '6', font = font, width = 3,
    command = lambda: addNumber('6')).grid(row = 4, column = 2, sticky = 'ew')
# -
tk.Button(root, text = '-', font = font, width = 3,
    command = lambda: addOperator('-')).grid(row = 4, column = 3, sticky = 'ew')

# row 3
# 1
tk.Button(root, text = '1', font = font, width = 3,
    command = lambda: addNumber('1')).grid(row = 5, column = 0, sticky = 'ew')
# 2
tk.Button(root, text = '2', font = font, width = 3,
    command = lambda: addNumber('2')).grid(row = 5, column = 1, sticky = 'ew')
# 3
tk.Button(root, text = '3', font = font, width = 3,
    command = lambda: addNumber('3')).grid(row = 5, column = 2, sticky = 'ew')
# +
tk.Button(root, text = '+', font = font, width = 3,
    command = lambda: addOperator('+')).grid(row = 5, column = 3, sticky = 'ew')

# row 4
# 0
tk.Button(root, text = '0', font = font, width = 3,
    command = lambda: addNumber('0')).grid(row = 6, column = 0, sticky = 'ew')
# .
tk.Button(root, text = '.', font = font, width = 3,
    command = lambda: addPoint()).grid(row = 6, column = 1, sticky = 'ew')
# %
tk.Button(root, text = '%', font = font, width = 3,
    command = lambda: ans.set(float(ans.get()) * 0.01)).grid(row = 6, column = 2, sticky = 'ew')
# =
tk.Button(root, text = '=', font = font, width = 3,
    command = calculate).grid(row = 6, column = 3, sticky = 'ew')
########################################
# 按鍵偵測

for key in range(10):
    root.bind('<Key-{}>'.format(key), lambda event: addNumber(event.char))
root.bind('<Key-AC>', lambda event: addPoint())

for key in ['Execute', 'Insert', 'Print', 'Help']:
    root.bind('<Key-{}>'.format(key), lambda event: addOperator(event.char))
root.bind('<Key-BackSpace>', lambda event: ans.set(ans.get()[:-1]))
root.bind('<Return>', lambda event: calculate())

root.mainloop()