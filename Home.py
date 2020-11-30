from tkinter import *
import datetime
import time
from time import strftime
from tkinter import messagebox
from suivant import suivant
#Fenetre principale : 
fen = Tk()
fen.title("GOPApp")
fen.geometry("720x500")
fen.maxsize(720, 720)
fen.config(background="#41B77F")
#Ajouter Boutton : 
quitter=Button(fen, text="Quitter",font=("Courrier",20),bg="red", fg='black', command=fen.quit)
quitter.place(x=200, y=400)
#Ajouter Boutton suivant : 
suivant=Button(fen, text="Suivant",font=("Courrier",20),bg="blue", fg='black', command=suivant)
suivant.place(x=400, y=400)

#Ajouter un frame : (boite)
f1 = Frame(fen,  bg="#41B77F",bd=1, relief=SUNKEN)
#Ajouter texte :
label_title=Label(f1, text="Bienvenue sur GOPApp", font=("Courrier",25),bg="#41B77F", fg='white')
label_title.pack(expand=YES)
#ajouter autre texte : 
label_subtitle=Label(f1, text="Une application qui vous garantit une meilleur prédiction", font=("Courrier",20),bg="#41B77F", fg='white')
label_subtitle.pack(expand=YES)
f1.pack(expand=YES)  
 

 
fen.mainloop()