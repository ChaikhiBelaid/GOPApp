
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
