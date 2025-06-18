# LE SCANNER DE MARCHE v4.1 - TRI INTERACTIF
# Ce script pose des questions a l'utilisateur, y compris le tri de l'Excel.

import configparser
import time
import requests
import pandas as pd
import numpy as np
import os

# --- BASE DE DONNÉES DES RECETTES (Le Cerveau du Scanner) ---
RECIPE_DATABASE = {
    # --- T3 ---
    "T3_ARMOR_PLATE_SET1": {"name": "Armure d'adepte T3", "category": "ARMOR_PLATE", "fame": 75, "materials": [{"id": "T3_METALBAR", "count": 16}]},
    "T3_HEAD_PLATE_SET1": {"name": "Casque d'adepte T3", "category": "ARMOR_PLATE", "fame": 38, "materials": [{"id": "T3_METALBAR", "count": 8}]},
    "T3_SHOES_PLATE_SET1": {"name": "Bottes d'adepte T3", "category": "ARMOR_PLATE", "fame": 38, "materials": [{"id": "T3_METALBAR", "count": 8}]},
    "T3_MAIN_SWORD": {"name": "Épée large d'adepte T3", "category": "WEAPON_SWORD", "fame": 75, "materials": [{"id": "T3_METALBAR", "count": 12}, {"id": "T2_LEATHER", "count": 4}]},
    "T3_TOOL_AXE": {"name": "Hache de bûcheron d'adepte T3", "category": "TOOL_AXE", "fame": 75, "materials": [{"id": "T3_PLANKS", "count": 10}, {"id": "T3_METALBAR", "count": 10}]},
    "T3_BAG": {"name": "Sac d'adepte T3", "category": "BAG", "fame": 75, "materials": [{"id": "T3_LEATHER", "count": 20}]},
    "T3_CAPE": {"name": "Cape d'adepte T3", "category": "CAPE", "fame": 38, "materials": [{"id": "T3_CLOTH", "count": 10}]},

    # --- T4 ---
    "T4_ARMOR_PLATE_SET1": {"name": "Armure de soldat T4", "category": "ARMOR_PLATE", "fame": 225, "materials": [{"id": "T4_METALBAR", "count": 16}]},
    "T4_HEAD_PLATE_SET1": {"name": "Casque de soldat T4", "category": "ARMOR_PLATE", "fame": 113, "materials": [{"id": "T4_METALBAR", "count": 8}]},
    "T4_SHOES_PLATE_SET1": {"name": "Bottes de soldat T4", "category": "ARMOR_PLATE", "fame": 113, "materials": [{"id": "T4_METALBAR", "count": 8}]},
    "T4_ARMOR_LEATHER_SET1": {"name": "Veste de mercenaire T4", "category": "ARMOR_LEATHER", "fame": 225, "materials": [{"id": "T4_LEATHER", "count": 16}]},
    "T4_HEAD_LEATHER_SET1": {"name": "Capuche de mercenaire T4", "category": "ARMOR_LEATHER", "fame": 113, "materials": [{"id": "T4_LEATHER", "count": 8}]},
    "T4_SHOES_LEATHER_SET1": {"name": "Chaussures de mercenaire T4", "category": "ARMOR_LEATHER", "fame": 113, "materials": [{"id": "T4_LEATHER", "count": 8}]},
    "T4_ARMOR_CLOTH_SET1": {"name": "Robe d'érudit T4", "category": "ARMOR_CLOTH", "fame": 225, "materials": [{"id": "T4_CLOTH", "count": 16}]},
    "T4_HEAD_CLOTH_SET1": {"name": "Capuchon d'érudit T4", "category": "ARMOR_CLOTH", "fame": 113, "materials": [{"id": "T4_CLOTH", "count": 8}]},
    "T4_SHOES_CLOTH_SET1": {"name": "Sandales d'érudit T4", "category": "ARMOR_CLOTH", "fame": 113, "materials": [{"id": "T4_CLOTH", "count": 8}]},
    "T4_MAIN_SWORD": {"name": "Épée large T4", "category": "WEAPON_SWORD", "fame": 225, "materials": [{"id": "T4_METALBAR", "count": 12}, {"id": "T4_LEATHER", "count": 4}]},
    "T4_TOOL_AXE": {"name": "Hache de bûcheron T4", "category": "TOOL_AXE", "fame": 225, "materials": [{"id": "T4_PLANKS", "count": 10}, {"id": "T4_METALBAR", "count": 10}]},
    "T4_BAG": {"name": "Sac T4", "category": "BAG", "fame": 225, "materials": [{"id": "T4_LEATHER", "count": 20}]},
    "T4_CAPE": {"name": "Cape T4", "category": "CAPE", "fame": 113, "materials": [{"id": "T4_CLOTH", "count": 10}]},

    # --- T5 ---
    "T5_ARMOR_PLATE_SET2": {"name": "Armure de chevalier T5", "category": "ARMOR_PLATE", "fame": 675, "materials": [{"id": "T5_METALBAR", "count": 16}]},
    "T5_HEAD_PLATE_SET2": {"name": "Casque de chevalier T5", "category": "ARMOR_PLATE", "fame": 338, "materials": [{"id": "T5_METALBAR", "count": 8}]},
    "T5_SHOES_PLATE_SET2": {"name": "Bottes de chevalier T5", "category": "ARMOR_PLATE", "fame": 338, "materials": [{"id": "T5_METALBAR", "count": 8}]},
    "T5_ARMOR_LEATHER_SET2": {"name": "Veste de chasseur T5", "category": "ARMOR_LEATHER", "fame": 675, "materials": [{"id": "T5_LEATHER", "count": 16}]},
    "T5_HEAD_LEATHER_SET2": {"name": "Capuche de chasseur T5", "category": "ARMOR_LEATHER", "fame": 338, "materials": [{"id": "T5_LEATHER", "count": 8}]},
    "T5_SHOES_LEATHER_SET2": {"name": "Chaussures de chasseur T5", "category": "ARMOR_LEATHER", "fame": 338, "materials": [{"id": "T5_LEATHER", "count": 8}]},
    "T5_ARMOR_CLOTH_SET2": {"name": "Robe de mage T5", "category": "ARMOR_CLOTH", "fame": 675, "materials": [{"id": "T5_CLOTH", "count": 16}]},
    "T5_HEAD_CLOTH_SET2": {"name": "Capuchon de mage T5", "category": "ARMOR_CLOTH", "fame": 338, "materials": [{"id": "T5_CLOTH", "count": 8}]},
    "T5_SHOES_CLOTH_SET2": {"name": "Sandales de mage T5", "category": "ARMOR_CLOTH", "fame": 338, "materials": [{"id": "T5_CLOTH", "count": 8}]},
    "T5_MAIN_SWORD": {"name": "Épée large T5", "category": "WEAPON_SWORD", "fame": 675, "materials": [{"id": "T5_METALBAR", "count": 12}, {"id": "T5_LEATHER", "count": 4}]},
    "T5_TOOL_AXE": {"name": "Hache de bûcheron T5", "category": "TOOL_AXE", "fame": 675, "materials": [{"id": "T5_PLANKS", "count": 10}, {"id": "T5_METALBAR", "count": 10}]},
    "T5_BAG": {"name": "Sac T5", "category": "BAG", "fame": 675, "materials": [{"id": "T5_LEATHER", "count": 20}]},
    "T5_CAPE": {"name": "Cape T5", "category": "CAPE", "fame": 338, "materials": [{"id": "T5_CLOTH", "count": 10}]},

    # --- T6 ---
    "T6_ARMOR_PLATE_SET3": {"name": "Armure de gardien T6", "category": "ARMOR_PLATE", "fame": 2025, "materials": [{"id": "T6_METALBAR", "count": 16}]},
    "T6_HEAD_PLATE_SET3": {"name": "Casque de gardien T6", "category": "ARMOR_PLATE", "fame": 1013, "materials": [{"id": "T6_METALBAR", "count": 8}]},
    "T6_SHOES_PLATE_SET3": {"name": "Bottes de gardien T6", "category": "ARMOR_PLATE", "fame": 1013, "materials": [{"id": "T6_METALBAR", "count": 8}]},
    "T6_ARMOR_LEATHER_SET3": {"name": "Veste de harceleur T6", "category": "ARMOR_LEATHER", "fame": 2025, "materials": [{"id": "T6_LEATHER", "count": 16}]},
    "T6_HEAD_LEATHER_SET3": {"name": "Capuche de harceleur T6", "category": "ARMOR_LEATHER", "fame": 1013, "materials": [{"id": "T6_LEATHER", "count": 8}]},
    "T6_SHOES_LEATHER_SET3": {"name": "Chaussures de harceleur T6", "category": "ARMOR_LEATHER", "fame": 1013, "materials": [{"id": "T6_LEATHER", "count": 8}]},
    "T6_ARMOR_CLOTH_SET3": {"name": "Robe de clerc T6", "category": "ARMOR_CLOTH", "fame": 2025, "materials": [{"id": "T6_CLOTH", "count": 16}]},
    "T6_HEAD_CLOTH_SET3": {"name": "Capuchon de clerc T6", "category": "ARMOR_CLOTH", "fame": 1013, "materials": [{"id": "T6_CLOTH", "count": 8}]},
    "T6_SHOES_CLOTH_SET3": {"name": "Sandales de clerc T6", "category": "ARMOR_CLOTH", "fame": 1013, "materials": [{"id": "T6_CLOTH", "count": 8}]},
    "T6_MAIN_SWORD": {"name": "Épée large T6", "category": "WEAPON_SWORD", "fame": 2025, "materials": [{"id": "T6_METALBAR", "count": 12}, {"id": "T6_LEATHER", "count": 4}]},
    "T6_TOOL_AXE": {"name": "Hache de bûcheron T6", "category": "TOOL_AXE", "fame": 2025, "materials": [{"id": "T6_PLANKS", "count": 10}, {"id": "T6_METALBAR", "count": 10}]},
    "T6_BAG": {"name": "Sac T6", "category": "BAG", "fame": 2025, "materials": [{"id": "T6_LEATHER", "count": 20}]},
    "T6_CAPE": {"name": "Cape T6", "category": "CAPE", "fame": 1013, "materials": [{"id": "T6_CLOTH", "count": 10}]},
    
    # --- T7 ---
    "T7_ARMOR_PLATE_ROYAL": {"name": "Armure royale T7", "category": "ARMOR_PLATE", "fame": 6075, "materials": [{"id": "T7_METALBAR", "count": 16}]},
    "T7_HEAD_PLATE_ROYAL": {"name": "Casque royal T7", "category": "ARMOR_PLATE", "fame": 3038, "materials": [{"id": "T7_METALBAR", "count": 8}]},
    "T7_SHOES_PLATE_ROYAL": {"name": "Bottes royales T7", "category": "ARMOR_PLATE", "fame": 3038, "materials": [{"id": "T7_METALBAR", "count": 8}]},
    "T7_ARMOR_LEATHER_ROYAL": {"name": "Veste royale T7", "category": "ARMOR_LEATHER", "fame": 6075, "materials": [{"id": "T7_LEATHER", "count": 16}]},
    "T7_HEAD_LEATHER_ROYAL": {"name": "Capuche royale T7", "category": "ARMOR_LEATHER", "fame": 3038, "materials": [{"id": "T7_LEATHER", "count": 8}]},
    "T7_SHOES_LEATHER_ROYAL": {"name": "Chaussures royales T7", "category": "ARMOR_LEATHER", "fame": 3038, "materials": [{"id": "T7_LEATHER", "count": 8}]},
    "T7_ARMOR_CLOTH_ROYAL": {"name": "Robe royale T7", "category": "ARMOR_CLOTH", "fame": 6075, "materials": [{"id": "T7_CLOTH", "count": 16}]},
    "T7_HEAD_CLOTH_ROYAL": {"name": "Capuchon royal T7", "category": "ARMOR_CLOTH", "fame": 3038, "materials": [{"id": "T7_CLOTH", "count": 8}]},
    "T7_SHOES_CLOTH_ROYAL": {"name": "Sandales royales T7", "category": "ARMOR_CLOTH", "fame": 3038, "materials": [{"id": "T7_CLOTH", "count": 8}]},
    "T7_MAIN_SWORD": {"name": "Épée large T7", "category": "WEAPON_SWORD", "fame": 6075, "materials": [{"id": "T7_METALBAR", "count": 12}, {"id": "T7_LEATHER", "count": 4}]},
    "T7_TOOL_AXE": {"name": "Hache de bûcheron T7", "category": "TOOL_AXE", "fame": 6075, "materials": [{"id": "T7_PLANKS", "count": 10}, {"id": "T7_METALBAR", "count": 10}]},
    "T7_BAG": {"name": "Sac T7", "category": "BAG", "fame": 6075, "materials": [{"id": "T7_LEATHER", "count": 20}]},
    "T7_CAPE": {"name": "Cape T7", "category": "CAPE", "fame": 3038, "materials": [{"id": "T7_CLOTH", "count": 10}]},

    # --- T8 ---
    "T8_ARMOR_PLATE_AVALON": {"name": "Armure d'avatar T8", "category": "ARMOR_PLATE", "fame": 18225, "materials": [{"id": "T8_METALBAR", "count": 16}]},
    "T8_HEAD_PLATE_AVALON": {"name": "Casque d'avatar T8", "category": "ARMOR_PLATE", "fame": 9113, "materials": [{"id": "T8_METALBAR", "count": 8}]},
    "T8_SHOES_PLATE_AVALON": {"name": "Bottes d'avatar T8", "category": "ARMOR_PLATE", "fame": 9113, "materials": [{"id": "T8_METALBAR", "count": 8}]},
    "T8_ARMOR_LEATHER_AVALON": {"name": "Veste d'avatar T8", "category": "ARMOR_LEATHER", "fame": 18225, "materials": [{"id": "T8_LEATHER", "count": 16}]},
    "T8_HEAD_LEATHER_AVALON": {"name": "Capuche d'avatar T8", "category": "ARMOR_LEATHER", "fame": 9113, "materials": [{"id": "T8_LEATHER", "count": 8}]},
    "T8_SHOES_LEATHER_AVALON": {"name": "Chaussures d'avatar T8", "category": "ARMOR_LEATHER", "fame": 9113, "materials": [{"id": "T8_LEATHER", "count": 8}]},
    "T8_ARMOR_CLOTH_AVALON": {"name": "Robe d'avatar T8", "category": "ARMOR_CLOTH", "fame": 18225, "materials": [{"id": "T8_CLOTH", "count": 16}]},
    "T8_HEAD_CLOTH_AVALON": {"name": "Capuchon d'avatar T8", "category": "ARMOR_CLOTH", "fame": 9113, "materials": [{"id": "T8_CLOTH", "count": 8}]},
    "T8_SHOES_CLOTH_AVALON": {"name": "Sandales d'avatar T8", "category": "ARMOR_CLOTH", "fame": 9113, "materials": [{"id": "T8_CLOTH", "count": 8}]},
    "T8_MAIN_SWORD": {"name": "Épée large T8", "category": "WEAPON_SWORD", "fame": 18225, "materials": [{"id": "T8_METALBAR", "count": 12}, {"id": "T8_LEATHER", "count": 4}]},
    "T8_TOOL_AXE": {"name": "Hache de bûcheron T8", "category": "TOOL_AXE", "fame": 18225, "materials": [{"id": "T8_PLANKS", "count": 10}, {"id": "T8_METALBAR", "count": 10}]},
    "T8_BAG": {"name": "Sac T8", "category": "BAG", "fame": 18225, "materials": [{"id": "T8_LEATHER", "count": 20}]},
    "T8_CAPE": {"name": "Cape T8", "category": "CAPE", "fame": 9113, "materials": [{"id": "T8_CLOTH", "count": 10}]},
    
    # --- MONTURES ---
    "T3_MOUNT_HORSE": {"name": "Cheval de monte T3", "category": "MOUNTS", "fame": 75, "materials": [{"id": "T2_MOUNT_HORSE", "count": 1}, {"id": "T3_LEATHER", "count": 10}]},
    "T4_MOUNT_HORSE": {"name": "Cheval de monte T4", "category": "MOUNTS", "fame": 225, "materials": [{"id": "T3_MOUNT_HORSE", "count": 1}, {"id": "T4_LEATHER", "count": 20}]},
    "T5_MOUNT_HORSE": {"name": "Cheval de monte T5", "category": "MOUNTS", "fame": 675, "materials": [{"id": "T4_MOUNT_HORSE", "count": 1}, {"id": "T5_LEATHER", "count": 20}]},
    "T6_MOUNT_HORSE": {"name": "Cheval de monte T6", "category": "MOUNTS", "fame": 2025, "materials": [{"id": "T5_MOUNT_HORSE", "count": 1}, {"id": "T6_LEATHER", "count": 20}]},
    "T7_MOUNT_HORSE": {"name": "Cheval de monte T7", "category": "MOUNTS", "fame": 6075, "materials": [{"id": "T6_MOUNT_HORSE", "count": 1}, {"id": "T7_LEATHER", "count": 20}]},
    "T8_MOUNT_HORSE": {"name": "Cheval de monte T8", "category": "MOUNTS", "fame": 18225, "materials": [{"id": "T7_MOUNT_HORSE", "count": 1}, {"id": "T8_LEATHER", "count": 20}]},
    "T3_MOUNT_OX": {"name": "Boeuf de transport T3", "category": "MOUNTS", "fame": 75, "materials": [{"id": "T2_MOUNT_OX", "count": 1}, {"id": "T3_LEATHER", "count": 10}]},
    "T4_MOUNT_ARMOREDHORSE": {"name": "Cheval de guerre T4", "category": "MOUNTS", "fame": 225, "materials": [{"id": "T4_MOUNT_HORSE", "count": 1}, {"id": "T4_METALBAR", "count": 20}]},
    
    # --- ANIMAUX (pour recettes de montures, ne pas scanner directement) ---
    "T2_MOUNT_HORSE": {"name": "Cheval de T2 (non sellé)", "category": "ANIMALS", "fame": 0, "materials": []},
    "T2_MOUNT_OX": {"name": "Boeuf de T2 (non sellé)", "category": "ANIMALS", "fame": 0, "materials": []},

    # --- ARMES : DAGUES ---
    "T4_2H_DAGGERPAIR": {"name": "Dagues T4", "category": "WEAPON_DAGGER", "fame": 225, "materials": [{"id": "T4_METALBAR", "count": 8}, {"id": "T4_LEATHER", "count": 8}]},
    "T5_2H_DAGGERPAIR": {"name": "Dagues T5", "category": "WEAPON_DAGGER", "fame": 675, "materials": [{"id": "T5_METALBAR", "count": 8}, {"id": "T5_LEATHER", "count": 8}]},

    # --- ARMES : LANCES ---
    "T4_MAIN_SPEAR": {"name": "Lance T4", "category": "WEAPON_SPEAR", "fame": 225, "materials": [{"id": "T4_METALBAR", "count": 8}, {"id": "T4_PLANKS", "count": 8}]},
    "T5_MAIN_SPEAR": {"name": "Lance T5", "category": "WEAPON_SPEAR", "fame": 675, "materials": [{"id": "T5_METALBAR", "count": 8}, {"id": "T5_PLANKS", "count": 8}]},

    # --- MAINS GAUCHES : BOUCLIERS & GRIMOIRES ---
    "T4_OFF_SHIELD": {"name": "Bouclier T4", "category": "OFFHAND_SHIELD", "fame": 113, "materials": [{"id": "T4_METALBAR", "count": 6}, {"id": "T4_PLANKS", "count": 6}]},
    "T5_OFF_SHIELD": {"name": "Bouclier T5", "category": "OFFHAND_SHIELD", "fame": 338, "materials": [{"id": "T5_METALBAR", "count": 6}, {"id": "T5_PLANKS", "count": 6}]},
    "T4_OFF_BOOK": {"name": "Grimoire T4", "category": "OFFHAND_BOOK", "fame": 113, "materials": [{"id": "T4_PLANKS", "count": 4}, {"id": "T4_CLOTH", "count": 8}]},

    # --- CONSOMMABLES : POTIONS ---
    "T4_POTION_HEAL": {"name": "Potion de soin T4", "category": "POTION", "fame": 45, "materials": [{"id": "T4_ALCOHOL", "count": 1}, {"id": "T1_ROCK", "count": 10}, {"id": "T4_PLANKS", "count": 10}]}, # Exemple simplifié
    "T6_POTION_HEAL": {"name": "Potion de soin T6", "category": "POTION", "fame": 270, "materials": [{"id": "T6_ALCOHOL", "count": 1}, {"id": "T1_ROCK", "count": 30}, {"id": "T6_PLANKS", "count": 30}]}, # Exemple simplifié

    # --- ARMES D'ARTEFACT ---
    # La Lame Maudite nécessite un "Cursed Blade" en plus des ressources normales.
    "T4_MAIN_CURSEDSTAFF_UNDEAD": {"name": "Lame maudite T4", "category": "WEAPON_CURSED", "fame": 225, "materials": [{"id": "T4_METALBAR", "count": 12}, {"id": "T4_CLOTH", "count": 4}, {"id": "T4_ARTEFACT_MAIN_CURSEDSTAFF_UNDEAD", "count": 1}]},
    "T5_MAIN_CURSEDSTAFF_UNDEAD": {"name": "Lame maudite T5", "category": "WEAPON_CURSED", "fame": 675, "materials": [{"id": "T5_METALBAR", "count": 12}, {"id": "T5_CLOTH", "count": 4}, {"id": "T5_ARTEFACT_MAIN_CURSEDSTAFF_UNDEAD", "count": 1}]},

}
# --- DICTIONNAIRE FAME -> COUT EN FOCUS (v2.0 - ETENDU) ---
FAME_TO_FOCUS_COST = {
    # T3
    38: 19, 75: 38,
    # T4
    113: 57, 225: 113,
    # T5
    338: 169, 675: 338,
    # T6
    1013: 507, 2025: 1013,
    # T7
    3038: 1519, 6075: 3038,
    # T8
    9113: 4557, 18225: 9113,
}
# --- Blocs de code du scanner ---
CITIES_RRR_BONUS = { "Lymhurst": {"FIBER": 0.259, "WOOD": 0.259}, "Bridgewatch": {"ROCK": 0.259, "HIDE": 0.259}, "Martlock": {"HIDE": 0.259, "ORE": 0.259}, "Thetford": {"ORE": 0.259, "ROCK": 0.259}, "Fort Sterling": {"WOOD": 0.259, "FIBER": 0.259}, "Caerleon": {} }
BASE_RRR = 0.152; FOCUS_RRR_BONUS = 0.357

