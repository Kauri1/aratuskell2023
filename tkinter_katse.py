import tkinter as tk
import time

root = tk.Tk()

#kella definitsioon
def update_time():
    global current_time
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time, font=("Arial",100))
    root.after(1000, update_time)

    print(current_time)

#kuvab aega
clock_label = tk.Label(root, text="")
clock_label.pack()

#uuendab aega
update_time()


aratuse_label = tk.Label(root, text="00:00:00")
aratuse_label.pack()



#äratuse panek
aratuse_panek = tk.Text(root, font=("Arial", 16), height=3)
aratuse_panek.pack()


def maara_aeg():
    global aratuse_aeg
    aratuse_aeg = aratuse_panek.get("1.0", tk.END)
    aratuse_label.config(text=aratuse_aeg, font=("Arial", 100))


check = tk.Button(root, text="pane aeg", font=("Arial", 16), command = maara_aeg)
check.pack()

#äratuskella definitsioon
aratuse_aeg = "00:00:00"

def aratus_kontroll():
    if current_time > aratuse_aeg:
        aratus_label.config(text="ääääärraaaaatuuuuuuuuss", font=("Arial",100))
        print("ääratuus")
    else:
        aratus_label.config(text="maga maga", font=("Arial",100))
    root.after(1000, aratus_kontroll)

#kuvab äratust
aratus_label = tk.Label(root, text="maga maga", font=("Arial", 100))
aratus_label.pack()

aratus_kontroll()

root.mainloop()