# Albion Online - Le Scanner de Marché

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Un outil interactif en ligne de commande pour analyser l'économie d'Albion Online et découvrir les opportunités d'artisanat les plus rentables.

Le script pose des questions à l'utilisateur, récupère les prix du marché en temps réel, calcule les coûts de matériaux, les taxes et le profit avec/sans focus, puis exporte un rapport complet dans un fichier Excel.

## Fonctionnalités Principales

-   **Interface Interactive :** Pas besoin de coder. Lancez le script et répondez aux questions.
-   **Données en Temps Réel :** Utilise l'API du [Albion Online Data Project](https://www.albion-online-data.com/) pour des prix toujours à jour.
-   **Calcul de Profit Avancé :** Prend en compte les taxes d'échoppes (configurables) et le Taux de Retour des Ressources (RRR) avec et sans Focus.
-   **Découverte d'Opportunités :** Scanne des catégories entières d'objets (armures, armes, montures...) pour trouver les niches rentables.
-   **Tri Personnalisable :** Triez le rapport final par rentabilité, par efficacité du focus, ou par nom.
-   **Export Excel :** Génère un fichier `.xlsx` clair et facile à analyser.

## Aperçu de l'Interface

```
=======================================================
     Le Scanner de Marche v4.1 - TRI INTERACTIF
=======================================================
Bienvenue ! Configurez votre session d'analyse.

--- Quelles catégories voulez-vous analyser ? ---
  [1] ARMOR_CLOTH
  [2] ARMOR_LEATHER
  [3] ARMOR_PLATE
  ...
Entrez le ou les numéros séparés par une virgule (ex: 1,3) :
```

## Démarrage Rapide (pour les non-développeurs)

Suivez ces étapes pour utiliser l'outil.

### Prérequis
-   **Python 3.9 ou plus récent.** Si vous ne l'avez pas, téléchargez-le depuis [python.org](https://www.python.org/downloads/).
    -   **Important pour Windows :** Lors de l'installation, cochez la case **"Add Python to PATH"**.

### Installation & Lancement

1.  **Téléchargez le Projet**
    -   Cliquez sur le bouton vert `<> Code` en haut de la page GitHub, puis sur `Download ZIP`.
    -   Décompressez le fichier ZIP dans un dossier sur votre ordinateur (par exemple, sur votre Bureau).

2.  **Lancez l'Analyse**
    -   **Sur Windows :** Double-cliquez simplement sur le fichier `lancer_analyse.bat`.
    -   **Sur macOS :**
        -   **Première fois uniquement :** Ouvrez le `Terminal`, tapez `chmod +x `, glissez-déposez le fichier `lancer_analyse_mac.sh` dans la fenêtre, puis appuyez sur Entrée. Cela donne la permission d'exécution.
        -   **Pour lancer :** Double-cliquez sur `lancer_analyse_mac.sh` (ou glissez-le dans une fenêtre de Terminal et appuyez sur Entrée).

3.  **Répondez aux Questions**
    -   La fenêtre de terminal s'ouvrira et vous guidera pour choisir les catégories, tiers, etc.

4.  **Consultez les Résultats**
    -   Une fois l'analyse terminée, un fichier `resultats_scan_... .xlsx` apparaîtra dans le dossier.

## Configuration

-   Les **critères de scan** (tiers, catégories) sont choisis de manière interactive à chaque lancement.
-   Les **taxes des villes** peuvent être ajustées dans le fichier `config.ini` avant de lancer le script.

## Pour les Développeurs : Étendre la Base de Données

La puissance du scanner dépend de sa `RECIPE_DATABASE`. Pour ajouter de nouveaux objets :

1.  Ouvrez le fichier `market_scanner.py`.
2.  Repérez la variable `RECIPE_DATABASE = { ... }`.
3.  Ajoutez votre nouvelle recette en suivant le format existant. N'oubliez pas d'inclure les clés `name`, `category`, `fame`, et `materials`.
4.  Étendez le dictionnaire `FAME_TO_FOCUS_COST` si votre objet a une valeur de renommée qui n'y figure pas.
5.  C'est tout ! Le script détectera automatiquement la nouvelle catégorie et les nouveaux objets au prochain lancement.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Remerciements

Cet outil n'existerait pas sans le travail formidable de la communauté du **Albion Online Data Project**.