def display_header():
    print("=======================================================")
    print("     Le Scanner de Marche v4.1 - TRI INTERACTIF")
    print("=======================================================")
    print("Bienvenue ! Configurez votre session d'analyse.\n")

def get_user_selections(question, options, allow_all=True):
    """Affiche une liste d'options et retourne les choix de l'utilisateur."""
    print(f"--- {question} ---")
    for i, option in enumerate(options, 1):
        print(f"  [{i}] {option}")
    
    if allow_all:
        print(f"  [{len(options) + 1}] TOUT SELECTIONNER")
    
    prompt_text = "Entrez le ou les numéros séparés par une virgule (ex: 1,3) : " if allow_all else "Entrez un seul numéro : "

    while True:
        try:
            choice_str = input(prompt_text)
            if not choice_str:
                print("Erreur: Vous devez faire au moins une sélection.")
                continue
            
            chosen_indices = [int(i.strip()) for i in choice_str.split(',')]
            
            if not allow_all and len(chosen_indices) > 1:
                print("Erreur: Veuillez entrer un seul numéro.")
                continue

            if allow_all and len(options) + 1 in chosen_indices:
                return options

            selections = [options[i - 1] for i in chosen_indices if 1 <= i <= len(options)]
            
            if selections:
                return selections if allow_all else selections[0]
            else:
                print("Erreur: Selection invalide. Veuillez choisir parmi les numéros de la liste.")
        except ValueError:
            print("Erreur: Veuillez entrer uniquement des numéros.")


