import tkinter as tk
import datetime
from pygame import mixer

root = tk.Tk()
mixer.init()
lugu = "Morning-Routine-Lofi-Study-Music(chosic.com).mp3"

#Muusika loop
def play():
    mixer.music.load(lugu)
    mixer.music.play(loops=-1)

#kella definitsioon
def update_time():
    global current_time
    current_time = datetime.datetime.now()
    clock_label.config(text=current_time.strftime('%d-%m-%y %H:%M:%S'), font=("Arial",50))
    root.after(1000, update_time)

    print(current_time)

#kuvab aega
clock_label = tk.Label(root)
clock_label.pack()


#aja uuendamise käivitamine
update_time()

pandud_label = tk.Label(root, text="Kell äratab: ", font=("Arial", 25))
pandud_label.pack()

#pandud aja kuvamine
aratuse_label = tk.Label(root)
aratuse_label.pack()


uus_kuuüäev_label = tk.Label(root, text="Uus kuupäev(dd:mm:yy): ", font=("Arial", 25))
uus_kuuüäev_label.pack()

#kuupäeva paneku text box
kuupäeva_panek = tk.Entry(root, font=("Arial", 50))
kuupäeva_panek.insert(0, current_time.strftime('%d-%m-%y'))
kuupäeva_panek.pack()

uus_kell_label = tk.Label(root, text="Uus kell(hh:mm:ss): ", font=("Arial", 25))
uus_kell_label.pack()

#kella paneku text box
kella_panek = tk.Entry(root, font=("Arial", 50))
kella_panek.insert(0, current_time.strftime('%H:%M:%S'))
kella_panek.pack()


#äratuskella default value
aratuse_aeg = current_time
aratuse_label.config(text=aratuse_aeg.strftime('%d-%m-%y %H:%M:%S'), font=("Arial", 50))


#siin vahetatakse äratuse aega
def maara_aeg():
    global aratuse_aeg
    aratuse_kell = kella_panek.get()
    aratuse_kuupäev = kuupäeva_panek.get()
    print(aratuse_kuupäev+" "+aratuse_kell)
    aratuse_aeg = datetime.datetime.strptime(aratuse_kuupäev+" "+aratuse_kell, '%d-%m-%y %H:%M:%S')
    #aratuse_aeg = datetime.datetime.strptime(aratuse_tekst, '%d-%m-%y %H:%M:%S')
    aratuse_label.config(text=aratuse_aeg.strftime('%d-%m-%y %H:%M:%S'), font=("Arial", 50))



#nupp, millega panna uus aeg sisse
check = tk.Button(root, text="pane aeg", font=("Arial", 16), command = maara_aeg)
check.pack()


#siin kontrollitakse, kas on äratus või mitte
def aratus_kontroll():
    if current_time == aratuse_aeg:
            aratus_label.config(text=f"{lugu}", font=("Arial",50))
            print("Music starting")
            play()
    else:      
        aratus_label.config(text="maga maga", font=("Arial",50))
        print("Stop1")
        mixer.music.stop()
    root.after(1000, aratus_kontroll())

#Label kus kuvab, kas äratus, või mitte
aratus_label = tk.Label(root, text="maga maga", font=("Arial", 50))
aratus_label.pack()

#äratuse kontrollimse käivitamine
aratus_kontroll()

root.mainloop()
