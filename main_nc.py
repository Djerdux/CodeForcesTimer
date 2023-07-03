from get_contest import *
import tkinter as tk
import time
from os import system

name, re_time = get_contest()
nick, rg = get_rank()

W, H = 400, 100

def open_site():
    system('start https://codeforces.com')


def update_time():
    global re_time
    global t
    lable.config(
        text=f"{nick}:{rg}\n"+f"{name}\n{time.strftime(f'{abs(re_time) // 60 // 60 // 24}'+':%H:%M:%S', time.gmtime(abs(re_time)))}",
    )
    # coords = c.bbox(t)
    # c.delete(t)
    # tw = coords[2] - coords[0]
    # th = coords[3] - coords[1]
    # print(tw/2, th/2)
    # t = c.create_text(126, 31.5, font=("JetBrains Mono", 12),text=f"{nick}:{rg}\n"+f"{name}\n{time.strftime(f'{abs(re_time) // 60 // 60 // 24}'+':%H:%M:%S', time.gmtime(abs(re_time)))}")
    re_time -= 1
    root.after(1000, update_time)




root = tk.Tk()
# c = tk.Canvas(height=H)
# c.pack()


# t = c.create_text(126, 31.5, font=("Consolas", 16), text=f"{name}\n{time.strftime(f'{abs(re_time) // 60 // 60 // 24}'+':%H:%M:%S', time.gmtime(abs(re_time)))}", fill="Black")
lable = tk.Label(
    font=("Fixedsys", 16),
    text=f"{nick}:{rg}\n"+f"{name}\n{time.strftime(f'{abs(re_time) // 60 // 60 // 24}'+':%H:%M:%S', time.gmtime(abs(re_time)))}",
    justify='left'
)
btn = tk.Button(
    text="Перейти", 
    command=open_site,
)
lable.pack()

btn.pack(side='left')

update_time()

root.mainloop()