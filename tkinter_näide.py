import tkinter as tk

root = tk.Tk()

#gui suurus ei ole vajalik
root.geometry("500x500")
#pealkiri üleval
root.title("My First GUI")

#tekst definitsioon
label = tk.Label(root, text="Hello World!", font=("Arial", 18))
#pealkirja kuvamine
label.pack()

#kasutaja saab kirjutada
textbox = tk.Text(root, font=("Arial", 16), height=3)
#kasti kuvamine padx-kui palju ruumi(px) servadest(x kordinaat) vaba
textbox.pack(padx=10)

#1 rida väike kirjutusala
myentry = tk.Entry(root)
myentry.pack()

#nupp
button = tk.Button(root, text="Click Me!", font=("Arial", 16))
button.pack(pady=10)

#gridi tegemine
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

#paneme root asemel buttonframe, kuna see nagu uus ekraan
btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky="we")

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky="we")

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky="we")

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky="we")

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky="we")

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky="we")

#lisa grid lehele
buttonframe.pack(fill="x")


anotehrbtn = tk.Button(root, text="test")
#saab panna elemente kordinaatide järgi
anotehrbtn.place(x=100,y=200, height = 100, width=100)


root.mainloop()

