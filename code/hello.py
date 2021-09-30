from tkinter import *

# 主視窗
root = Tk() # 主視窗

# 文字方塊
lab = Label(root, text = 'Hello World!', bg = '#eeeeee')
lab.pack()
lab2 = Label(root, text = 'This color is Red', fg = 'red')
lab2.pack()
Label(root, text = '預設由上而下且靠左').pack()

root.mainloop()