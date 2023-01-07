import csv
import time
start_time = time.time()


def get_actions(fichier_csv):
    """
    Cette fonction permet de récupérer les données d'un fichier au format .csv.

    Arg = fichier_csv = string correspondant au nom du fichier au format .csv.
    Returns: actions = une liste composée de sous-listes. Chaque sous-liste est formée de la manière suivante :
                        [nom de l'action, coût de l'action, bénéfice obtenu par un investissement dans cette action]
    """
    actions = []
    with open(fichier_csv, newline='') as dataset:
        csv_reader = csv.reader(dataset)
        for count, row in enumerate(csv_reader):
            if count >= 1:
                ratio_value = int(row[1]) * (int(row[2])/100)
                new_action = [row[0], int(row[1]), round(ratio_value, 2)]
                actions.append(new_action)
    return actions


def create_set(number_of_actions):
    """
    Cette fonction permet de créer tous les sous-ensembles possibles pour une combinaison d'un nombre donné d'éléments.
    Ainsi, si l'on dispose de deux actions, il est possible de composer quatre combinaisons :
        [00] : aucune action ne fait partie du sous-ensemble
        [10] : la première action fait partie du sous-ensemble
        [01] : la deuxième action fait partie du sous-ensemble
        [11] : les deux actions font partie du sous-ensemble.

    Arg : number_of_actions = integer qui correspond au nombre d'actions (éléments) dont il va falloir déterminer
    les combinaisons.
    Returns: list-of_set = une liste composée de sous-listes correspondants à chaque combinaison.
    """
    list_of_set = [[] for i in range(2 ** number_of_actions)]
    for i in range(1, number_of_actions + 1):
        help_number = 0
        for set_in_progress in list_of_set:
            if help_number < ((2 ** number_of_actions)/(2 ** i)):
                binary_value = 0
            else:
                binary_value = 1
            set_in_progress.append(binary_value)
            help_number += 1
            if help_number == (2 ** number_of_actions)/(2 ** (i-1)):
                help_number = 0
    return list_of_set


def get_cost_and_value(actions, testing_set):
    """
    Cette fonction permet de calculer le coût et le bénéfice obtenu pour une combinaison d'actions.

    Arg : actions = une liste obtenue à partir de la fonction get_actions().
          testing_set = une liste composée de 0 et de 1 correspondant à une combinaison d'éléments (voir fonction
          create_set()).
    Returns : cost_and_value_of_set = une liste composée de testing_set, du coût et du bénéfice de cette combinaison.
    """
    cost = 0
    value = 0
    for index, presence in enumerate(testing_set):
        cost += presence*actions[index][1]
        value += presence*actions[index][2]
    cost_and_value_of_set = [testing_set, cost, round(value, 2)]
    return cost_and_value_of_set


def get_set_of_max_value(actions, all_set):
    """
    Cette fonction permet d'une part d'appeler la fonction get_cost_and_value() pour obtenir le coût et le bénéfice
    pour chaque combinaison de all_set(). D'autre part, lorsque le coût de la combinaison n'excède pas 500€,
    le bénéfice est comparer à un précédent set.

    Arg : actions = une liste obtenue à partir de la fonction get_actions().
          all_set = une liste composée de sous-listes correspondants à chaque combinaison.

    Returns : set_of_max_value = une liste comportant les informations de la combinaison qui permet d'obtenir le
    plus haut bénéfice pour un coût inférieur à 500€. La liste est composée de [la combinaison, le coût,
    le bénéfice].
    """
    set_of_max_value = [[], 0, 0]
    for testing_set in all_set:
        cost_and_value_of_set = get_cost_and_value(actions, testing_set)
        if (cost_and_value_of_set[1] <= 500) and (cost_and_value_of_set[2] > set_of_max_value[2]):
            set_of_max_value = cost_and_value_of_set
    return set_of_max_value


def get_best_invest(actions, all_set):
    """
    Cette fonction permet de lancer la fonction get_set_of_max_value(), puis d'écrire dans la console les résultats
    obtenus (i.e. dans quelles actions il faudrait investir, le coût et le bénéfice d'investissement).

    Arg : actions = une liste obtenue à partir de la fonction get_actions().
          all_set = une liste composée de sous-listes correspondants à chaque combinaison.
    """
    set_of_max_value = get_set_of_max_value(actions, all_set)
    print("Vous devriez investir dans les actions suivantes : ")
    for index, action in enumerate(set_of_max_value[0]):
        if action == 1:
            print(actions[index][0])
    print("\nCela vous coûtera " + str(set_of_max_value[1]) + "€.")
    print("Vous recevrez " + str(set_of_max_value[2]) + "€ de bénéfice au bout de deux ans.")


def main():
    actions = get_actions('bruteforce_dataset.csv')
    all_set = create_set(20)
    get_best_invest(actions, all_set)
    print("--- %s seconds ---" % (time.time() - start_time))


main()
