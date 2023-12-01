import tkinter as tk
import random

def matemaatika():
    root2 = tk.Tk()

    def disable_event():
        pass

    root2.protocol("WM_DELETE_WINDOW", disable_event)

    with open("matemaatika.txt") as f:
        lines = f.readlines()
        if lines:
            ülesanded = (random.choices(lines, k = random.randint(3,5)))

    for ülesanne in ülesanded:
        print(ülesanne)
        #leiab vastuse ja ülesande
        ülesanne_l = ülesanne.split("= ")

        ülesande_label = tk.Label(root2, text=ülesanne_l[0], font=("Arial",50))
        ülesande_label.pack()

        vastuse_panek = tk.Entry(root2, font=("Arial",50))
        vastuse_panek.pack()

        result_variable = tk.BooleanVar()


    def kontrolli_vastust():
        global ülesanded
        sisestatud = vastuse_panek.get()
        if sisestatud == ülesanne_l[1].strip():
            result_variable.set(True)
            root2.quit()
            root2.destroy()
        else:
            matemaatika()
            


    submit = tk.Button(root2, text="submit", command=kontrolli_vastust, font=("Arial",50))
    submit.pack()


    root2.mainloop()


    return result_variable.get()