def confirm_scan(config):
    """Affiche un résumé et demande confirmation avant de lancer."""
    print("\n------------------ RESUME DU SCAN ------------------")
    print(f"  Catégories    : {', '.join(config['categories'])}")
    print(f"  Tiers         : {', '.join(config['tiers'])}")
    print(f"  Enchantements : {', '.join(config['enchantements_display'])}")
    print(f"  Tri du rapport: {config['sort_display']}")
    print("  Taxes des villes lues depuis config.ini.")
    print("------------------------------------------------------")
    
    while True:
        confirm = input("Lancer l'analyse avec ces paramètres ? (o/n) : ").lower()
        if confirm in ['o', 'oui']:
            return True
        elif confirm in ['n', 'non']:
            return False

# ----- Les fonctions de calcul du scanner restent ici (non modifiées) -----
def get_live_market_prices(item_ids, cities):
    print(f"\n-> Connexion a l'API pour {len(item_ids)} objets dans {len(cities)} villes...")
    all_price_data = []
    item_chunks = [item_ids[i:i + 100] for i in range(0, len(item_ids), 100)]
    for i, chunk in enumerate(item_chunks):
        print(f"   ...Analyse du lot {i+1}/{len(item_chunks)}")
        item_string = ",".join(chunk)
        city_string = ",".join(cities)
        url = f"https://www.albion-online-data.com/api/v2/stats/prices/{item_string}?locations={city_string}&qualities=1"
        try:
            response = requests.get(url, timeout=45)
            response.raise_for_status()
            all_price_data.extend(response.json())
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"   /!\\ AVERTISSEMENT: Erreur lors de la recuperation du lot {i+1}: {e}")
    return all_price_data

