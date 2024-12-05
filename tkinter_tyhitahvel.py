from tkinter import *
raam = Tk()
raam.title("Tühi tahvel")
# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600, height=800, bg="red")
# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()