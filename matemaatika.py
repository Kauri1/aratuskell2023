import tkinter as tk

def matemaatika():
    root = tk.Tk()

    with open("matemaatika.txt") as f:
        ülesanne = f.readline()

    ülesanne_l = ülesanne.split("= ")

    ülesande_label = tk.Label(root, text=ülesanne_l[0], font=("Arial",50))
    ülesande_label.pack()

    vastuse_panek = tk.Entry(root, font=("Arial",50))
    vastuse_panek.pack()

    result_variable = tk.BooleanVar()

    def kontrolli_vastust():
        sisestatud = vastuse_panek.get()
        if sisestatud == ülesanne_l[1].strip():
            result_variable.set(True)
            root.quit()


    submit = tk.Button(root, text="submit", command=kontrolli_vastust, font=("Arial",50))
    submit.pack()


    root.mainloop()


    return result_variable.get()