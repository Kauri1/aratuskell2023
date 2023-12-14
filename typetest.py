import tkinter as tk
import random

def typing(kiirus1):

    try:
        kiirus1 = float(kiirus1)
    except:
        kiirus1 = 200

    global kiirus
    kiirus = kiirus1

    root2 = tk.Tk()
    root2.geometry('900x500')
    

    global aeg
    aeg = 0

    def uuenda_aega():
        global aeg, tähti_kirjutatud, kiirus
        aeg += 0.1
        cpm = round(tähti_kirjutatud/aeg*60, 2)
        aeg_label.config(text=round(aeg, 1))
        wpm_label.config(text=str(cpm)+ "Tähte minutis")
        if aeg > 30 and cpm >= kiirus:
            result_variable.set(True)
            root2.quit()
            root2.destroy()
        elif aeg > 30 and cpm < kiirus:
            tekst_parem_label.config(text=algne_tekst)
            tekst_vasak_label.config(text="")
            tähti_kirjutatud = 0
            aeg = 0
            kiirus *= 0.8
            kiirus_label.config(text=kiirus)
        root2.after(100, uuenda_aega)
    
    global tähti_kirjutatud
#(tähti_kirjutatud+1)/aeg, tähti_kirjutatud+1, aeg)
    tähti_kirjutatud = 0
    
    global failid
    failid = 0

    def key_pressed(event):
        global tähti_kirjutatud, aeg, failid
        tekst = tekst_parem_label['text']
        tekst2 = tekst_vasak_label['text']
        key = event.char
        print(key)
        täht_label.config(text=tekst[0])
        if key != "":
            if tekst[0] == key:
                täht_label.config(text=tekst[1])
                tekst2+=tekst[0]
                tekst_parem_label.config(text=tekst[1:])
                tekst_vasak_label.config(text=tekst2)
                tähti_kirjutatud += 1
                #kui tekst saab otsa
                if len(tekst) == 1:
                    result_variable.set(True)
                    root2.quit()
                    root2.destroy()
            #kui failib
            else:
                failid += 1
                if failid > 5:
                    tekst_parem_label.config(text=algne_tekst)
                    tekst_vasak_label.config(text="")
                    tähti_kirjutatud = 0
                    aeg = 0
                    failid = 0
    
    
    with open("typetest.txt", encoding="UTF-8") as f:
        lines = f.readlines()
        if lines:
            algne_tekst = random.choice(lines).strip()


    result_variable = tk.BooleanVar()

    pealkiri_label = tk.Label(root2, text="Kirjuta sõnu kiirusega", font=("Arial", 25))
    pealkiri_label.pack()

    kiirus_label = tk.Label(root2, text=kiirus, font=("consolas 30"))
    kiirus_label.pack()

    aeg_label = tk.Label(root2, font=("consolas 30"))
    aeg_label.place(relx=0.4, rely=0.3, anchor=tk.E)

    #näitab kirjutamise kiirust
    wpm_label = tk.Label(root2, font=("consolas 30"))
    wpm_label.place(relx=0.6, rely=0.3, anchor=tk.W)



    #vasakule kalduv tekst
    tekst_vasak_label = tk.Label(root2, text="", font=("consolas 30"), fg="green", bg="lightgray")
    tekst_vasak_label.place(relx=0.3, rely=0.5, anchor=tk.NE)


    tekst_parem_label = tk.Label(root2, text=algne_tekst, font=("consolas 30"), wraplength="600", justify="left")
    tekst_parem_label.place(relx=0.3, rely=0.5, anchor=tk.NW)

    täht_label = tk.Label(root2, text=algne_tekst[0], font=("consolas 30"))
    täht_label.place(relx=0.2, rely=0.7, anchor=tk.N)

    root2.bind("<KeyPress>",key_pressed)

    uuenda_aega()

    root2.mainloop()

    return result_variable.get()