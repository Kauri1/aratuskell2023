import tkinter as tk
import datetime
import winsound

import matemaatika, typetest



#siit algab GUI
root = tk.Tk()


#kella definitsioon
def update_time():
    global current_time , iga_päev_var
    if iga_päev_var.get() == 1:
        current_time = datetime.datetime.now().time()
    else:
        current_time = datetime.datetime.now()
    clock_label.config(text=datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S'), font=("Arial",50))
    root.after(1000, update_time)

    print(current_time)

def iga_päev_switch():
    global aratuse_aeg, läbitud
    maara_aeg()
    root.protocol("WM_DELETE_WINDOW", close_program)
    läbitud = True
    #
    if iga_päev_var.get() == 1:
        kuupäeva_panek["state"] = "disabled"
        try:
            aratuse_aeg = aratuse_aeg.time()
        except:
            pass
    else:
        kuupäeva_panek["state"] = "normal"
    print("switched")
    print(aratuse_aeg)
    

def disable_event():
    pass

def close_program():
    root.destroy()



iga_päev_var = tk.IntVar()


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

#iga päeva vahetamise nupp
iga_päev_checkbox = tk.Checkbutton(root, text='Iga päev?', variable=iga_päev_var, onvalue=1, offvalue=0, command=iga_päev_switch, font=("Arial", 25))
iga_päev_checkbox.pack()

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

#Kumb ülesanne tuleb
def kumb_ülesanne():
    if valik.get() == 2:
        return typetest.typing(kiiruse_valik.get())
    else:
        return matemaatika.matemaatika()

valik = tk.IntVar()

kas_matemaatika = tk.Radiobutton(root, text="Matemaatika", variable=valik, value=1)
kas_matemaatika.pack(anchor=tk.W)
kas_speed = tk.Radiobutton(root, text="Kirjutamine", variable=valik, value=2)
kas_speed.pack(anchor=tk.W)
kiiruse_valik = tk.Entry(root)
kiiruse_valik.pack(anchor=tk.W)

#äratuskella default value
aratuse_aeg = current_time
aratuse_label.config(text=aratuse_aeg.strftime('%d-%m-%y %H:%M:%S'), font=("Arial", 50))


#siin vahetatakse äratuse aega
def maara_aeg():
    global aratuse_aeg, läbitud, iga_päev_var

    läbitud = False

    #keelab kinni panemise
    root.protocol("WM_DELETE_WINDOW", disable_event)

    aratuse_kell = kella_panek.get()
    aratuse_kuupäev = kuupäeva_panek.get()
    print(aratuse_kuupäev+" "+aratuse_kell)
    if iga_päev_var.get() == 1:
        aratuse_aeg = datetime.datetime.strptime(aratuse_kell, '%H:%M:%S').time()
        aratuse_label.config(text=aratuse_aeg.strftime('%H:%M:%S'), font=("Arial", 50))
    else:
        aratuse_aeg = datetime.datetime.strptime(aratuse_kuupäev+" "+aratuse_kell, '%d-%m-%y %H:%M:%S')
        aratuse_label.config(text=aratuse_aeg.strftime('%d-%m-%y %H:%M:%S'), font=("Arial", 50))



#nupp, millega panna uus aeg sisse
check = tk.Button(root, text="pane aeg", font=("Arial", 16), command = maara_aeg)
check.pack()

# Kas on heli muutuja
issound = False
is_ül = False
läbitud = True

#siin kontrollitakse, kas on äratus või mitte
def aratus_kontroll():
    global issound, is_ül, läbitud
    if current_time > aratuse_aeg and läbitud == False:
        aratus_label.config(text="ääärraaatuuuss", font=("Arial",50))
        print("ääratuus")
        
        #Kui pole heli, siis mängi heli
        if issound == False and läbitud == False:
            winsound.PlaySound("helid/mixkit-classic-alarm-995.wav", winsound.SND_LOOP | winsound.SND_ASYNC)
            issound = True

        if is_ül == False and läbitud == False:
            #võtab ülesande True/False väärtuse
            läbitud = kumb_ülesanne()
            is_ül = True

        if läbitud == True:

            root.protocol("WM_DELETE_WINDOW", close_program)

            is_ül=False
            #jätab paneb heli None
            winsound.PlaySound(None , winsound.SND_ASYNC)
            issound = False
            aratus_label.config(text="Sisesta uus äratus", font=("Arial",50))
            print("nüüd on läbi")
            
        
    elif läbitud != True:
        aratus_label.config(text="maga maga", font=("Arial",50))
    root.after(1000, aratus_kontroll)

        
#Label kus kuvab, kas äratus, või mitte
aratus_label = tk.Label(root, text="Sisesta äratus", font=("Arial", 50))
aratus_label.pack()

#äratuse kontrollimse käivitamine
aratus_kontroll()

root.mainloop()