import tkinter as tk
import datetime
import winsound

root = tk.Tk()

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
    aratuse_label.config(text=aratuse_aeg.strftime('%d-%m-%y %H:%M:%S'), font=("Arial", 50))



#nupp, millega panna uus aeg sisse
check = tk.Button(root, text="pane aeg", font=("Arial", 16), command = maara_aeg)
check.pack()

# Kas on heli muutuja
issound = False

#siin kontrollitakse, kas on äratus või mitte
def aratus_kontroll():
    global issound
    if current_time > aratuse_aeg:
        aratus_label.config(text="ääärraaatuuuss", font=("Arial",50))
        print("ääratuus")
        #Kui pole heli, siis mängi heli
        if issound == False:
            winsound.PlaySound("helid/Morning-Routine-Lofi-Study-Music(chosic.com).wav", winsound.SND_LOOP | winsound.SND_ASYNC)
            issound = True
    else:
        aratus_label.config(text="maga maga", font=("Arial",50))
        #jätab paneb heli None
        winsound.PlaySound(None , winsound.SND_ASYNC)
        issound = False
    root.after(1000, aratus_kontroll)

#Label kus kuvab, kas äratus, või mitte
aratus_label = tk.Label(root, text="maga maga", font=("Arial", 50))
aratus_label.pack()

#äratuse kontrollimse käivitamine
aratus_kontroll()

root.mainloop()