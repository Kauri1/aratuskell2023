import tkinter as tk
import random

def matemaatika():
    root2 = tk.Tk()

    def disable_event():
        pass

    root2.protocol("WM_DELETE_WINDOW", disable_event)

    #klass, kuna igat ülesannet tuleb kontrollida, klassiga lihtne mitmele ülesandele anda individuaalne isiksus
    class ülesanne:
        ülesanded = []
        def __init__(self, ülesanne):
            self.ülesanne = ülesanne
            self.__class__.ülesanded.append(self)

    #loeb 3-5 ülesannet
    with open("matemaatika.txt", encoding="utf-8") as f:
        lines = f.readlines()
        if lines:
            ülesanded = (random.choices(lines, k = random.randint(3,5)))

    #teeb ülesande objektid
    for ül in ülesanded:
        ül = ül.strip()
        ül_l = ül.split("= ")
        ül = ülesanne(ül_l)

    #sisestus väljade list
    entries = []

    #käib läbi kõik ülesannete objektid
    for ül in ülesanne.ülesanded:
        print(ül.ülesanne)

        ülesande_label = tk.Label(root2, text=ül.ülesanne[0], font=("Arial",50))
        ülesande_label.pack()

        vastuse_panek = tk.Entry(root2, font=("Arial",50))
        vastuse_panek.pack()

        entries.append(vastuse_panek)



    #tagastab lõpus selle
    result_variable = tk.BooleanVar()


    """
    for ülesanne in ülesanded:
        print(ülesanne)
        #leiab vastuse ja ülesande
        ülesanne = ülesanne.strip()
        ülesanne_l = ülesanne.split("= ")

        ülesande_label = tk.Label(root2, text=ülesanne_l[0], font=("Arial",50))
        ülesande_label.pack()

        vastuse_panek = tk.Entry(root2, font=("Arial",50))
        vastuse_panek.pack()

        #tagastab lõpus selle
        result_variable = tk.BooleanVar()
    """ 

    def kontrolli_vastust():
        õigesti = 0
        for entry, ül in zip(entries, ülesanne.ülesanded):

            sisestatud = entry.get()
            vastus = ül.ülesanne[1].strip()
            print(sisestatud, vastus)
            

            if sisestatud == vastus:
                õigesti += 1
        if õigesti == len(entries):
            result_variable.set(True)
            root2.quit()
            root2.destroy()
        else:
            matemaatika()
    


    submit = tk.Button(root2, text="submit", command=kontrolli_vastust, font=("Arial",50))
    submit.pack()


    root2.mainloop()


    return result_variable.get()
