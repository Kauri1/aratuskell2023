import tkinter as tk

from pygame import mixer

"""
mixer.init()

sound = mixer.Sound("Morning-Routine-Lofi-Study-Music(chosic.com).mp3")

root = tk.Tk()

tk.Button(root, command=sound.play).pack()

root.mainloop()
"""

root = tk.Tk()
root.title('GeeksforGeeks sound player')
 
root.geometry("500x400")
 
mixer.init()# initialise the pygame
 
def play():
    mixer.music.load("Morning-Routine-Lofi-Study-Music(chosic.com).mp3")
    mixer.music.play(loops=-1)
 
title=tk.Label(root,text="GeeksforGeeks",bd=9,
            font=("times new roman",50,"bold"),bg="white",fg="green") 
title.pack() 
 
play_button = tk.Button(root, text="Play Song", font=("Helvetica", 32), command=play)
play_button.pack(pady=20)
root.mainloop()