'''
Combinaisons de 3 chiffres

Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant, dans l’ordre croissant. La répétition est volontaire.

Exemples d’utilisation :
$> python exo.py
012, 013, 014, 015, 016, 017, 018, 019, 023, 024, ... , 789
$>

987 n’est pas là parce que 789 est présent.

020 n’est pas là parce que 0 apparaît deux fois.

021 n’est pas là parce que 012 est présent.

000 n’est pas là parce que cette combinaison ne comporte pas exclusivement des chiffres différents les uns des autres.
'''



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
	result = ", ".join(combinations)
	print(result)
possible_combinations()