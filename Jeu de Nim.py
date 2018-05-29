import random
import pickle
player1 = input("donnez le nom du premier joueur: ")
player2= input("donnez le nome du deuxième joueur: ")
player=player1
Nbcoup1=0
Nbcoup2=0
score1=0
score2=0
contr=0
T=1
Score={}
with open('score.pickle', 'rb') as handle :    # le programme récuper les scores des joueurs dans le fichier .pickle
    Score= pickle.load(handle)


if player1 in Score.keys():    #si le  joueur 1 est dans la liste la programme  affiche son meilleur score et son dernier score
    print("le meilleur score de" ,player1,  "est: %s  "   %Score[player1][0])
    print("le score de " ,player1, " de la derniere partie est de %s "    %Score[player1][1] )
else: #si non on lui affecte 0
    print("le meilleur score et le score de la derniere partie de %s est de 0 et 0 " %player1)
    Score[player1]=[1000000000,0]



if player2 in Score.keys(): #meme chose pour le joueur 2
    print("le meilleur score de",player2, "  est: %s  "  %Score[player2][0])
    print("le score de ",player2, " de la derniere partie est de %s "    %Score[player2][1] )
else:
    print("le meilleur score et le score de la derniere partie de %s est de 0 et 0 " %player2)
    Score[player2]=[1000000000,0]


leng = random.randint(4,8) #le programme choisit le nombre de tas  au hasard entre 3 et 7
Tas=[]
for i in range(0,leng):
    nombreDeBase = random.randint(5,23) # a chaque élément de la liste le programme affecte un nombre entre 5 et 23 qui représente le nombre de pierre
    l = nombreDeBase
    Tas.append(l)

long=len(Tas)
for j in range(1,long): # affichage de l'état du jeu
    print(j,"|",end="")
    for i in range(0,Tas[j]):
        print("*",end="")
    print("|",Tas[j])

while T==1:

        print("c'est au tour de  %s de jouer" %player)
        while True:
                move=[int(x) for x in input( "indiquez le tas et le nombre de pierres à retirer, séparer les deux nombre par un éspace:   ").split()]
                for j in range(0,long):
                    if move[0]==j and move[1] < Tas[j]: # le joueur indique le tas et le nombre  a retirer
                        Tas[j]=Tas[j]-move[1]
                break
        if player == player1:
            Nbcoup1=Nbcoup1 + 1
        else:
             Nbcoup2=Nbcoup2 + 1
        print("le jeu est devenu comme sa:") #afficher a chaque fois l'état du jeu
        for j in range(1,long):
                print(j,"|",end="")
                for i in range(0,Tas[j]):
                    print("*",end="")
                print("|",Tas[j])
        for i in range(1,long):
            if Tas[i]==1 : # si tout les tas sont égale à 1 alors on sort de la boucle 
                contr=contr+1
        if contr == long-1:
            T=0
        else:
                contr=0
        if player==player1: # changer de joueur
            player=player2
        else:
            player=player1


if player==player1:
     player=player2
else:
     player=player1

Nbcoup1 = Nbcoup1+1
Nbcoup2= Nbcoup2 +1

for i in range(1,Nbcoup1):       # calculer le score du joueur 1
        score1 = score1 + (i*10**i)
for i in range(1,Nbcoup2):      #calculer le score du joueur 2 
    score2 = score2+ (i*10**i)



if player == player1 and score1< Score[player1][0]: #afficher le gagnant  si c'est le player 1 et enregistrer le score
    Score[player1]=[score1,score1]
    print(" %s gagne la partie et son score est de : "  %player )
    print(score1)

elif player == player1:
    Score[player1][1]=score1
    print(" %s gagne la partie et son score est de : "  %player )
    print(score1)
    

if  player == player2 and score2 < Score[player2][0]: #afficher le gagnant si c'est le player2 et enregistrer le score
    Score[player2]=[score2,score2]
    print(" %s gagne la partie et son score est de : "  %player )
    print(score2)
if player == player2:
     Score[player2][1]= score2
     print(" %s gagne la partie et son score est de : "  %player )
     print(score2)
if Score[player1][0]==1000000000:
    del Score[player1]
if Score[player2][0]== 1000000000:
    del Score[player2]
with open('score.pickle', 'wb') as handle: # enregistrer le score dans le fichier .pickle
    pickle.dump(Score, handle, protocol=pickle.HIGHEST_PROTOCOL)
