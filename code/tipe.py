import numpy.random as rd
import matplotlib.pyplot as plt
from pylab import *

prI = 0.32 #Probabilité d'infection
pG = 0.12 #Probabilité de guérison
pM= 0.01 #Probabilité de mort
prD = 0.75 #Probabilité de déplacement
nbD=10 #Nombre de déplacements maximum


#Renvoie la liste somme de deux listes L1 et L2 de même taille
def sommeL(L1,L2): 
    n = len(L1)
    L=[]
    for i in range(n):
        L.append(L1[i]+L2[i])
    return L 

#Prend en entrée une matrice d'individus A, et déplace les individus d'au plus une case avec une probabilité pD
def Deplacement(A,pD): 
    
    n=len(A)
    for i in range(n):
        for j in range(n):
            if rd.binomial(1,pD) == 1:
                side = rd.randint(0,3) # 0 : gauche ; 1 : droite ; 2 : Haut ; 3 : Bas
                if side == 0 and i>0: #Si le déplacement est possible
                    A[i][j],A[i-1][j] = A[i-1][j],A[i][j] #On échange les individus
                elif side == 1 and i<(n-1): 
                    A[i][j],A[i+1][j] = A[i+1][j],A[i][j]
                elif side == 2 and j<(n-1):
                    A[i][j],A[i][j+1] = A[i][j+1],A[i][j]
                else:
                    A[i][j],A[i][j-1] = A[i][j-1],A[i][j]
                    

#Prend en entrée une matrice d'individus A, n la longueur / largeur de la matrice A, pI la probabilité d'infection, et teste l'infection des 4 voisins les plus proches de A
def Infection(A,n,pI): 
    for i in range(n):
        for j in range(n):
            if A[i][j][0] == 1: #Si l'individu est infecté
                if 1<i and (A[i-1][j][0] == 0) and (rd.binomial(1,pI)) ==1 : #test de l'infection du voisin de gauche
                    A[i-1][j][0] = 1 
                   
                if i<(n-2) and (A[i+1][j][0] == 0) and (rd.binomial(1,pI)) == 1: 
                    A[i+1][j][0] = 1
                   
                if 1<j and (A[i][j-1][0] == 0) and (rd.binomial(1,pI)) == 1:
                    A[i][j-1][0] = 1
                  
                if j<(n-2) and (A[i][j+1][0] == 0) and (rd.binomial(1,pI)) ==1:
                    A[i][j+1][0] = 1

#Prend en entrée une matrice d'individus A n la longueur / largeur de la matrice A, pI la probabilité d'infection, et teste l'infection des 8 voisins les plus proches de A
def Infection2(A,n,pI):
    for i in range(n):
        for j in range(n):
            if A[i][j][0] == 1:

                #Infection des voisins les plus proches
                if 1<i and (A[i-1][j][0] == 0) and (rd.binomial(1,pI)) ==1 :
                    A[i-1][j][0] = 1
                if i<(n-2) and (A[i+1][j][0] == 0) and (rd.binomial(1,pI)) == 1: 
                    A[i+1][j][0] = 1
                if 1<j and (A[i][j-1][0] == 0) and (rd.binomial(1,pI)) == 1:
                    A[i][j-1][0] = 1
                if j<(n-2) and (A[i][j+1][0] == 0) and (rd.binomial(1,pI)) ==1:
                    A[i][j+1][0] = 1

                #Infection des voisins les plus proches diagonaux
                if 1<i and 1<j and (A[i-1][j-1][0] == 0) and (rd.binomial(1,pI/3)) ==1:
                    A[i-1][j-1][0] == 1
                if i<(n-2) and 1<j and (A[i+1][j-1][0] == 0) and (rd.binomial(1,pI/3)) ==1:
                    A[i+1][j-1][0] == 1
                if 1<i and j<(n-2) and (A[i-1][j+1][0] == 0) and (rd.binomial(1,pI/3)) ==1:
                    A[i-1][j+1][0] == 1
                if i<(n-2) and j<(n-2) and (A[i+1][j+1][0] == 0) and (rd.binomial(1,pI/3)) ==1:
                    A[i+1][j+1][0] == 1
                

#Prend en entrée une matrice d'individus A, n la longueur / largeur de la matrice A, et teste la guérison ou la mort des individus
#On considère 
def TestGM(A,n): 
    
    for i in range(n):
        for j in range(n):
            
            if A[i][j][0] == 1 and A[i][j][1] == 4: #Si l'individu est infecté depuis 4 jours
                #Si l'individu guérit
                if rd.binomial(1,pG)==1: 
                    #Il devient immunisé
                    A[i][j][0] = 3 
                else:
                    #Sinon il resdevient sain (et peut être infecté)
                    A[i][j][0] = 0 
                    A[i][j][1] = 0
            #Si l'individu est infecté depuis 4 jours et qu'il meurt
            elif (A[i][j][0] == 1) == 1 and (rd.binomial(1,pM+0.01*A[i][j][1])): 
                    A[i][j][0] = 2
                    A[i][j][1] = 0
                
            #Si l'individu est infecté depuis moins de 4 jours, et qu'il ne meurt pas
            elif A[i][j][0] == 1 and A[i][j][1] < 4:
                 A[i][j][1] +=1 #On incrémente le temps d'infection de l'individu
                 