def create_price_lookup(price_data):
    lookup = {}
    for item in price_data:
        if item['sell_price_min'] > 0:
            if item['item_id'] not in lookup: lookup[item['item_id']] = {}
            lookup[item['item_id']][item['city']] = item['sell_price_min']
    return lookup

def get_cheapest_material_cost(materials, price_lookup, enchantment):
    total_cost = 0
    for mat in materials:
        mat_id_enchanted = mat['id'] + enchantment
        if mat_id_enchanted not in price_lookup: return None
        cheapest_price = min(price_lookup[mat_id_enchanted].values())
        total_cost += cheapest_price * mat['count']
    return total_cost

def calculate_crafting_profits(recipes_to_analyze, price_lookup, config):
    results = []
    print("\n-> Calcul des profits pour toutes les recettes trouvees...")
    for recipe in recipes_to_analyze:
        material_cost = get_cheapest_material_cost(recipe['materials'], price_lookup, recipe['enchantment'])
        if material_cost is None: continue

        for city, tax in config['villes_taxes'].items():
            product_id_enchanted = recipe['id'] + recipe['enchantment']
            if product_id_enchanted not in price_lookup or city not in price_lookup[product_id_enchanted]: continue
            
            sell_price = price_lookup[product_id_enchanted][city]
            item_value_estimation = (recipe['fame'] * 4) * (2 ** recipe['enchantment_level'])
            station_tax = item_value_estimation * tax
            
            city_bonus_rrr = CITIES_RRR_BONUS.get(city,{}).get(recipe.get('category'), 0)
            total_rrr_sans_focus = BASE_RRR + city_bonus_rrr
            cost_sans_focus = material_cost * (1 - total_rrr_sans_focus)
            profit_sans_focus = sell_price - cost_sans_focus - station_tax
            
            focus_cost = FAME_TO_FOCUS_COST.get(recipe['fame'], 0)
            profit_avec_focus, profit_par_focus = 0, 0
            if focus_cost > 0:
                total_rrr_avec_focus = BASE_RRR + FOCUS_RRR_BONUS
                cost_avec_focus = material_cost * (1 - total_rrr_avec_focus)
                profit_avec_focus = sell_price - cost_avec_focus - station_tax
                profit_par_focus = (profit_avec_focus - profit_sans_focus) / focus_cost if focus_cost > 0 else 0

            results.append({ "Produit": recipe['name'] + recipe['enchantment'], "Ville de Craft": city, "Prix Vente": sell_price, "Coût Matériaux": material_cost, "Profit Net (Focus)": profit_avec_focus, "Profit / Focus": profit_par_focus, "Profit Net (Sans Focus)": profit_sans_focus })
    return pd.DataFrame(results)


