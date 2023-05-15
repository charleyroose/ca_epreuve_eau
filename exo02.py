'''
Créez un programme qui affiche ses arguments reçus à l’envers.


Exemples d’utilisation :
$> python exo.py “Suis” “Je” “Drôle”
Drôle
Je
Suis


$> python exo.py ha ho
ho
ha

$> python exo.py “Bonjour 36”
Bonjour 36

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys
#definir une fonction qui inverse les arguments de la liste
def reverse_arguments(args):
	return args[::-1]

if len(sys.argv) < 2:
	print("Erreur, il n'y a pas assez d'arguments")
	sys.exit
#definir une nouvelle liste sans le nom du script
args = sys.argv[1:]

args_reversed = reverse_arguments(args)

for n in args_reversed:
	print(n)