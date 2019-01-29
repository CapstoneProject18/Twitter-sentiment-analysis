import tkinter as tk

import random
guessesTaken = 0
number = random.randint(1,20)

def check():
    while guessesTaken < 6:
        guess = int(txt_guess.get())

        if guess < number:
             msg = ('Your guess is too low.')
        elif guess > number:
             msg = ('Your guess is too high.')
        elif guess == number:
            msg = ('Good job!')

    lbl_result["text"] = msg

root = tk.Tk()


lbl_title = tk.Label(root,text="Welcome to the Guessing Game! I am thinking of a number between 1 and 100.")

lbl_title.pack()


lbl_result = tk.Label(root,text="Good luck!")

lbl_result.pack()

btn_check = tk.Button(root,text="Check", fg = "blue", command = check)
btn_check.pack(side = "left")

btn_reset = tk.Button(root,text="Reset", fg = "red", command = root.quit())
btn_reset.pack(side = "right")

txt_guess = tk.Entry(root, width = 10)

txt_guess.pack()

root.mainloop()



