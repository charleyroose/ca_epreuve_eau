'''
Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début
de la suite et le premier élément étant à l’index 0.


Exemples d’utilisation :
$> python exo.py 3
2
$>

Afficher -1 si le paramètre est négatif ou mauvais.
'''
#créer une liste avec les 2 premiers élément de la suite de fibonacci et leur attribuer des variables
#créer une boucle qui itère de 0 à N fois a + b = c puis ajouter c à la liste à chaque iteration
#réattribuer les valeurs aux bonnes variables à la fin de chaque boucle

import sys

# Fonction pour calculer le N ième élément de la suite de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    fibo = [0, 1]

    for x in range(0, n+1):
        c = a + b
        fibo.append(c)
        a = b
        b = c
    return fibo[n]

if len(sys.argv) != 2:
    print("Erreur, il doit y avoir un seul argument")
    sys.exit()

# Vérifier le type de donnée est un entier et affiche -1 si argument négatif
try:
    arg = int(sys.argv[1])  
    if arg < 0:
        print(-1)
        sys.exit()
except (ValueError, IndexError):
    print("Erreur, l'argument doit être un nombre entier")
    sys.exit()

result = fibonacci(arg) 
print(result)