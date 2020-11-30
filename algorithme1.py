from tkinter import *
def algorithme1():
    fen=Tk()
    fen.title("Algorthme1")
    fen.geometry("720x500")
    fen.maxsize(720, 720)
    fen.config(background="#41B77F")
    #Ajouter un frame : (boite)
    f = Frame(fen,  bg="#41B77F",bd=1, relief=SUNKEN)
    #Ajouter texte :
    label_title=Label(f, text="Entrer les données suivantes : ", font=("Courrier",25),bg="#41B77F", fg='black')
    label_title.pack(expand=YES)
    f.place(x=100, y=0)  
    #Entrer les données nécessaires : 
    #La période :
    lablT=Label(fen, text='période : ')
    lablT.place(x=150, y=100)
    entryT=Entry(fen)
    entryT.place(x=350, y=100)
    #Temps :
    labltemps=Label(fen, text='sur combien de temps ? ')
    labltemps.place(x=150, y=150)
    entrytemps=Entry(fen)
    entrytemps.place(x=350, y=150)
    #Paramètre alpha :
    lablalpha=Label(fen, text='paramètre alpha : ')
    lablalpha.place(x=150, y=200)
    entryalpha=Entry(fen)
    entryalpha.place(x=350, y=200)
    #Boutton confirmer :
    confirmer=Button(fen, text="Confirmer",font=("Courrier",20),bg="green", fg='black', command=fen.quit)
    confirmer.place(x=250, y=400)





    fen.mainloop()