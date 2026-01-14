from logging import disable
from tkinter.ttk import *
from tkinter import *
import random
from ttkthemes import ThemedTk

window = ThemedTk(theme='breeze')
window.configure(themebg='breeze', bg='#136F63')
window.title('Guess the number Python Project Created by JP')
window.geometry('420x380')
window.resizable(False, False)

upar = PhotoImage(file='up_ar.png')
downar = PhotoImage(file='down_ar.png')
dice = PhotoImage(file='dice.png')
correct = PhotoImage(file='correct.png')

diff = IntVar()
diff.set(2)  # default medium

secret_number = IntVar()
tries = IntVar()
tries.set(0)

def randomize_number():
    if diff.get() == 1:
        secret_number.set(random.randint(1, 50))
    elif diff.get() == 2:
        secret_number.set(random.randint(1, 100))
    elif diff.get() == 3:
        secret_number.set(random.randint(1, 200))

    tries.set(0)
    tries_label.config(text="Tries: 0")
    result_label.config(text=".", image=dice, compound="top")
    window.after(400, lambda: result_label.config(text="..", image=dice, compound="top"))
    window.after(800, lambda: result_label.config(text="...", image=dice, compound="top"))
    window.after(1200, lambda: result_label.config(text="....", image=dice, compound="top"))
    window.after(1200, lambda: result_label.config(text="New number created!", image=dice, compound="top"))
    txt.config(state="normal")
    txt.delete(0, END)


easy = Radiobutton(window, text='Easy (0-50)', value=1, variable=diff,
                   bg="#136F63", fg="#A2A79E")
easy.grid(column=0, row=2, pady=10)

medium = Radiobutton(window, text='Medium (0-100)', value=2, variable=diff,
                     bg="#136F63", fg="#A2A79E")
medium.grid(column=1, row=2, pady=10)

hard = Radiobutton(window, text='Hard (0-200)', value=3, variable=diff,
                   bg="#136F63", fg="#A2A79E")
hard.grid(column=2, row=2, pady=10)

Label(window, text='Guess the number', bg='#136F63', fg='#FC7753',
      font=('Helvetica', 18)).grid(column=1, row=0)

Label(window, text='Try to find the secret number!', font=('Helvetica'),
      bg='#136F63', fg='#A2A79E').grid(column=1, row=5)

result_label = Label(window, text="Let's start!", image=dice, bg="#136F63",
                     fg="#A2A79E", font=('Helvetica', 14), compound="top")
result_label.grid(column=1, row=8, pady=10)

tries_label = Label(window, text="Tries: 0", bg="#136F63",
                    fg="#A2A79E", font=('Helvetica', 14))
tries_label.grid(column=1, row=7)

credits_label = Label( window, text='Created by JP',bg="#136F63",fg="#A2A79E", font=('Helvetica'))
credits_label.grid(column=1, row=12, pady=20)


def check_guess(event=None):
    try:
        guess = int(txt.get())
    except:
        result_label.config(text="Enter a valid number!", image=dice, compound="top")
        txt.delete(0, END)
        return

    tries.set(tries.get() + 1)
    tries_label.config(text=f"Tries: {tries.get()}")

    target = secret_number.get()

    if guess < target:
        result_label.config(text="Higher!", image=upar, compound="top")
    elif guess > target:
        result_label.config(text="Lower!", image=downar, compound="top")
    else:
        result_label.config(text=f"Correct! Tries: {tries.get()}",
                            image=correct, compound="top")
        txt.config(state="disabled")

    txt.delete(0, END)


txt = Entry(window, font=('Helvetica'), state='disabled',justify="center")
txt.grid(column=1, row=9, pady=2)
txt.bind("<Return>", check_guess)


btn_exit = Button(window, text='Exit', width=10, font=('Helvetica', 10),
                  bg="#FC7753", fg="#A2A79E", command=window.destroy)
btn_exit.grid(column=2, row=8)

btn_rand = Button(window, text='Randomize', width=10, font=('Helvetica', 10),
                  bg="#FC7753", fg="#A2A79E", command=randomize_number)
btn_rand.grid(column=2, row=9, pady=2)

window.mainloop()

