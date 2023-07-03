from get_contest import *
import tkinter as tk
import time
import win10toast
from os import system

# init varibles
name, re_time = get_contest()
nick, rg = get_rank()
W, H = 400, 100
times = (3*3600, 3600, 600, 120)


def open_site():
    system('start https://codeforces.com')


def update_time():
    global re_time
    global t
    lable.config(
        text=f"{nick}:{rg}\n"+f"{name}\n{time.strftime(f'{abs(re_time) // 60 // 60 // 24}'+':%H:%M:%S', time.gmtime(abs(re_time)))}",
    )
    re_time -= 1

    if abs(re_time) in times:
        if (abs(re_time)) >= 3600:
            win10toast.ToastNotifier().show_toast("Time", f"remainig {abs(re_time) // 3600} hours", duration=4, threaded=True)
        else:
            win10toast.ToastNotifier().show_toast("Time", f"remainig {abs(re_time) // 60} minutes", duration=4, threaded=True)
        

    root.after(1000, update_time)




root = tk.Tk()
root.iconbitmap('favicon.ico')
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