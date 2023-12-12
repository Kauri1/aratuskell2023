import tkinter as tk
import random

def typing():
    root2 = tk.Tk()
    root2.geometry('1000x600')
    
#    root2.after(10000, )

    global aeg
    aeg = 0

    def uuenda_aega():
        global aeg
        aeg += 0.1
        aeg_label.config(text=round(aeg, 1))
        wpm_label.config(text=str(round(tähti_kirjutatud/aeg, 2))+ "Tähte sekundis")
        root2.after(100, uuenda_aega)
    
    global tähti_kirjutatud
#(tähti_kirjutatud+1)/aeg, tähti_kirjutatud+1, aeg)
    tähti_kirjutatud = 0
    

    def key_pressed(event):
        global tähti_kirjutatud, aeg
        tekst = algne_tekst
        key = event.char
        print(key)
        täht_label.config(text=tekst[tähti_kirjutatud])
        if key != "":
            if tekst[tähti_kirjutatud] == key:
                täht_label.config(text=tekst[tähti_kirjutatud+1])
                tekst_vasak_label.config(text=tekst[:tähti_kirjutatud+1])
                tähti_kirjutatud += 1
                print(tähti_kirjutatud)
                #kui tekst saab otsa
                if len(tekst) == 1:
                    result_variable.set(True)
                    root2.quit()
                    root2.destroy()
            #kui failib
            else:
                tekst_parem_label.config(text=algne_tekst)
                tekst_vasak_label.config(text="")
                tähti_kirjutatud = 0
                aeg = 0
    
    
    with open("typetest.txt", encoding="UTF-8") as f:
        lines = f.readlines()
        if lines:
            algne_tekst = random.choice(lines).strip()


    result_variable = tk.BooleanVar()

    pealkiri_label = tk.Label(root2, text="Kirjuta sõnu kiirusega", font=("Arial", 25))
    pealkiri_label.pack()


        


#    tekst_vasak_label = tk.Label(root2, text="", font=("Arial", 25), wraplength=1000, fg="green", justify="left")
#    tekst_vasak_label.pack(side=tk.TOP, anchor='nw')
#
#    tekst_parem_label = tk.Label(root2, text=algne_tekst, font=("Arial", 25), wraplength=1000, justify="left")
#    tekst_parem_label.pack(side=tk.TOP, anchor='nw')
#


#    tekst_parem_label = tk.Label(root2, text=algne_tekst, font=("Arial", 25), wraplength=1000, justify="left")
#    tekst_parem_label.place(relx=0.5, rely=0.5, anchor=tk.NW)

    tekst_parem_label = tk.Label(root2, text=algne_tekst, font=("consolas 30"), wraplength=1000, justify="left")
    tekst_parem_label.place(relx=0, rely=0.3, anchor=tk.NW)

    tekst_vasak_label = tk.Label(root2, text="", font=("consolas 30"), wraplength=1000, fg="green", justify="left")
    tekst_vasak_label.place(relx=0, rely=0.3, anchor=tk.NW)

    aeg_label = tk.Label(root2, font=("Arial", 25))
    aeg_label.place(relx=0.4, rely=0.2, anchor=tk.E)

    #näitab kirjutamise kiirust
    wpm_label = tk.Label(root2, font=("Arial", 25))
    wpm_label.place(relx=0.6, rely=0.2, anchor=tk.W)

    #vasakule kalduv tekst
#    tekst_vasak_label = tk.Label(root2, text="", font=("Arial", 25), fg="green", bg="lightgray")
#    tekst_vasak_label.place(relx=0.5, rely=0.5, anchor=tk.E)
#
#
#    tekst_parem_label = tk.Label(root2, text=algne_tekst, font=("Arial", 25))
#    tekst_parem_label.place(relx=0.5, rely=0.5, anchor=tk.W)
#
    täht_label = tk.Label(root2, text=algne_tekst[0], font=("Arial", 25))
    täht_label.place(relx=0.5, rely=0.8, anchor=tk.N)

    root2.bind("<KeyPress>",key_pressed)

    uuenda_aega()

    root2.mainloop()

    return result_variable.get()
typing()