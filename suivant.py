from tkinter import *
from lissage_double import LissageDouble
from lissage_triple import LissageTriple
from lissage_simple import LissageSimple
from meilleur import meilleur
from algo import algorithme1

def suivant():
    
    fen=Tk()
    fen.title("GOPApp")
    fen.geometry("720x500")
    fen.maxsize(720, 720)
    fen.config(background="AntiqueWhite3")
    fen.iconbitmap('icone.ico')
    
    #Ajouter un frame : (boite)
    f = Frame(fen,  bg="AntiqueWhite3",bd=1, relief=SUNKEN)
    #Ajouter texte :
    label_title=Label(f, text="Choisir un algorithme de prédiction", font=("Courrier",25),bg="AntiqueWhite3", fg='black')
    label_title.pack(expand=YES)
    f.place(x=100, y=0)  
    #Buttons des agorithmes à choisir :
    #Lissage Simple:
    alg1=Button(fen, text="Lissage Simple",font=("Courrier",20),bg="blue", fg='black', command=LissageSimple)
    alg1.place(x=50, y=200)
    #Lissage Double :
    alg2=Button(fen, text="Lissage Double",font=("Courrier",20),bg="orange", fg='black', command=LissageDouble)
    alg2.place(x=500, y=200)
    #Lissage Triple:
    alg3=Button(fen, text="Lissage Triple",font=("Courrier",20),bg="grey", fg='black', command=LissageTriple)
    alg3.place(x=50, y=300)
    #Algorithme4:
    alg3=Button(fen, text="Meilleur Méthode",font=("Courrier",18),bg="yellow", fg='black', command=meilleur)
    alg3.place(x=500, y=300)
    

    
    fen.mainloop()
    