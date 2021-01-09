def Prevision(D, nbre_periode, alpha=0.5):
    somme=0
    for i in range(nbre_periode):
        somme+=D[i]
    #moyenne des nbre_periode premiers :
    moyenne=somme/nbre_periode
    P=[]
    for i in range(len(D)-nbre_periode):
        if i==0 :
            P+=[moyenne]
        else :
            P+=[alpha*D[nbre_periode-1+i]+(1-alpha)*P[i-1]]
    return P



