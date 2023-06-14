'''
Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.


Exemples d’utilisation :
$> python exo.py 14
17
$>

Afficher -1 si le paramètre est négatif ou mauvais.
'''

#Récupérer l'argument et vérifier si int et si < 1
#écrire une boucle qui ajoute à une liste vierge les nombres premier en partant de arg jusque en trouver un
#attribuer à une variable le nombre trouvé et affiché celle-ci

import sys

def is_prime_number(number):
    if number == 2:
        return True 
    elif number % 2 == 0:
        return False #nombre pair != nombre premier
    else:
        count = 3
        result = number ** 0.5

        while count <= result:
            if number % count == 0:
                return False
            count += 2 #tester si divisible jusque sa racine carré, si pas de reste != nombre premier

        return True

try:
    number = int(sys.argv[1])
    # vérification du nombre d'arguments
    if len(sys.argv) != 2:
        print("-1")
        sys.exit()
    # vérification d'un entier positif
    if number < 1:
        print("-1")
        sys.exit()

except (ValueError, IndexError):
    print("-1")
    sys.exit()

#je créé une boucle qui teste les nombres en utilisant la fonction
prime_found = False
test_number = number + 1 #je commence par le nombre suivant

while not prime_found:
    if is_prime_number(test_number):
        prime_found = True
    else:
        test_number += 1 #passer au nombre suivant si false

if prime_found:
    print(test_number)