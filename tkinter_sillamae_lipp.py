from tkinter import *

raam = Tk()
raam.title("Sillamäe lipp")
tahvel = Canvas(raam, width=880, height = 560)

tahvel.create_rectangle(0, 0, 880, 560, fill="blue", outline="blue")

i = 0
while i < 5:
    
    tahvel.create_rectangle(0+i*80, 560-3*70-i*70, 2*80+i*80, 560-i*70, fill="yellow", outline="yellow")
    
    tahvel.create_rectangle(880-2*80-i*80, 560-3*70-i*70, 880-i*80, 560-i*70, fill="yellow", outline="yellow")
    i += 1

tahvel.create_rectangle(880-6*80, 0, 880-5*80, 70, fill="yellow", outline="yellow")

tahvel.pack()

raam.mainloop()