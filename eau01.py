'''
Combinaisons de 2 nombres

Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.


Exemples d’utilisation :
$> python exo.py
00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
$>
'''

#créer une liste vide
#créer deux boucle jusque 100 dont l'une supérieur de 1 à la première
#ajouter chaque itération à la liste vide
#ajouter un 0 pour avoir des nombres au format 00

def combination_of_numbers():
	combination_list = []
	for number_a in range(0, 100):
		for number_b in range(number_a+1, 100):
			combination_list.append("{:02d} {:02d}".format(number_a, number_b))

	result = ", ".join(combination_list)
	return result
print(combination_of_numbers())