import matplotlib.pyplot as plt
import numpy as np
import random

#______________________________________Initialisation________________________________________#

def L_initiale(D, nbre_periode):     # initialisation du lissage : L1
    moyenne = 0
    for i in range(nbre_periode):
        moyenne += D[i]
    return(moyenne/nbre_periode)

def L_tendance_initiale(D, nbre_periode):            # initialisation du lissage tendance : T1
    return((D[nbre_periode-1]-D[0])/(nbre_periode-1))


#__________________________________Calcule de la prévision__________________________________#


def Prevision(D,h, nbre_periode = 2, alpha = 0.5, beta = 0.2):     # certains paramétres sont donné par défaut
    L = [L_initiale(D, nbre_periode)]
    T = [L_tendance_initiale(D, nbre_periode)]
    P = []   # La prévision
    Ph=[]
    
    for i in range(len(D)-nbre_periode):
        L += [alpha* D[i+nbre_periode-1] + (1-alpha)*(L[i] + T[i])]
        T += [beta*(L[i+1] - L[i]) + (1-beta)*T[i]]
        P += [L[i+1] + T[i+1]]
    for i in range(h):
        Ph += [L[i+1] + h*T[i+1]]
    return(P,Ph)


#___________________Proposition d'UN alpha et d'UN beta qui donnent une meilleure prévision__________#


def meilleur_coefficient(D, h,nbre_periode ,n, marge):  # la présision de l'algorithme augmente avec 'n'
    minp = np.asarray([marge]*len(D[nbre_periode:]))  # marge est la marge qu'on souhaite avoir entre la prévision et la demande réelle pour décider sur le choix du paramètre
    occu_max = 0
    alpha, beta= 0.5, 0.5
    
    for i in range(n):
        al, bt= random.random(), random.random()   #choisir des nombres aléatoires entre 0 et 1
        P,ph = np.asarray(Prevision(D,h, nbre_periode, al, bt))   #calculer la prévision selon ces deux nombres
        occurrences = np.count_nonzero((abs(P - D[nbre_periode:]) < minp) == True) 
        if  occurrences > occu_max :      #comparer avec la demande réelle
            minp = P - D[nbre_periode:]
            occu_max = occurrences
            alpha, beta= al, bt
    return(alpha, beta, occu_max)

"""nbre_periode = int(input("Saisir le nombre de période: "#))
#alpha =  float(input("Entrer la constante de lissage : "))
#beta =  float(input("Saisir le coefficient de correction de tendance: "))
h=int(input("donner l'horizon de prévision :"))
D = [50, 70, 90, 80, 90, 110, 130, 120, 140, 150, 170, 160, 150, 190, 220, 225]
période = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

Z = np.asarray(D)

alpha, beta, occu_max = meilleur_coefficient(Z, h, nbre_periode ,100000, 0.1) 


P,ph  = Prevision(D, h, nbre_periode, alpha, beta )

X = np.asarray(période)
Y = np.asarray(P)
Q=np.asarray(ph)
#___________________Traçage de la courbe de la prévision et de la demande réelle___________________#

fig, ax = plt.subplots()

ax.set(xlabel='Périodes', ylabel='La demande', title='La prévision par la méthode de Lissage Double')


ax.plot(X[nbre_periode :], Y, color='green', linestyle='dashed', linewidth=2) # Traçage de la courbe de la prévision
ax.plot(X, Z, color='blue', linewidth=2)     #Traçage de la courbe de la demande réelle
ax.plot(X[nbre_periode : ], Q, color='black', linestyle='dashed', linewidth=2) 
plt.legend(('Prévision', 'Demande réelle',"prévion à l'horizon "), shadow=True)
    

ax.grid()
plt.show()

print("Le meilleure Alpha trouvé est :", alpha)
print("Le meilleure Betta trouvé est :", beta)
print("Le nombre de prévision qui satisfaitent la marge est :", occu_max)"""