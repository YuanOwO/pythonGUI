import tkinter as tk
import tkinter.font as font
import datetime
import asyncio

async def update():
    global now_Str
    while True:
        now = datetime.datetime.now()
        date = now.strftime('%Y 年 %m 月 %d 日')
        week = ['一','二', '三', '四', '五', '六', '日'][now.weekday()]
        time = now.strftime('%H 時 %M 分 %S 秒')
        now_Str.set('{} ({})\n{}'.format(date, week, time))
        await asyncio.sleep(1)

# def update():
#     global now_Str
#     now = datetime.datetime.now()
#     date = now.strftime('%Y 年 %m 月 %d 日')
#     week = ['一','二', '三', '四', '五', '六', '日'][now.weekday()]
#     time = now.strftime('%H 時 %M 分 %S 秒')
#     now_Str.set('{} ({})\n{}'.format(date, week, time))

root = tk.Tk()
root.title('Clock')
root.geometry('720x640')

# Font config
textStyle = font.Font(family = '微軟正黑體', size = 20)

tk.Label(root, text = '現在時間', font = textStyle).pack()
now_Str = tk.StringVar()
tk.Label(root, textvariable = now_Str, font = textStyle).pack()

asyncio.run(update())
tk.Button(root, text = '更新時間', font = textStyle, command = update).pack()


root.mainloop()