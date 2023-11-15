import tkinter as tk
import random

def matemaatika():
    root2 = tk.Tk()

    with open("matemaatika.txt") as f:
        
        ülesanne = next(f)
        for num, aline in enumerate(f, 2):
            if random.randrange(num):
                continue
            ülesanne = aline

    ülesanne_l = ülesanne.split("= ")

    ülesande_label = tk.Label(root2, text=ülesanne_l[0], font=("Arial",50))
    ülesande_label.pack()

    vastuse_panek = tk.Entry(root2, font=("Arial",50))
    vastuse_panek.pack()

    result_variable = tk.BooleanVar()

    def kontrolli_vastust():
        sisestatud = vastuse_panek.get()
        if sisestatud == ülesanne_l[1].strip():
            result_variable.set(True)
            root2.quit()
            root2.destroy()
            


    submit = tk.Button(root2, text="submit", command=kontrolli_vastust, font=("Arial",50))
    submit.pack()


    root2.mainloop()


    return result_variable.get()