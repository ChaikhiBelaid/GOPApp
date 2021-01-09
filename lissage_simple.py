from tkinter import * 
from tkinter import messagebox  
from tkinter import ttk 
from LissageSimple import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt 
import matplotlib 

#from LissageDouble import *
def LissageSimple():
    fen=Tk()
    fen.title("Lissage simple")
    fen.geometry("720x500")
    fen.maxsize(720, 720)
    fen.config(background="AntiqueWhite3")
    fen.iconbitmap('icone.ico')
    #Ajouter un frame : (boite)
    f = Frame(fen,  bg="AntiqueWhite3",bd=1, relief=SUNKEN)
    #Ajouter texte :
    label_title=Label(f, text="Entrer les données suivantes : ", font=("Courrier",25),bg="AntiqueWhite3", fg='black')
    label_title.pack(expand=YES)
    f.place(x=100, y=0)  
    #Entrer les données nécessaires : 
    #La période :
    lablT=Label(fen, text='nombre de saisons :')
    lablT.place(x=150, y=100)
    entryT=IntVar(fen)
    Entry(fen,textvariable=entryT).place(x=350, y=100)

    #fonction OCheckDeselect
    def OCheckDeselct():
        OCheck.deselect()
    #fonction OCheckDeselect
    def NCheckDeselct():
        NCheck.deselect()
    #Check box :
    global OCheck
    global NCheck
    lablP=Label(fen, text='Paramètres par défaut: ')
    lablP.place(x=150, y=150)
    O = IntVar(fen)
    OCheck=Checkbutton(fen, text="Oui", variable=O,command=NCheckDeselct)
    OCheck.place(x=350,y=150)
    N = IntVar(fen)
    NCheck=Checkbutton(fen, text="Non", variable=N,command=OCheckDeselct)
    NCheck.place(x=400,y=150)
   
    
    #Bouton pour saisir les données :
    def SaisirLissagesimple():
        nb_saison=entryT.get()
        #Erreur si l'utilisateur a entré un nombre non entier dans nobre de saison :
        if nb_saison>4 or nb_saison==0  :
            messagebox.showerror("Erreur nombre de saisons","Veuillez entrer un nombre entier entre 1 et 4 ")
        else : 
            fene=Tk()
            fene.title("Saisir les information pour le Lissage double")
            fene.geometry("720x720")
            fene.maxsize(720, nb_saison*4*35+100)
            fene.minsize(720, nb_saison*4*35+100)
            fene.config(background="AntiqueWhite3")
            fene.iconbitmap('icone.ico')
            
            #Ajouter un frame de demnade : (boite)
            fed = Frame(fene,  bg="AntiqueWhite3",bd=1, relief=SUNKEN)
            #Entrer les demandes :
            label_title=Label(fed, text="Entrer les demandes  ", font=("Courrier",15),bg="AntiqueWhite3", fg='black')
            label_title.pack(expand=YES)
            fed.place(x=25, y=0)  
            #Liste de demande D :
            S={}
            for i in range(1,nb_saison*4+1):
                lablper=Label(fene, text=f'{i} :')
                lablper.place(x=50, y=i*35)
                S[i]=DoubleVar(fene)
                Entry(fene,textvariable=S[i]).place(x=100, y=i*35)
                
            #Entrer les paramètres : 
            #Ajouter un frame de  : (boite)
            fep = Frame(fene,  bg="AntiqueWhite3",bd=1, relief=SUNKEN)
            #Entrer les demandes :
            label_title=Label(fep, text="Entrer les paramètres de l'algorithme  ", font=("Courrier",15),bg="AntiqueWhite3", fg='black')
            label_title.pack(expand=YES)
            fep.place(x=300, y=0)  
            if N.get()==1:
                #Alpha
                Label(fene,text="Alpha : ").place(x=300, y=50)
                Alpha=DoubleVar(fene)
                Entry(fene,textvariable=Alpha).place(x=450,y=50)
                
                #nbre de périodes :
                Label(fene,text="nombre de période : ").place(x=300, y=80)
                np=IntVar(fene)
                Entry(fene,textvariable=np).place(x=450,y=80)
                #l'horizon h :
                Label(fene,text="l'horizon h: ").place(x=300, y=110)
                horizon=IntVar(fene)
                Entry(fene,textvariable=horizon).place(x=450,y=110)
                alpha=Alpha.get()
                
                #définir la commande de dernier bouton :
                def prevision():
                    #alpha :
                    alpha=Alpha.get()
                    
                    #nombre de périodes:
                    nbre_periode=np.get()
                   
                    #La liste D des demandes :
                    D=[]
                    for i in range(1,nb_saison*4+1):
                        D.append(S[i].get())
                    
                    #La prévision P et Ph :
                    P=Prevision(D,nbre_periode, alpha)
                    
                    root=Tk()
                    root.title("table with tkinter")
                    root.geometry("300x300")
                    root.minsize(400,300)
                    root.maxsize(400,300)
                    mytree = ttk.Treeview(root)
                    #define columns :
                    mytree["column"] = ("Période", "Demande", "Prévision")
                    #Formate our columns :
                    mytree.column("#0", width=0, minwidth=0)
                    mytree.column("Période",anchor=W,width=80)
                    mytree.column("Demande",anchor=CENTER,width=120)
                    mytree.column("Prévision",anchor=W,width=120)
                    #Crete headings :
                    mytree.heading("#0",text="Période",anchor=W)
                    mytree.heading("Période",text="Période",anchor=CENTER)
                    mytree.heading("Demande",text="Demande",anchor=CENTER)
                    mytree.heading("Prévision",text="Prévision",anchor=CENTER)
                    #Add data :
                    for i in range(1,nb_saison*4+1):
                        if i<=nbre_periode :
                            mytree.insert("",i, values=(i,D[i-1],"---"))
                        else :
                            mytree.insert("",i, values=(i,D[i-1],round(P[i-1-nbre_periode],5)))
                        
                    mytree.pack(pady=20)
                    #Fonction de la visualisation graphique :
                    def graphe():
                       
                        # This defines the Python GUI backend to use for matplotlib
                        matplotlib.use('TkAgg')

                        # Initialize an instance of Tk
                        root = Tk()
                        root.title("Visualisation graphique de la méthode de Lissage Double ")
                        # Initialize matplotlib figure for graphing purposes
                        fig = plt.figure(1)

                        # Special type of "canvas" to allow for matplotlib graphing
                        canvas = FigureCanvasTkAgg(fig, master=root)
                        plot_widget = canvas.get_tk_widget()

                        # génere un graphe à l'horizon h :
                        #la période à l'horizon h :
                        T=[]
                        for i in range(nbre_periode+1,nb_saison*4+1):
                            T.append(i)
                        plt.plot(T,P)
                        plt.title("graphe à l'horizon h ")
                        plt.xlabel("les périodes")
                        plt.ylabel("les prédictions ")
                        # Add the plot to the tkinter widget: 
                        plot_widget.grid(row=0, column=0)
                        mainloop()
                    #Bouton de visualisation graphique :
                    Graphe=Button(root, text="Graphe",font=("Courrier",20),bg="blue", fg='black', command=graphe)
                    Graphe.place(x=100, y=250)
                    mainloop()
                
                
                #Le bouton de résultat :
                resultat=Button(fene, text="Resultat",font=("Courrier",10),bg="blue", fg='black', command=prevision)
                resultat.place(x=300, y=200)
            if O.get()==1:
                #Titre:
                Label(fene, text="Le paramètre alpha l'algorithme est par défaut ", font=("courrier",10), bg="AntiqueWhite3", fg="red").place(x=350,y=50)
                #Alpha par défaut :
                alpha=0.5
                Label(fene,text=f"le parmètre alpha = {alpha}").place(x=300,y=80)
                
                #nbre de périodes :
                Label(fene,text="nombre de période : ").place(x=300, y=110)
                np=IntVar(fene)
                Entry(fene,textvariable=np).place(x=450,y=110)
                
                
                #définir la commande de dernier bouton :
                def prevision():
                    #nombre de périodes:
                    nbre_periode=np.get()
                   
                    #La liste D des demandes :
                    D=[]
                    for i in range(1,nb_saison*4+1):
                        D.append(S[i].get())
                    
                    #La prévision P et Ph :
                    P=Prevision(D, h,nbre_periode, alpha)                    
                   
                    root=Tk()
                    root.title("table with tkinter")
                    root.geometry("300x300")
                    root.minsize(300,300)
                    root.maxsize(300,300)
                    mytree = ttk.Treeview(root)
                    #define columns :
                    mytree["column"] = ("Période", "Demande", "Prévision")
                    #Formate our columns :
                    mytree.column("#0", width=0, minwidth=0)
                    mytree.column("Période",anchor=W,width=80)
                    mytree.column("Demande",anchor=CENTER,width=120)
                    mytree.column("Prévision",anchor=W,width=120)
                    #Crete headings :
                    mytree.heading("#0",text="Période",anchor=W)
                    mytree.heading("Période",text="Période",anchor=CENTER)
                    mytree.heading("Demande",text="Demande",anchor=CENTER)
                    mytree.heading("Prévision",text="Prévision",anchor=CENTER)
                    #Add data :
                    for i in range(1,nb_saison*4+1):
                        if i<=nbre_periode :
                            mytree.insert("",i, values=(i,D[i-1],"---"))
                        else :
                            mytree.insert("",i, values=(i,D[i-1],round(P[i-1-nbre_periode],5)))
                       
                    mytree.pack(pady=20)
                    #Fonction de la visualisation graphique :
                    def graphe():
                       
                        # This defines the Python GUI backend to use for matplotlib
                        matplotlib.use('TkAgg')

                        # Initialize an instance of Tk
                        root = Tk()
                        root.title("Visualisation graphique de la méthode de Lissage Double ")
                        # Initialize matplotlib figure for graphing purposes
                        fig = plt.figure(1)

                        # Special type of "canvas" to allow for matplotlib graphing
                        canvas = FigureCanvasTkAgg(fig, master=root)
                        plot_widget = canvas.get_tk_widget()

                        # génere un graphe à l'horizon h :
                        #la période à l'horizon h :
                        T=[]
                        for i in range(nbre_periode+1,nb_saison*4+1):
                            T.append(i)
                        plt.plot(T,P)
                        plt.title("graphe à l'horizon h ")
                        plt.xlabel("les périodes")
                        plt.ylabel("les prédictions ")
                        # Add the plot to the tkinter widget: 
                        plot_widget.grid(row=0, column=0)
                        mainloop()
                    #Bouton de visualisation graphique :
                    Graphe=Button(root, text="Graphe",font=("Courrier",20),bg="blue", fg='black', command=graphe)
                    Graphe.place(x=100, y=250)
                    mainloop()
                
                #Le bouton de résultat :
                resultat=Button(fene, text="Resultat",font=("Courrier",10),bg="blue", fg='black', command=prevision)
                resultat.place(x=300, y=200)
            mainloop()
    #Boutton confirmer :
    confirmer=Button(fen, text="Confirmer",font=("Courrier",20),bg="green", fg='black', command=SaisirLissagesimple)
    confirmer.place(x=250, y=400)
    mainloop()