#Modifie A afin de guérir, faire décéder, ou augmenter le temps d'infection des 
#individus de A

    
def Programme(n):
    #Prend en entrée n€N pour réaliser l'algorithme décrit
    #definition des bases
    x = [0] #x est la liste des instants
    A = [] #Matrice d'individus, elle sera de taille n*n
    pI = prI 
    pD = prD 
    cpt1,cpt2,cpt3 = 0,0,0 #Compteurs pour les individus sains, infectés, et morts
    

    #Listes pour les graphiques, comptant à l'instant i le nombre d'individus sains, infectés, guéris, et morts
    S = [] 
    I = [] 
    G = [] 
    M = [] 

    #Creation de la matrice "2D" initiale
    #A[i][j][0] = 0 si l'individu est sain
    #A[i][j][0] = 1 si l'individu est infecté
    #A[i][j][0] = 2 si l'individu est mort
    #A[i][j][0] = 3 si l'individu est guéri
    #A[i][j][1] donne le nombre de tours depuis l'infection

    for i in range(n):
        A.append([])
        for j in range(n):
            A[i].append([0,0]) #On initialise tous les individus comme sains
    A[rd.randint(0,n)][rd.randint(0,n)][0]=1 #On infecte un individu au hasard
    S.append((n*n)-1) #On initialise le nombre d'individus sains
    I.append(1) #On initialise le nombre d'individus infectés 
    G.append(0) #On initialise le nombre d'individus guéris 
    M.append(0) #On initialise le nombre d'individus morts
    cpt1=0 #On initialise le compteur d'individus sains
    k=0 #On initialise le compteur de tours
    
    while (I[k]!=0): #Tant qu'il y a des individus infectés
        x.append (k+1) #On ajoute un instant à la liste des instants
        k+=1 #On incrémente le compteur de tours
        
        #Confinement 
        
        if I[-1]>= ( (n*n)/2 ): #Si le nombre d'infectés est supérieur à la moitié de la population
            #On diminue la probabilité d'infection et de déplacement, et on diminue le nombre de déplacements
            pI = prI/1.5 
            pD = prD/2 
            nbd=5 
        elif I[-1] <= ( (n*n)/(2.5) ): #Si le nombre d'infectés est inférieur à la population/2.5
            #On réinitialise les valeurs changées
            pI = prI 
            nbd=10 
            
        
        TestGM(A,n) #On teste la guérison ou la mort des individus
        
        Infection(A,n,pI) #On teste l'infection des individus 
        
        for i in range(nbd): #On effectue nbd déplacements
            Deplacement(A,pD)  
            
        for i in range(n): #On compte les états des individus après modification
            for j in range(n):
                if A[i][j][0] == 1:
                    cpt1+=1
                elif A[i][j][0] == 2:
                    cpt2+=1
                elif A[i][j][0] == 3:
                    cpt3+=1

        #Ajout des valeurs dans les listes correspondantes
        I.append(cpt1)
        M.append(cpt2)
        G.append(cpt3)
        S.append((n*n)-cpt1-cpt2-cpt3)
        cpt1,cpt2,cpt3 = 0,0,0 #On remet les compteurs à 0 pour le prochain tour
        
        
    ##Affichage
    graph1 = plt.figure(1) #4 données
    plt.scatter(x,I,c = 'grey')
    plot(x,I, label = "infection", c = "grey")
    
    plt.scatter(x,M,c= "red")
    plot(x,M, label = "décès", c = "red")
    
    plt.scatter(x,S, c = "green")
    plot(x,S, label = "sains", c = "green")
    
    plt.scatter(x,G, c = 'blue')
    plot(x,G, label = "guéris", c = "blue")
    
    plt.legend()
    plt.grid()
    show()
    
    
    # graph2 = plt.figure(2) #Guéris et sains confondus
    # plt.scatter(x,I,c = 'grey')
    # plot(x,I, label = "infection", c = "grey")
    
    # plt.scatter(x,M,c= "red")
    # plot(x,M, label = "décès", c = "red")
    
    # plt.scatter(x,sommeL(G,S), c = "green")
    # plot(x,sommeL(G,S), label = "guéris + sains", c = "green")
    
   
    # plt.legend()
    # plt.grid()
    # show()

n=int(input("Entrez le nombre de lignes/colonnes de la matrice (Le nombre d'individus sera n*n) :"))

print("Il y a donc",n*n,"individus")
Programme(n)
