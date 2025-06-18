#!/bin/bash

# =======================================================
#  LANCEUR POUR MACOS / LINUX
#  (Le Meme Gemini v3.0)
# =======================================================

# Cette ligne permet au script de toujours s'exécuter
# depuis le dossier où il se trouve, peu importe d'où on le lance.
cd "$(dirname "$0")"

echo "======================================================="
echo " Lancement du Scanner de Marche pour Albion Online"
echo " (Version macOS)"
echo " Ce processus peut prendre plusieurs minutes..."
echo "======================================================="
echo ""

# Sur Mac, il est préférable d'utiliser 'python3' et 'pip3' 
# pour être sûr d'utiliser la bonne version de Python.
echo "--> Etape 1/3: Verification des dependances..."
pip3 install -r requirements.txt

echo ""
echo "--> Etape 2/3: Lancement du script d'analyse..."
python3 market_scanner.py

echo ""
echo "--> Etape 3/3: Analyse terminee !"
echo "======================================================="
echo " Vous pouvez trouver les resultats dans le fichier"
echo " 'resultats_scan_marche.xlsx'"
echo "======================================================="
echo ""

# Attend que l'utilisateur appuie sur Entrée avant de fermer.
read -p "Appuyez sur la touche Entree pour fermer cette fenetre..."