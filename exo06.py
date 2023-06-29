'''
Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.


Exemples d’utilisation :
$> python exo.py “Hello world !”
HeLlO wOrLd !


$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

#vérifier le nombre et la nature d'argument
#si la string est vide ou ne contient aucune lettre, afficher erreur
#les caractères spéciaux ne doivent pas être comptés et doivent être conservés tel quel

import sys

def modify_string(argument):
    result = ""
    letter_count = 0
    #boucle qui ne prend en compte que les lettres, si pair met en min si impair met en maj
    for char in argument:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            if letter_count % 2 == 0:
                result += char.upper()
            else:
                result += char.lower()
            letter_count += 1
        else:
            result += char

    return result

#j'ai choisi de n'avoir qu'un argument, pas obligatoire juste une préférence
if len(sys.argv) != 2:
    print("error")
    sys.exit()

argument = sys.argv[1]

# vérification de la présence d'au moins une lettre
has_letter = False
for char in argument:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        has_letter = True
        break

if not has_letter:
    print("error")
    sys.exit()

print(modify_string(argument))