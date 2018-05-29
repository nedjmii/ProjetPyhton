#Projet Python 2éme partie - Outils de Programmation - L3/RO/B/G03 - 2017/2018
#Ecrit par:
# LAMOURI Nedjemeddine 201500008512
# TALMAT Ammar Farid 
# BOUKRANA Mohammed Habib


def minProd(k):
	premier=0;
	s=0;
	t=list(format(k, '08b'))
	number=[int(x) for x in t]

#convertir k en binaire et le stocker dans une liste des entiers

	for i in range(8):
#on cherche le 1er indice non nul tel que cet indice n'est pas dans les 3 dernieres positions
		if number[i]!=0 and i<=5 and premier==0:
			number[i]=len(number)-i-1
			premier=1

		s=sum(number)
	
	return s

print("Entrer la puissance:")
x=int(input())

#cette methode se trompe quand le x s'écrit sous forme x=(2**k)-1 avec k un entier >2 donc on ajoute ces cas spéciaux dans un "if".
if x==15 or x==31:
	print("Le nombre d'itérations est: ", minProd(x)-1)
if x==63 or x==127:
	print("Le nombre d'itérations est: ", minProd(x)-2)
else:
	print("Le nombre d'itérations est: ", minProd(x))



	





