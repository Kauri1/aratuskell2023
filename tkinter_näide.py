import tkinter as tk


root = tk.Tk()

#gui suurus ei ole vajalik
root.geometry("500x500")
#pealkiri üleval
root.title("My First GUI")

#pealkiri definitsioon
label = tk.Label(root, text="Hello World!", font=("Arial", 18))
#pealkirja kuvamine
label.pack()

#kasutaja saab kirjutada
textbox = tk.Text(root, font=("Arial", 16), height=3)
#kasti kuvamine
textbox.pack()

root.mainloop()


