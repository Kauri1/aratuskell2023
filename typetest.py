import tkinter as tk


def typing():
    root2 = tk.Tk()

    
    result_variable = tk.BooleanVar()

    pealkiri_label = tk.Label(root2, text="Kirjuta sõnu kiirusega", font=("Arial", 25))
    pealkiri_label.pack()

    algne_tekst = "Siin on tekst mida testin"

    key_pressed_variable = tk.BooleanVar()

    def key_pressed(event):
        tekst = tekst_label['text']
        key = event.char
        if key_pressed_variable.get() == False:
            print(key)
            if key != "":
                if tekst[0] == key:
                    tekst_label.config(text=tekst[1:])
                    if len(tekst) == 1:
                        result_variable.set(True)
                        root2.quit()
                        root2.destroy()
                else:
                    tekst_label.config(text=algne_tekst)

    tekst_label = tk.Label(root2, text=algne_tekst, font=("Arial", 25))
    tekst_label.pack()

    root2.bind("<KeyPress>",key_pressed)
    #root2.bind('<KeyRelease>',key_released)



    root2.mainloop()

    return result_variable.get()
typing()