import sys
# Permet d'effectuer un temps d'arrêt dans le code
from time import sleep
# Permet de choisir avec une flèche plutôt que de devoir écrire le mot de l'item /l'action voulue
from pick import pick
# Permet de sauvegarder des variables dans un fichier externe (serialization/deserialization --> Python objects > binaire)
# sauvegarder, conserver, compresser
import pickle


def save(x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead, Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe):
    # Fonction qui prend en paramètre les variables les plus importantes et les sauvegardes dans un fichier .dat
    title = "Voulez vous: "
    options = ["Sauvegarder et quitter", "Quitter sans sauvegarder"]
    choice, index = pick(options, title, indicator='=>', default_index=0)
    sleep(1)
    variables = 0

    if index == 0:
        saveName = input("Donnez un nom a votre sauvegarde : ")
        # Sauvegarde des variables
        with open(f'{saveName}.dat', 'wb') as f:
            pickle.dump([x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead,
                        Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe], f, protocol=2)
        sys.exit()

    elif index == 1:
        sys.exit()


def load(partie):
    # ouveture du fichier contenant les variables
    with open(f'{partie}.dat', 'rb') as f:
        x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead, Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe = pickle.load(
            f)
    return x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead, Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe
