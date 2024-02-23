'''
Combinaisons de 2 nombres

Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.


Exemples d’utilisation :
$> python exo.py
00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
$>
'''

#créer deux boucles de 0 à 99
#quand la deuxième boucle atteint son max, itérer la première
#puis relancer la deuxième
#print unique si la deuxième liste > première liste

def combination_of_numbers():
    combination_list = []
    for number_a in range(0, 100):
        for number_b in range(number_a+1, 100):
            if number_b > number_a:
                #gérer le 0 devant, séparer les deux nombres, mettre 0 devant puis les concatener
                combination_list.append("{:02d} {:02d}".format(number_a, number_b))

    result = ", ".join(combination_list)
    return result
print(combination_of_numbers())