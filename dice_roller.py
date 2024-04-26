import tkinter as tk
import random

class DiceRoller:
    def __init__(self, master):
        self.master = master
        master.title("Кости")

        self.label = tk.Label(master, text="бросим кубик?", font=("Helvetica", 100))
        self.label.pack(pady=50)

        label = tk.Label(master, text="сколько раз?", font=("Helvetica", 24))
        label.pack()

        entry = tk.Entry(master)
        entry.pack()

        button = tk.Button(master, text="ввод", command=self.entered_value)
        button.pack()

        self.roll_button = tk.Button(master, text="Бросить", font=("Helvetica", 24), command=self.roll_dice)
        self.roll_button.pack()
        
    def entered_value(self):
        value = entry.get()
        print("введено :", value) #для проверки

    def roll_dice(self):
        dice_value = random.randint(1, 6)
        self.label.config(text=str(dice_value))
        
root = tk.Tk()
dice_roller = DiceRoller(root)
root.mainloop()