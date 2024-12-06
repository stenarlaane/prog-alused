from tkinter import *

raam = Tk()
raam.title("Harjumaa haldusüksuse lipp")
tahvel = Canvas(raam, width=1000, height=600)

#Loo roheline ja valge taust
tahvel.create_rectangle(0, 300, 1000, 600, fill="green", outline="green")
tahvel.create_rectangle(0, 0, 1000, 300, fill="white", outline="white")

#Loo sümboli ringline kuju
tahvel.create_oval(400, 165, 600, 275, fill="red", outline="red")

#RINGJOON
tahvel.create_arc(400, 165, 600, 275, extent=-180, width=2)

#Loo sümboli peamine osa (punased ristkülikud)
tahvel.create_rectangle(400, 25, 600, 225, fill="red", outline="red")

#Loo ristid (valged ristkülikud)
tahvel.create_rectangle(485, 25, 515, 280, fill="white", outline="white")
tahvel.create_rectangle(400, 125, 600, 155, fill="white", outline="white")

#Loo piirjooned
tahvel.create_line(400, 25, 400, 226, width=2)
tahvel.create_line(600, 25, 600, 226, width=2)
tahvel.create_line(400, 25, 600, 25, width=2)
tahvel.create_line(485, 275, 500, 285, width=2)
tahvel.create_line(500, 285, 516, 275, width=2)

tahvel.pack()
raam.mainloop()