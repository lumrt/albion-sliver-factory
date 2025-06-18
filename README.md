# Albion Online - The Market Scanner 🇺🇸

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An interactive command-line tool to analyze the Albion Online economy and discover the most profitable crafting opportunities.

The script asks the user a series of questions, fetches real-time market prices, calculates material costs, station taxes, and profit with/without focus, then exports a comprehensive report to an Excel file.

## Core Features

-   **Interactive Interface:** No coding required. Just launch the script and answer the questions.
-   **Real-Time Data:** Uses the [Albion Online Data Project](https://www.albion-online-data.com/) API for up-to-date prices.
-   **Advanced Profit Calculation:** Takes into account station taxes (configurable) and Resource Return Rate (RRR) with and without Focus.
-   **Opportunity Discovery:** Scans entire item categories (armor, weapons, mounts...) to find profitable niches.
-   **Customizable Sorting:** Sort the final report by profitability, focus efficiency, or item name.
-   **Excel Export:** Generates a clean and easy-to-analyze `.xlsx` file.

## Interface Preview

```
=======================================================
     The Market Scanner v4.1 - INTERACTIVE SORTING
=======================================================
Welcome! Please configure your analysis session.

--- Which categories would you like to analyze? ---
  [1] ARMOR_CLOTH
  [2] ARMOR_LEATHER
  [3] ARMOR_PLATE
  ...
Enter the number(s) separated by a comma (e.g., 1,3):
```

## Quick Start (for Non-Developers)

Follow these steps to use the tool.

### Prerequisite
-   **Python 3.9 or newer.** If you don't have it, download it from [python.org](https://www.python.org/downloads/).
    -   **Important for Windows users:** During installation, check the box that says **"Add Python to PATH"**.

### Installation & Launch

1.  **Download the Project**
    -   Click the green `<> Code` button at the top of the GitHub page, then `Download ZIP`.
    -   Unzip the file into a folder on your computer (e.g., on your Desktop).

2.  **Run the Analysis**
    -   **On Windows:** Simply double-click the `lancer_analyse.bat` file.
    -   **On macOS:**
        -   **First time only:** Open the `Terminal` app, type `chmod +x `, then drag and drop the `lancer_analyse_mac.sh` file into the window, and press Enter. This grants execution permission.
        -   **To launch:** Double-click `lancer_analyse_mac.sh` (or drag it into a Terminal window and press Enter).

3.  **Answer the Questions**
    -   The terminal window will open and guide you through selecting categories, tiers, etc.

4.  **Check the Results**
    -   Once the analysis is complete, a `results_scan_... .xlsx` file will appear in the folder.

## Configuration

-   **Scan criteria** (tiers, categories) are chosen interactively on each run.
-   **City taxes** can be adjusted in the `config.ini` file before running the script.

## For Developers: Expanding the Database

The power of the scanner lies in its `RECIPE_DATABASE`. To add new items:

1.  Open the `market_scanner.py` file.
2.  Locate the `RECIPE_DATABASE = { ... }` variable.
3.  Add your new recipe following the existing format. Be sure to include the `name`, `category`, `fame`, and `materials` keys.
4.  Extend the `FAME_TO_FOCUS_COST` dictionary if your item has a fame value that is not already listed.
5.  That's it! The script will automatically detect the new category and items on the next run.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

This tool would not be possible without the amazing work of the **Albion Online Data Project** community.

# Albion Online - Market Scanner 🇫🇷

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
