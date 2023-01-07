import csv


def get_actions(fichier_csv):
    """
    Cette fonction permet de récupérer les données d'un fichier au format .csv.

    Arg = fichier_csv = string correspondant au nom du fichier au format .csv.
    Returns: actions = un dictionnaire pour lequel chaque clé correspond au nom d'une action, et chaque valeur est
    composée d'une liste [coût de l'action, profit : % du coût obtenu, profit : valeur brute]
    """
    actions = {}
    with open(fichier_csv, newline='') as dataset:
        csv_reader = csv.reader(dataset)
        for count, row in enumerate(csv_reader):
            if count >= 1 and float(row[1]) > 1:
                value = float(row[1]) * (float(row[2])/100)
                new_action = [float(row[1]), float(row[2]), round(value, 2)]
                actions[row[0]] = new_action
    return actions


def sort_actions_by_profit_percentage(actions):
    """
    Cette fonction permet de trier le dictionnaire 'actions' en fonction du pourcentage du coût obtenu.

    Arg : actions = dictionnaire obtenu grâce à la fonction get_actions()
    Returns: sorted_actions = le dictionnaire actions trié.
    """
    sorted_actions = {action_name: dict_value for action_name, dict_value in sorted(actions.items(),
                                                                                    key=lambda item: item[1][1],
                                                                                    reverse=True)}
    return sorted_actions


def get_invest(sorted_actions):
    """
    Cette fonction permet de sélectionner l'action qui serait la plus rentable (% de bénéfice le plus élévé) et
    essaye d'ajouter la deuxième action la plus rentable. Le coût doit toujours rester inférieur à 500€.

    Arg : sorted_actions = un dictionnaire obtenu grâce à la fonction sort_actions_by_profit_percentage()
    Returns : invest = une liste composée de : [[liste des actions dans lesquelles investir], coût d'investissement,
    bénéfice d'investissement].
    """
    list_of_actions = []
    cost = 0
    value = 0
    for item in sorted_actions.items():
        cost_of_item = item[1][0]
        testing_cost = cost + cost_of_item
        if testing_cost <= 500:
            list_of_actions.append(item[0])
            cost = testing_cost
            value += item[1][2]
    invest = [list_of_actions, round(cost, 2), round(value, 2)]
    return invest


def print_information(invest):
    """
    Cette fonction permet d'écrire dans la console les résultats obtenus (i.e. dans quelles actions il faudrait
    investir, le coût et le bénéfice d'investissement).

    Arg : invest = une liste obtenue à l'aide de la fonction get_invest()
    """
    print("Vous devriez investir dans les actions suivantes : ")
    for action in invest[0]:
        print(action)
    print("\nCela vous coûtera " + str(invest[1]) + "€.")
    print("Vous recevrez " + str(invest[2]) + "€ de bénéfice au bout de deux ans.")


def main():
    actions = get_actions('dataset2_Python+P7.csv')
    sorted_actions = sort_actions_by_profit_percentage(actions)
    invest = get_invest(sorted_actions)
    print_information(invest)


main()
