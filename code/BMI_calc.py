import tkinter as tk
from tkinter.font import Font

# 計算 BMI 值
def BMI_calc():
    global result
    try:
        height = float(heightEntry.get())
        weight = float(weightEntry.get())
        bmi = round((weight / (height * 0.01) ** 2) * 100) / 100
        result.set('你的 BMI 是 {}, {}'.format(bmi, BMI_desc(bmi)))
    except ZeroDivisionError:
        result.set('身高不可為零')
    except Exception as e:
        result.set('發深了未知的錯誤:\n{}'.format(e.args))

def BMI_desc(value):
    if value < 18.5:
        return '體重過輕'
    if value < 24:
        return '體重適中'
    return '體重過重'

########### 初始化設定  ###########
root = tk.Tk()
root.title('BMI Calc')

# 字型設定
font = Font(family = '微軟正黑體', size = 20)

# 標題
tk.Label(root, text = 'BMI 計算機', font = font).pack()

###################################
# 身高欄位
heightFrame = tk.Frame(root)
heightFrame.pack()
heightLabel = tk.Label(heightFrame, text = '身高\n(cm)', font = font)
heightEntry = tk.Entry(heightFrame, font = font)
heightLabel.pack(side = tk.LEFT)
heightEntry.pack(side = tk.RIGHT)

# 體重欄位
weightFrame = tk.Frame(root)
weightFrame.pack()
weightLabel = tk.Label(weightFrame, text = '體重\n(kg)', font = font)
weightEntry = tk.Entry(weightFrame, font = font)
weightLabel.pack(side = tk.LEFT)
weightEntry.pack(side = tk.RIGHT)

result = tk.StringVar(root)
result.set('')
# 計算結果
tk.Label(root, textvariable = result, font = font).pack()


calcBtn = tk.Button(root, text = '馬上試算!!', command = BMI_calc, font = font)
calcBtn.pack()

############ 字體大小 ############
# 變大
def fontSizeIncrease():
    font['size'] += 2
# 變小
def fontSizeDecrease():
    font['size'] -= 2

fontConfigFrame = tk.Frame(root, padx = font['size'], pady = font['size'])
fontConfigFrame.pack()
fontSizeIncreaseBtn = tk.Button(fontConfigFrame, text = '字體放大', command = fontSizeIncrease, font = font)
fontSizeIncreaseBtn.pack(side = tk.LEFT)
fontSizeDecreaseBtn = tk.Button(fontConfigFrame, text = '字體縮小', command = fontSizeDecrease, font = font)
fontSizeDecreaseBtn.pack(side = tk.RIGHT)


root.mainloop()