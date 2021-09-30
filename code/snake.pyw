import tkinter as tk
from tkinter import messagebox as msgbox
from random import choice, randint

####################################################################################################
# 重置遊戲
def restart(event):
    global score, high, speed, isGodMode
    
    score = 0
    speed = 0.25 if isGodMode.get() else 1
    root.unbind('<Return>')
    text.set('Score: 0\nHigh: {}'.format(high))
    create_snake()
    create_food()
    rendering()
    root.after(1000, move)

# 生成 snake
def create_snake():
    global snake, face, size
    face  = choice(['Up', 'Down', 'Left', 'Right'])
    snake = [(randint(1, size[0] - 1), randint(1, size[1] - 1))]
    for i in [0, 1]:
        snake.append({
            'Left':  (snake[i][0] + 1, snake[i][1]),
            'Right': (snake[i][0] - 1, snake[i][1]),
            'Up':    (snake[i][0], snake[i][1] + 1),
            'Down':  (snake[i][0], snake[i][1] - 1)
        }.get(face))

# 生成 food
def create_food():
    global food
    i    = 0 if snake[0] else 1
    food = (choice((list(range(1, snake[ i][0])) + list(range(snake[-1][0] + 1, size[0] + 1))) if snake[i][0] < snake[-1][0] else
                   (list(range(1, snake[-1][0])) + list(range(snake[ i][0] + 1, size[0] + 1)))),
            choice((list(range(1, snake[ i][1])) + list(range(snake[-1][1] + 1, size[1] + 1))) if snake[i][1] < snake[-1][1] else
                   (list(range(1, snake[-1][1])) + list(range(snake[ i][1] + 1, size[1] + 1)))))

# 蛇移動
def move():
    global score, high, speed, snake, food, isGodMode
    
    speed = 0.25 if isGodMode.get() else 0.75 ** (score // 5)
    if snake[0]:
        snake.insert(0, None)
        snake.pop(-1)
    snake[0] = {
        'Left':  (snake[1][0] - 1, snake[1][1]),
        'Right': (snake[1][0] + 1, snake[1][1]),
        'Up':    (snake[1][0], snake[1][1] - 1),
        'Down':  (snake[1][0], snake[1][1] + 1)
    }.get(face)
    
    # 結束偵測
    x, y = snake[0][0], snake[0][1]
    if (snake[0] in snake[1:-1]) \
        or (x <= 0 or x > size[0]) or (y <= 0 or y > size[1]):
        # 遊戲結束
        msgbox.showinfo(
            title   = '遊戲結束',
            message = '遊戲結束!\n按 Enter 重新開始'
        )
        root.bind('<Return>', restart)
    else:
        # 繼續進行
        rendering()
        if snake[0] == food:
            # 接觸到 food
            score += 1
            high   = max(high, score)
            if score & 1:
                snake.insert(0, None)
            create_food()
            text.set('Score: {}\nHigh: {}'.format(score, high))
        root.after(int(speed * 1000), move)

# 繪製圖塊
def rendering():
    global cv
    
    cv.delete('all')
    width  = cv.winfo_width()  // size[0]
    height = cv.winfo_height() // size[1]
    for i in [0]:
        x = food[0] * width
        y = food[1] * height
        cv.create_rectangle(x - width, y - height, x, y, fill = 'red')
    for i in range(len(snake)):
        x = snake[i][0] * width
        y = snake[i][1] * height
        cv.create_rectangle(x - width, y - height, x, y, fill = 'yellow')

# 轉彎
def turn(event):
    global face
    face = event.keysym # keysym 按鍵名稱


# 遊戲設定
def setting():
    msgbox.showwarning(
        title = '遊戲設定',
        message = 'Coming Soon.\n(Maybe...)'
    )

####################################################################################################
root = tk.Tk()
root.title('貪食蛇')

# 遊戲參數 初始化
size = (20, 20) # (x, y)
speed = 1
isGodMode = tk.BooleanVar(value = False)
score, high = 0, 0
snake, face = 0, 0
create_snake()
create_food()

# Menu
mainMenu    = tk.Menu(root)
settingMenu = tk.Menu(mainMenu, tearoff = 0)
root.config(menu = mainMenu)
settingMenu.add_command(label = '遊戲設置',  command = setting)
settingMenu.add_command(label = 'God Mode', command = lambda: isGodMode.set(not isGodMode.get()))
mainMenu.add_cascade(label = '設定', menu = settingMenu)
mainMenu.add_command(label = '說明', command = lambda: msgbox.showinfo(title = '遊戲說明', message = '就是貪食蛇。'))
mainMenu.add_command(label = '離開', command = root.quit)

# 遊戲資訊
text = tk.StringVar(value = 'Score: 0\nHigh: 0')
tk.Label(root, textvariable = text, height = 2, font = ('微軟正黑體', 16)).pack()
# 遊戲畫面
cv = tk.Canvas(bg = 'black', width = 400, height = 400, highlightthickness = 0)
cv.pack()

# 按鍵偵測
root.bind('<Key-g>', lambda event: isGodMode.set(not isGodMode.get()))
root.bind('<Key-Left>',  turn)
root.bind('<Key-Right>', turn)
root.bind('<Key-Up>',    turn)
root.bind('<Key-Down>',  turn)

rendering()
root.after(1000, move)
root.mainloop()