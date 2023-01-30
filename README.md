# Résolvez des problèmes en utilisant des algorithmes en Python

## Description
Le but de ce projet est de concevoir un algorithme qui maximise le profit de clients après deux ans d'investissement dans des actions.
L'algorithme doit suggérer une liste des actions les plus rentables. 
La description plus complète du fonctionnement des algorithmes se trouve dans le fichier diapositives.pdf.

### Contraintes 
Trois contraintes doivent être respectées :
- Chaque action ne peut être achetée qu'une seule fois.
- Nous ne pouvons pas acheter une fraction d'action.
- Nous pouvons dépenser au maximum 500 euros par client.

### Algorithme de force brute
L'algorithme de force brute doit tester toutes les différentes combinaisons d'actions qui correspondent aux contraintes.
Le programme doit donc lire un fichier contenant des informations sur les actions, explorer toutes les combinaisons possibles et afficher le meilleur investissement.

### Optimisation d'algorithme
Le nouvel algorithme n'a pas besoin d'explorer toutes les combinaisons possibles. L'algorithme doit donc s'en trouver accéléré. 

## Procédure d'installation

### Import du dépôt Github
Dans un dossier de travail, importez le dépôt github puis, changez de répertoire courant pour vous positionner dans le dossier. 
```sh
$ git clone https://github.com/lcourdes/Developpez-des-problemes-en-utilisant-des-algorithmes-en-python.git
$ cd Developpez-des-problemes-en-utilisant-des-algorithmes-en-python
```

### Création d'un environnement virtuel
Il est recommandé d'installer un environnement virtuel. Pour ce faire, suivez les instructions 
ci-dessous :

- S'il ne l'est pas déjà, installez le package *virtualenv* :
```sh
$ pip install virtualenv
```

- Créez un environnement de travail et activez-le :
```sh
$ virtualenv env
$ source env/bin/activate
```

### Installation des librairies
Actuellement aucune librairie ne doit être installée pour démarrer les programmes.

## Utilisation du programme

### Démarrage des algorithmes
Assurez-vous lors de toute utilisation que l'environnement virtuel est activé.
Trois fichiers python sont disponibles : 
- bruteforce.py, 
- optimized-glouton.py qui utilise un algorithme glouton,
- optimized-dynamic.py qui utilise un algorithme de programmation dynamique.

```sh
$ python3 bruteforce.py
$ python3 optimized-glouton.py
$ python3 optimized-dynamic.py
```

### Les bases de données de tests

Les scripts python peuvent être utilisés avec différentes bases de données au format csv. 
Nous fournissons ici trois bases : 
- bruteforce_dataset.csv
- dataset1_Python+P7.csv
- dataset2_Python+P7.csv

Nous recommandons d'utiliser le fichier bruteforce.py avec seulement la base de données bruteforce_dataset.csv. En effet, 
le script ne présentant pas un algorithme optimisé, il est préférable d'utiliser une base de données restreinte.

## Lien Github

[![github_icone](README_pictures/github.png)](https://github.com/lcourdes/Developpez-des-problemes-en-utilisant-des-algorithmes-en-python)