'''
Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.


Exemples d’utilisation :
$> python exo.py bonjour jour
true


$> python exo.py bonjour joure
false


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

#gerer les erreurs d'arguments
#si argument =! valide alors afficher error
#récuperer la taille de la string à chercher
#itérer sur la string de reference avec les bons index
#à chaque itération, sortir une sub string de la même taille que celle recherché
#comparer la sub string à celle recherché
#affiché true si oui sinon apres avoir tout parcouru, afficher false

import sys

def verify_string(reference_string, test_string):
	#recuperer la taille de la string à rechercher
	size_of_test_string = len(test_string)

	#itérer sur la string de reference
	for i in range(len(reference_string) - size_of_test_string + 1):
		#extraire une sub string de la mpême taill que celle recherché
		sub_string = reference_string[i:i+size_of_test_string]
		if sub_string == test_string:
			return True
	return False		

try:
	if len(sys.argv) != 3:
		print("error")
		sys.exit()

	reference_string = str(sys.argv[1])
	test_string = str(sys.argv[2])

except (ValueError, IndexError):
	print("error")
	sys.exit()

result = verify_string(reference_string, test_string)

print(result)