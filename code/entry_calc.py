from tkinter import *
from tkinter.font import Font

root = Tk()

###################### Window Setting ######################
root.title('calcuration')
root.geometry('400x600')            # 預設的大小
root.minsize(width=400, height=600) # 視窗最小值
root.maxsize(width=400, height=600) # 視窗最大值
root.resizable(False, False)        # 是否可縮放

root.attributes('-alpha', 0.9)      # 透明度
root.attributes('-topmost', True)   # 置頂

########################### font ###########################
textStyle = Font(family='微軟正黑體', size=20)


ans = DoubleVar(value=0)

def compute(*args):
    formula = formulaEnt.get()
    formula.replace('^', '**')
    ans.set(eval(formula))
    formula.delete(0, -1)

Label(root, text='Input', font=textStyle).pack()

formulaEnt = Entry(root, font=textStyle)
formulaEnt.pack()

comBtn = Button(root, text='Compute', font=textStyle, command=compute)
comBtn.pack()


ansLab = Label(root, textvariable=ans)
ansLab.config(font=textStyle, height=2)
ansLab.pack()

root.bind('<Return>', compute)
root.mainloop()