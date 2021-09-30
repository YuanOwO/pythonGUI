# setting.py

import tkinter as tk

root = tk.Tk()

root.title("Hello") # 標題
# Tk.title(text: str)
# 視窗的標題

root.geometry("640x480")
# Tk.geometry("WxH+X+Y")
# 寬度 W, 高度 H, 視窗左上角座標為 (X, Y); 螢幕左上角座標為 (0, 0)

root.maxsize(1280, 720)
# Tk.maxsize(width: int, height: int)
# 視窗大小的最大值

root.minsize(480, 360)
# Tk.minsize(width: int, height: int)
# 視窗大小的最小值

# root.resizable(TR)

lab = tk.Label(root, text = "Hello World")
lab.pack()

root.mainloop() # Call the mainloop of root.