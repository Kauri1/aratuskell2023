import tkinter as tk
import random

def typing():
    root2 = tk.Tk()
    root2.geometry('700x400')
    
    result_variable = tk.BooleanVar()

    pealkiri_label = tk.Label(root2, text="Kirjuta sõnu kiirusega", font=("Arial", 25))
    pealkiri_label.pack()

    with open("typetest.txt", encoding="UTF-8") as f:
        lines = f.readlines()
        if lines:
            algne_tekst = random.choice(lines).strip()


    def key_pressed(event):
        tekst = tekst_label['text']
        tekst2 = tekst2_label['text']
        key = event.char
        print(key)
        if key != "":
            if tekst[0] == key:
                tekst2+=tekst[0]
                tekst_label.config(text=tekst[1:])
                tekst2_label.config(text=tekst2)
                if len(tekst) == 1:
                    result_variable.set(True)
                    root2.quit()
                    root2.destroy()
            #kui failib
            else:
                tekst_label.config(text=algne_tekst)
                tekst2_label.config(text="")
        


#    tekst2_label = tk.Label(root2, text="", font=("Arial", 25), wraplength=1000, fg="green", justify="left")
#    tekst2_label.pack(side=tk.TOP, anchor='nw')
#
#    tekst_label = tk.Label(root2, text=algne_tekst, font=("Arial", 25), wraplength=1000, justify="left")
#    tekst_label.pack(side=tk.TOP, anchor='nw')

    tekst2_label = tk.Label(root2, text="", font=("Arial", 25), fg="green")
    tekst2_label.place(relx=0.5, rely=0.5, anchor=tk.E)


    tekst_label = tk.Label(root2, text=algne_tekst, font=("Arial", 25))
    tekst_label.place(relx=0.5, rely=0.5, anchor=tk.W)



    root2.bind("<KeyPress>",key_pressed)



    root2.mainloop()

    return result_variable.get()
typing()