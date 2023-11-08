import tkinter as tk
from tkinter import messagebox
import time

#ei tea mis class teeb, lihtsam siin suhelda GUI ja programmi vahel
class MyGUI:
    
    def __init__(self):
        #root, algus
        self.root = tk.Tk()
        
        
        self.clock_label = tk.Label(self.root, text="")
        self.clock_label.pack(padx=20, pady=20)
        
        self.update_time()
        
        self.label = tk.Label(self.root, text="Your Message", font=("Arial", 18))
        self.label.pack(padx=10,pady=10)
        #Saab lugeda nupu vajutust
        self.textbox = tk.Text(self.root, height=5, font=("Arial", 18))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 16), variable = self.check_state)
        self.check.pack(padx=10, pady=10)
        
        #show message siin ei kutsu välja funktsiooni, vaid kasutab seda muutujana
        self.button = tk.Button(self.root, text="Show Message", font=("Arial", 18), command = self.show_message)
        self.button.pack(padx=10, pady=10)
        
        
        #mainloop, lõpp
        self.root.mainloop()
    
    def show_message(self):
        #print("Hello World")
        #self.check_state.get() annab check_state väärtuse
        if self.check_state.get() == 0:
            #self.textbox.get("1.0", tk.END) saab textboxi väärtuse, 1.0 alusta algusest, tk.END tähendab lõpp
            print(self.textbox.get("1.0", tk.END))
        else:
            #messagebox teeb uue GUI sisestatud tekstiga
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))
        

    #kui mingi nup vajutatakse tekib event, seda saab lugeda
    def shortcut(self, event):
        #print(event)
        #print(event.keysym)
        #print(event.state)
        #control enter kombinatsioon saadud kasutades ülemisi käske
        if event.state == 4 and event.keysym == "Return":
            self.show_message()
    
    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_time)
    
MyGUI()
    