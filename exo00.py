#ecrire son code sous format : fonctions utlisées, gestion d'erreurs, parsing, résultats, affichage
#faire trois boucles d'itérations de 0 à 9
#rassembler ces itérations sous conditions
#si conditions respectées, ajouter la combinaison à liste au préalablement créée et vide


def possible_combinations():
	combinations = []
	for i in range(0, 10):
		for j in range(0, 10):
			for k in range(0, 10):
				if i < j and j < k:
					combinations.append(str(i) + str(j) + str(k))
	print(combinations)
possible_combinations()