def main():
    """Fonction principale du programme, maintenant interactive."""
    display_header()
    
    # --- Découverte dynamique des options ---
    available_categories = sorted(list(set(r['category'] for r in RECIPE_DATABASE.values() if r.get('category'))))
    available_tiers = sorted(list(set(k.split('_')[0] for k in RECIPE_DATABASE.keys())))
    
    # --- Séquence de questions ---
    chosen_categories = get_user_selections("Quelles catégories voulez-vous analyser ?", available_categories)
    chosen_tiers = get_user_selections("\nQuels tiers voulez-vous analyser ?", available_tiers)
    
    ench_map = {".0 (Normal)": "", ".1": "@1", ".2": "@2", ".3": "@3"}
    chosen_ench_display = get_user_selections("\nQuels niveaux d'enchantement ?", list(ench_map.keys()))
    chosen_ench_api = [ench_map[e] for e in chosen_ench_display]

    # --- NOUVELLE QUESTION POUR LE TRI ---
    sort_options_map = {
        "Par Profit / Focus (le + efficace, recommandé)": {"by": "Profit / Focus", "ascending": False},
        "Par Profit Net le plus élevé (le + rentable)": {"by": "Profit Net (Focus)", "ascending": False},
        "Par Pertes les plus élevées (ordre croissant)": {"by": "Profit Net (Focus)", "ascending": True},
        "Par Nom de l'objet (alphabétique)": {"by": "Produit", "ascending": True}
    }
    chosen_sort_display = get_user_selections("\nComment voulez-vous trier le rapport Excel final ?", list(sort_options_map.keys()), allow_all=False)
    chosen_sort_params = sort_options_map[chosen_sort_display]

    # --- Lecture du .ini pour les taxes ---
    parser = configparser.ConfigParser()
    if not parser.read('config.ini'):
        print("\nERREUR: 'config.ini' introuvable. Assurez-vous qu'il est dans le dossier.")
        input("Appuyez sur Entree pour fermer."); return
    try:
        villes_taxes = {city.strip().capitalize(): float(tax) for city, tax in parser.items('PARAMETRES_ECONOMIQUES')}
    except (configparser.NoSectionError, ValueError):
        print("\nERREUR: Section [PARAMETRES_ECONOMIQUES] manquante ou mal configurée dans 'config.ini'.")
        input("Appuyez sur Entree pour fermer."); return

    # --- Création de la configuration finale et confirmation ---
    final_config = {
        'categories': chosen_categories, 'tiers': chosen_tiers, 'enchantements': chosen_ench_api, 
        'enchantements_display': chosen_ench_display, 'villes_taxes': villes_taxes,
        'sort_params': chosen_sort_params, 'sort_display': chosen_sort_display
    }

    if not confirm_scan(final_config):
        print("Analyse annulée.")
        return

    # --- Lancement du scanner (logique existante) ---
    recipes_to_analyze = []
    # (le reste de la logique principale ne change pas...)
    for base_id, recipe_data in RECIPE_DATABASE.items():
        tier = base_id.split('_')[0]
        category = recipe_data.get('category')
        if tier in final_config['tiers'] and category in final_config['categories']:
            for ench_str in final_config['enchantements']:
                new_recipe = recipe_data.copy()
                new_recipe.update({'id': base_id, 'enchantment': ench_str, 'enchantment_level': int(ench_str.replace('@','')) if ench_str else 0})
                recipes_to_analyze.append(new_recipe)
    
    if not recipes_to_analyze:
        print("\nAVERTISSEMENT: Aucune recette ne correspond a vos criteres dans la base de donnees interne.")
        input("Appuyez sur Entree pour fermer."); return
    
    all_item_ids = {r['id'] + r['enchantment'] for r in recipes_to_analyze}
    for r in recipes_to_analyze:
        for mat in r['materials']: all_item_ids.add(mat['id'] + r['enchantment'])
    
    price_data = get_live_market_prices(list(all_item_ids), list(villes_taxes.keys()))

    if not price_data:
        print("\nERREUR: Aucune donnee n'a pu etre recuperee depuis l'API.")
        input("Appuyez sur Entree pour fermer."); return

    price_lookup = create_price_lookup(price_data)
    df_profit = calculate_crafting_profits(recipes_to_analyze, price_lookup, final_config)

    if df_profit.empty:
        print("\nRESULTAT: Aucune opportunite de profit n'a ete trouvee avec les criteres actuels.")
    else:
        df_profit.replace([np.inf, -np.inf], 0, inplace=True)
        # --- UTILISATION DU TRI DYNAMIQUE ---
        df_sorted = df_profit.sort_values(by=final_config['sort_params']['by'], ascending=final_config['sort_params']['ascending'])
        output_filename = f"resultats_scan_{time.strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
        try:
            print(f"\n-> Sauvegarde des resultats dans '{output_filename}'...")
            df_sorted.to_excel(output_filename, index=False, float_format="%.2f")
            print("   Sauvegarde terminee avec succes !")
        except Exception as e:
            print(f"\nERREUR: Impossible de sauvegarder le fichier Excel. Est-il deja ouvert ?\n   Erreur technique: {e}")

if __name__ == '__main__':
    main()