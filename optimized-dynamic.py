import csv
import time
start_time = time.time()


def get_actions(fichier_csv):
    """
    Cette fonction permet de récupérer les données d'un fichier au format .csv.

    Arg = fichier_csv = string correspondant au nom du fichier au format .csv.
    Returns: actions = une liste composée de trois sous-listes : [liste du nom des actions], [liste du coût des
    actions], [liste des bénéfices des actions]
    """
    list_of_actions = []
    price = []
    profit = []
    with open(fichier_csv, newline='') as dataset:
        csv_reader = csv.reader(dataset)
        for count, row in enumerate(csv_reader):
            if count >= 1 and float(row[1]) > 1:
                profit_of_actions = int(round(float(row[1]) * float(row[2])/100, 2)*100)# La multiplication par 100
                # permet de se débarasser des centimes d'euros et de traiter des integer.
                price_of_actions = int(float(row[1])*100)
                list_of_actions.append(row[0])
                price.append(price_of_actions)
                profit.append(profit_of_actions)
                actions = [list_of_actions, price, profit]
    return actions


def get_best_invest(actions, max_cost):
    """
    Cette fonction permet de trouver l'investissment maximal qui peut être obtenu à partir d'une liste d'action pour un
    coût maximal.
    Une liste 'memory_action' et une liste 'memory_value' sont créées. Ces listes seront consultées comme s'il s'agit
    de tableaux.
    Voici un aperçu de la composition du 'tableau' 'memory_value':
                   coût=0       coût=1
            [   [   0      ,     0, etc] -> aucune action n'est prise en compte
                [   0      ,     0, etc] -> la première action est prise en compte
                [   0      ,     0, etc] -> la première et la deuxième action sont prises en compte
            etc.]
        Chaque 0 correspond à une cellule du 'tableau' qu'il va falloir calculer. Le tableau final contiendra dans
        chaque cellule le bénéfice maximal qui peut être atteint en prenant en compte certaines actions en fonction
        du coût.
    Le tableau 'memory_action' fonctionne de la même manière. Les 0 sont remplacés par une liste des actions prises
    en compte.

    Arg : actions = liste obtenue grâce à la fonction get_actions().
          max_cost = integer correspondant au coût maximal d'investissement.

    Returns: memory_table[len(actions)][max_cost] = dernière case du tableau 'memory_table' ce qui correspond au
    meilleur investissement pour un coût maximal de 'max_cost' en prenant toutes les actions possibles en compte.
    """
    list_of_actions = actions[0]
    price = actions[1]
    profit = actions[2]
    memory_actions = [[[] for cost in range(max_cost + 1)] for number_of_actions in range(len(list_of_actions) + 1)]
    memory_value = [[0 for cost in range(max_cost + 1)] for number_of_actions in range(len(list_of_actions) + 1)]
    for number_of_actions in range(1, len(list_of_actions)+1):#On ajoute les actions une par une (i.e. ligne du tableau)
        for cost in range(max_cost + 1): # On parcourt les coût de 0 à max_cost + 1 (i.e. colonne du tableau)
            # On récupère dans le tableau le bénéfice obtenu si l'action n'est pas prise en compte
            exclude_action = memory_value[number_of_actions - 1][cost]
            # Si le prix de l'action que l'on tente d'ajouter est supérieur au coût que l'on teste.
            if price[number_of_actions - 1] > cost:
                """On exclue l'action et on sauvegarde le bénéfice et la liste des actions retenues. Cela correspond au 
                même résultat que la ligne précédente pour le même coût."""
                memory_value[number_of_actions][cost] = exclude_action
                memory_actions[number_of_actions][cost] = memory_actions[number_of_actions - 1][cost]
            else:
                include_action_base_price = cost - price[number_of_actions - 1]
                if exclude_action > memory_value[number_of_actions - 1][include_action_base_price] +\
                        profit[number_of_actions - 1]:
                    """S'il est plus rentable d'exclure l'action on sauvegarde le bénéfice et la liste des actions 
                    retenues. Cela correspond au même résultat que la ligne précédente pour le même coût."""
                    memory_value[number_of_actions][cost] = exclude_action
                    memory_actions[number_of_actions][cost] = memory_actions[number_of_actions - 1][cost]
                else:
                    """Sinon on calcule le bénéfice obtenu si l'action est prise en compte."""
                    memory_value[number_of_actions][cost] = \
                        memory_value[number_of_actions - 1][include_action_base_price] + profit[number_of_actions - 1]
                    memory_actions[number_of_actions][cost] = \
                        memory_actions[number_of_actions - 1][include_action_base_price] + \
                        [list_of_actions[number_of_actions - 1]]

    memory = [memory_actions[-1][-1], memory_value[-1][-1]]
    return memory


def print_information(invest, actions):
    """
    Cette fonction permet d'écrire dans la console les résultats obtenus (i.e. dans quelles actions il faudrait
    investir, le coût et le bénéfice d'investissement).

    Arg : invest = une liste obtenue à l'aide de la fonction get_invest()
          actions = une liste obtenue grâce à la fonction get_actions()
    """
    print("Vous devriez investir dans les actions suivantes : ")
    cost = 0
    for action_name in invest[0]:
        print(action_name)
        for index, action in enumerate(actions[0]):
            if action_name == action:
                cost = cost + actions[1][index]

    print("\nCela vous coûtera " + str(cost/100) + "€.")
    print("Vous recevrez " + str(invest[1]/100) + "€ de bénéfice au bout de deux ans.")


def main():
    actions = get_actions('dataset2_Python+P7.csv')
    invest = get_best_invest(actions, 50000)
    print("--- %s seconds ---" % (time.time() - start_time))
    print_information(invest, actions)


main()
