
#______________________________________Initialisation________________________________________#

def L_initiale(D, nbre_periode):     # initialisation du lissage : L1
    somme = 0
    for i in range(nbre_periode):
        somme += D[i]
    return(somme/nbre_periode)

def L_tendance_initiale(D, nbre_periode):            # initialisation du lissage tendance : T1
    return((D[nbre_periode-1]-D[0])/(nbre_periode-1))
def L_saisonnalité_initiale(D, nbre_periode):
    somme= 0
    for i in range(nbre_periode):
        somme += D[i]
    moyenne=somme/nbre_periode
    S=[]
    for i in range(nbre_periode):
        S.append(D[i]/moyenne)
    return S
    


#__________________________________Calcule de la prévision__________________________________#


def Prevision(D,h, nbre_periode = 2, alpha = 0.5, beta = 0.2, gamma=0.1):     # certains paramétres sont donné par défaut
    L = [L_initiale(D, nbre_periode)]
    T = [L_tendance_initiale(D, nbre_periode)]
    S=L_saisonnalité_initiale(D,nbre_periode)
    P = []   # La prévision
    Ph=[]
    
    for i in range(len(D)-nbre_periode):
        S+=[gamma*(D[nbre_periode-1+i]/L[i])+(1-gamma)*S[i]]
        L += [alpha* D[i+nbre_periode-1]/S[i] + (1-alpha)*(L[i] + T[i])]
        T += [beta*(L[i+1] - L[i]) + (1-beta)*T[i]]
        
        P += [L[i+1] + T[i+1]]
    for i in range(h):
        Ph += [(L[i+1] + h*T[i+1])*S[i+h-nbre_periode]]
    return(P,Ph)



