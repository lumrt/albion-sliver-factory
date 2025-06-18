@echo off
REM Permet d'afficher correctement les accents dans la console
chcp 65001 > nul

REM =======================================================
REM  LANCEUR POUR WINDOWS
REM  (Le Meme Gemini v3.0+)
REM =======================================================

REM Cette ligne permet au script de toujours s'exécuter
REM depuis le dossier où il se trouve. C'est l'équivalent de 'cd "$(dirname "$0")"'
cd /d "%~dp0"

echo =======================================================
echo  Lancement du Scanner de Marche pour Albion Online
echo  (Version Windows)
echo  Ce processus peut prendre plusieurs minutes...
echo =======================================================
echo.

REM Sur Windows, les commandes standards sont 'python' et 'pip'
REM (au lieu de python3/pip3) si Python a été correctement installé.
echo --> Etape 1/3: Verification des dependances...
pip install -r requirements.txt

echo.
echo --> Etape 2/3: Lancement du script d'analyse...
python market_scanner.py

echo.
echo --> Etape 3/3: Analyse terminee !
echo =======================================================
echo  Vous pouvez trouver les resultats dans le fichier
echo  'resultats_scan_....xlsx'
echo =======================================================
echo.

REM Attend que l'utilisateur appuie sur une touche avant de fermer.
REM C'est l'équivalent de 'read -p "..."'
pause