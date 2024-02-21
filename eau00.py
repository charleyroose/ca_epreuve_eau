'''
Combinaisons de 3 chiffres

Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant,
dans l’ordre croissant. La répétition est volontaire.


Exemples d’utilisation :
$> python exo.py
012, 013, 014, 015, 016, 017, 018, 019, 023, 024, ... , 789
$>

987 n’est pas là parce que 789 est présent.

020 n’est pas là parce que 0 apparaît deux fois.

021 n’est pas là parce que 012 est présent.

000 n’est pas là parce que cette combinaison ne comporte pas exclusivement des chiffres différents les uns des autres.
'''

#faire une boucle pour chaque chiffre de 0 à 10
#vérifier si les trois chiffres sont différents
#vérifier si a < b et b < c pour éviter les doublons
#si oui, ajouter à une liste

def combination_of_numbers():
    combination_lst = []
    for number_a in range(0, 10):
        for number_b in range(0, 10):
            for number_c in range(0, 10):
                if number_a < number_b and number_b < number_c:
                    combination_lst.append(str(number_a) + str(number_b) + str(number_c))
    #concaténer en une seule chaîne de caractère séparé par des virgules
    result = ", ".join(combination_lst) 
    return result

print(combination_of_numbers())