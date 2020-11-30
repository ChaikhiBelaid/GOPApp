from tkinter import *
from algorithme1 import algorithme1
def suivant():
    fen=Tk()
    fen.title("GOPApp")
    fen.geometry("720x500")
    fen.maxsize(720, 720)
    fen.config(background="#41B77F")
    #Ajouter un frame : (boite)
    f = Frame(fen,  bg="#41B77F",bd=1, relief=SUNKEN)
    #Ajouter texte :
    label_title=Label(f, text="Choisir une algorithme de prédiction", font=("Courrier",25),bg="#41B77F", fg='black')
    label_title.pack(expand=YES)
    f.place(x=100, y=0)  
    #Buttons des agorithmes à choisir :
    #Algorithme1:
    alg1=Button(fen, text="algorithme1",font=("Courrier",20),bg="blue", fg='black', command=algorithme1)
    alg1.place(x=50, y=200)
    #Algorithme2 :
    alg2=Button(fen, text="algorithme2",font=("Courrier",20),bg="orange", fg='black', command=algorithme1)
    alg2.place(x=500, y=200)
    #Algorithme3:
    alg3=Button(fen, text="algorithme3",font=("Courrier",20),bg="grey", fg='black', command=algorithme1)
    alg3.place(x=50, y=300)
    #Algorithme4:
    alg3=Button(fen, text="algorithme4",font=("Courrier",20),bg="yellow", fg='black', command=algorithme1)
    alg3.place(x=500, y=300)
    


    fen.mainloop()