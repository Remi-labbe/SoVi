---
lang: fr-FR
title: SoVi
subtitle: Visualisateur de réseau social
author:
    - Rémi Labbé
date: Decembre 2021
documentclass: report
toc: true
fontsize: 12
mainfont: Source Code Pro Medium
monofont: mononoki Nerd Font
---

# Notice

```
pip install -r requirements.txt
python sovi
```
Une fois le logiciel lancé vous pouvez ouvrir un fichier grace au menu situé
 en haut a gauche de la fenetre.

Ensuite l'interface se divise selon les opérations que vous pouvez réaliser.

# Les Choix

Les bases d'un projet reposent toujours durement sur les choix faits au départ,
 ceux-cis determineront les posibilités pour le langage ou l'optimisation pour
 les structures.

## Le Langage

Pour réaliser ce projet j'ai choisi de me tourner vers python, ayant peu
 utilisé ce langage j'ai voulu ajouter un peu de découverte à ce projet.
 Le python est un langage tres utilisé dans le monde des sciences des données
 et j'ai trouvé que le sujet de ce projet s'en rapprochait beaucoup.
 Bien qu'étant connu comme un langage "lent" j'ai essayé d'optimiser mes
 structures pour que cela ne me porte pas prejudice.

## Fichiers

Il nous était demandé de lire et écrire les données dans des fichiers sous
 forme de listes d'adjacences. J'ai choisi pour cela d'utiliser des fichier au
 format CSV avec pour séparateur la virugle ','. Format souvent utilisé
 en sciences des données et en python il est assez simple à lire et à écrire.

Les données sont donc représentées ainsi dans ces fichiers:
- Chaque ligne représente les relation d'un sommet
- La premiere case est le sommet Source
- Tous ceux qui le suivent sont ses successeurs

Dans chaque case on trouvera les information d'un utilisateur sous la forme:
```
Nom;Prénom;Age
```

ou celles d'une page:

```
Nom
```

## Structures de données

Les sommets de ce graphe sont représentés par 2 classes héritant d'une classe
 commune, la classe Sommet, je ne la détaillerai pas ici car elle a tres peu
 de contenu et représente surtout le lien entre les 2 premiers types de données
 créés.

### Utilisateurs

Un utilisateur connait ses successeurs et ses prédécesseurs afin d'optimiser
 les temps de calculs pour les algorithmes demandés.
```
Utilisateur(
Nom: str
Prénom: str
Age: int
successeurs: list[Utilisateur|Page]
prédécesseurs : list[Utilisateur]
)
```
Ce dernier peut suivre des pages et/ou d'autres utilisateurs.
 Il peut aussi administrer certaines page du réseau.

### Pages

Une page connait aussi ses prédécesseurs mais elle ne peut pas suivre d'autres
 comptes, elle a en revenche une liste d'utilisateurs qui l'administrent
```
Page(
Nom: str
administrateurs: list[Utilisateurs]
prédécesseurs : list[Utilisateurs]
)
```

### Graphe

Le graphe est la structure principale, c'est elle qui représente le reseau
 complet!

Pour la développer j'ai choisi d'utiliser des dictionnaires, c'est la
 structure proposée par Python s'approchant des tables de Hachage. Fournissant
 des méthodes pour lire et écrire en temps constants ils favorisent la
 complexite.

Un graphe contient donc la liste de ses sommets et la listes de ses arcs sous
 forme de liste de successeurs dans un dictionnaire.
```
Graphe(
sommets: dict
arcs: dict
)
```

# Algorithmes

Cette partie sera courte, le projet portant selon moi plus sur la visualisation
 que sur des montagnes de calculs.
 Ceux-cis ont été relativement simple a implementer grace au choix présente plus
 haut.

## Page Rank

Bien connu car au coeur du fonctionnement de l'internet moderne, plus
 particulierement utilise pour faire fonctionner les moteurs de recherche.

La recherche des elements utlisés pour le calcul à chaque itération se faisant
 en temps constant avec les structures que j'ai choisi, Le calcul de complexite
 peu donc simplement se faire depuis la formule mathématique et on trouve

O(n<sup>2</sup>)

## Plus Courte Distances

Comme pour l'algorithme du Page Rank, les structures de données choisies
 permettent de ne pas rajouter de coup en temps a l'éxécution.

La complexite de cet algorithme est donc:

O(n<sup>2</sup>)

# Difficultes

J'ai rencontré quelques difficultés liees au langage que j'ai pu résoudre
 relativement rapidement grace aux différentes documentations disponibles.

Le probleme le plus evident rencontre est le manque de temps et d'organisation,
 c'est un point qu'il me reste à améliorer dans mes futurs projets.

La suppression de sommets dans le graphe n'est pas fonctionnel à l'heure du
 rendu.

# Conclusions

Python est un langage assez plaisant à prendre en main par sa syntaxe simple.
 Cependant c'est aussi celle-ci qui n'a tenu loin de ce langage jusqu'ici car
 plutot marginale.

Le développement d'une application graphique était intéressant, de nouvelle
 possibilité ont pu etre appercues comparés au précédents projets qui se
 limitaient souvent au terminal.

Une interface utilisateur étant demandée je pense que je me serais tourné vers
 des outils de développement web si le choix de langage n'avait pas été limité.
