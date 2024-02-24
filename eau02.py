'''
Paramètres à l'envers

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

#faire une boucle qui itère chaque arguments donné dans une liste en partant de la fin
#assigner à une variable le résultat sans afficher le nom du script
#afficher à l'aide d'une boucle

import sys

def reverse_args(arguments):
    reversed_list = []
    for number in arguments[::-1]:
        reversed_list.append(number)
    return reversed_list

result = reverse_args(sys.argv[1:])

for element in result:
    print(element)