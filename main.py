# Permet d'effectuer un temps d'arrêt dans le code
from pick import pick
# Permet de récupérer la valeur des touches du clavier
import msvcrt
# Permet de choisir avec une flèche plutôt que de devoir écrire le mot de l'item /l'action voulue
from time import sleep
from map import Boss1, Boss2, Final_Boss, LvlDesign
from menu import *
from shop import fonction_shop
from fight import encounter, hp, hp_max, niveau, exp, lvlgain, atk, dfs
from inventory import inventaire
from map import Monster_Encounter, Player_Movement, world_map, Monster_Movement, Goblin_Movement, LvlDesign
from save import save, load
# Permet d'executer une commande systeme
from os import system


def Main():

    global inventaire, hp, hp_max, exp, niveau, lvlgain, master_sword_here, atk, sword, dfs, filename, want_load, lvl, foe
    want_load = False
    # affichage du menu
    filename, want_load = main_menu()
    # on vérifie si le joueur veut  charger une ancienne partie sinon on initialise les variables de base
    if want_load == True:
        x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead, Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe = load(
            filename)
        pass
    else:
        from map import lvl, Monster, Goblin, foe, Boss1, Boss2, Final_Boss, Master_Roshi
        argent = 50

        liste_item_etage1 = ["Potion", "Bombe"]
        liste_prix_etage1 = [20, 30]

        liste_item_etage2 = ["Potion +", "Bombe"]
        liste_prix_etage2 = [30, 30]

        liste_item_etage3 = ["Potion X", "Explo-bombe"]
        liste_prix_etage3 = [40, 60]
        # 19,14
        y = 3
        x = 14
        gobliny = 19
        goblinx = 7
        monstery = 9
        monsterx = 10
        Player_Life = 1
        monsterdead = False
        Boss1dead = False
        Boss2dead = False
        master_dead = False
        Final_Bossdead = False
        visited = 0  # Permet de savoir si le premier magasin a déjà été visité
        visited2 = 0  # Permet de savoir si le deuxième magasin a déjà été visité
        visited3 = 0  # Permet de savoir si le troisième magasin a déjà été visité
    Player_Life = 1
    # Affichage de la map
    world_map(y, x, monstery, monsterx, gobliny, goblinx)
    # Affichage des stats
    print(f"Argent: {argent} or       {hp}hp / {hp_max}hp")
    print(f"Stats: {atk} Atk        {dfs} dfs")
    print(f"Niveau: {niveau}        {exp}xp / {lvlgain}xp")
    print(f"Votre inventaire: {inventaire}")
    # Boucle principale qui ne s'arrete tant que le joueur n'est pas mort
    while Player_Life > 0:
        # On indique aux autres fonctions sur quelle carte (une, deux ou trois) le joueur se trouve.
        lvl = LvlDesign(y, lvl)
        # On récupère la valeur des touches du clavier de l'utilisateur
        char = msvcrt.getche().decode()
        Move = char
        # Coordonnées du joueur
        y, x = Player_Movement(Move, y, x)
        # Coordonnées du monstre (celui tout rouge en zone 2)
        monstery, monsterx = Monster_Movement(monstery, monsterx)
        # Coordonnées du goblin (celui tout rouge en zone 1)
        gobliny, goblinx = Goblin_Movement(gobliny, goblinx)
        # Case de sauvegarde demandant au joueur si oui ou non il veut sauvegarder
        if y == 15 and x == 5:
            title3 = "Vous arrivez dans une zone de sauvegarde. Voulez vous y entrer ?"
            options3 = ["oui", "non"]
            choice, index = pick(
                options3, title3, indicator='=>', default_index=0)
            if choice == "oui" and index == 0:
                save(x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead,
                     Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe)
                # save
            else:
                pass
        if y == 13 and x == 14:
            title3 = "Vous arrivez dans une zone de sauvegarde. Voulez vous y entrer ?"
            options3 = ["oui", "non"]
            choice, index = pick(
                options3, title3, indicator='=>', default_index=0)
            if choice == "oui" and index == 0:
                save(x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead,
                     Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe)
                # save
            else:
                pass

        if y == 3 and x == 3:
            title3 = "Vous arrivez dans une zone de sauvegarde. Voulez vous y entrer ?"
            options3 = ["oui", "non"]
            choice, index = pick(
                options3, title3, indicator='=>', default_index=0)
            if choice == "oui" and index == 0:
                save(x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead,
                     Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe)
                # save
            else:
                pass
        # Case du monstre rouge en zone 2 qui bouge en même temps que le joueur
        if y == monstery and x == monsterx:
            monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk = encounter(
                Monster, lvl)
            argent += argent_mob
        # Case du goblin en zone 2 qui bouge en même temps que le joueur
        if y == gobliny and x == goblinx:
            encounter(Goblin, lvl)
        # Case du magasin de la zone 1
        if y == 16 and x == 13:
            if visited == 0:
                # Boite de dialogue qui s'exécute a la première rencontre
                shopkeeper1()
                sleep(1)
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage1, liste_prix_etage1)
            visited += 1
            y += 1
        # Case du magasin de la zone 2
        if y == 13 and x == 3:
            if visited2 == 0:
                # Boite de dialogue qui s'exécute a la première rencontre
                shopkeeper2()
                sleep(1)
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage2, liste_prix_etage2)
            visited2 += 1
            y -= 1
        # Case du magasin de la zone 3
        if y == 3 and x == 10:
            if visited3 == 0:
                # Boite de dialogue qui s'exécute a la première rencontre
                shopkeeper3()
                sleep(1)
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage3, liste_prix_etage3)
            visited3 += 1
            y += 1
        # Case du boss de la zone 1
        if y == 15 and x == 0:
            # Boite de dialogue qui s'exécute quand on le rencontre
            boss1()
            Boss1dead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk = encounter(
                Boss1, lvl)
            argent += argent_mob
            # Si le boss est vaincu
            if Boss1dead == True:
                y -= 2  # Passage a la zone 2
                world_map(y, x, monstery, monsterx, gobliny, goblinx)
                zone2()  # Boite de dialogue qui s'exécute quand on passe a la zone 2
                sleep(1)
                pass
        # Case du boss de la zone 2
        if y == 7 and x == 14:
            # Boite de dialogue qui s'exécute quand on le rencontre
            boss2()
            Boss2dead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk = encounter(
                Boss2, lvl)
            argent += argent_mob
            # Si le boss est vaincu
            if Boss2dead == True:
                y -= 2  # Passage a la zone 3
                world_map(y, x, monstery, monsterx, gobliny, goblinx)
                zone3()  # Boite de dialogue qui s'exécute quand on passe a la zone 3
                sleep(1)
                pass
        # Case de Master Roshi
        if y == 3 and x == 14:
            # Niveau requis pour interagir avec le npc
            if niveau >= 8:
                scriptroshi2()
                sleep(1)
                master_dead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk = encounter(
                    Master_Roshi, lvl)
                # Si Master Roshi est vaincu
                if master_dead == True:
                    sleep(1)
                    scriptroshi3()  # Boite de dialogue qui s'exécute si on a battu Master Roshi
                    atk += 50  # On gagne la master sword qui boost notre attaque de 50
                    y += 1
                    world_map(y, x, monstery, monsterx, gobliny, goblinx)

            else:
                sleep(1)
                scriptroshi1()  # Boite de dialogue qui s'exécute si on n'a pas le niveau requis
                sleep(1)
                pass
        # Case du boss final (zone 3)
        if y == 0 and x == 0:
            # Choix de l'affronter ou non (préférable de ne pas le faire sans la master sword)
            script(
                "Voilà donc l'insecte qui brise le silence de ces lieux... Je me montrerai magnanime à ton égard. Je te laisse le choix de partir.")
            sleep(3)
            title = "Voulez vous partir ?"
            options = ["oui", "non"]
            choice, index = pick(
                options, title, indicator='=>', default_index=0)
            sleep(1)
            if choice == "non" or index == 1:
                finalboss2()  # Boite de dialogue qui s'exécute si on décide d'affronter le boss final
                sleep(1)
                Final_Bossdead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk = encounter(
                    Final_Boss, lvl)
                # Si le boss final est vaincu
                if Final_Bossdead == True:
                    sleep(1)
                    system("cls")  # clear de terminal
                    finalboss4()  # Boite de dialogue qui s'exécute quand on a battu le boss final
                    sleep(1)
                    system("cls")
                    postgame()  # Boite de dialogue de fin de jeu
                    sleep(2)
                    system("cls")
                    # Affichage du logo a la fin du jeu
                    script(" ▄▄▄       ███▄ ▄███▓ ███▄    █ ▓█████   ██████  ██▓ ▄▄▄      \n▒████▄    ▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒████▄    \n▒██  ▀█▄  ▓██    ▓██░▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒▒██  ▀█▄  \n░██▄▄▄▄██ ▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░░██▄▄▄▄██ \n ▓█   ▓██▒▒██▒   ░██▒▒██░   ▓██░░▒████▒▒██████▒▒░██░ ▓█   ▓██▒\n ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░\n▒   ▒▒ ░░  ░      ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░\n ░   ▒   ░      ░      ░   ░ ░    ░   ░  ░  ░   ▒ ░  ░   ▒   \n░  ░       ░            ░    ░  ░      ░   ░        ░  ░")
                    sleep(5)
                    filename, want_load = main_menu()

            else:
                pass
        else:
            # Permet de rencontrer et d'affronter des monstres random sur son chemin
            # % de chance de rencontrer un monstre sur son chemin
            Monster_Chance = Monster_Encounter()
            if Monster_Chance < 15:
                # si le % est  < a 15 on rencontre un monstre random entre 4 différents (les 4 diffèrent en fonction de la zone ou l'on est)
                monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk = encounter(
                    foe, lvl)
                # Si le monstre est vaincu
                if monsterdead == True:
                    argent += argent_mob
        # Si le joueur meurt il revient au menu principal
        if hp == 0:
            filename, want_load = main_menu()
        system('cls')
        # Actualisation de l'affichage des stats
        world_map(y, x, monstery, monsterx, gobliny, goblinx)
        print(f"Argent: {argent} or       {hp}hp / {hp_max}hp")
        print(f"Niveau: {niveau}        {exp}xp / {lvlgain}xp")
        print(f"Stats: {atk} Atk        {dfs} dfs")
        print(f"Votre inventaire: {inventaire}")


Main()
