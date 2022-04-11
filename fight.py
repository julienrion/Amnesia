from os import system
from time import sleep
from pick import pick
from random import randint
from inventory import fonction_inventory, inventaire
from menu import boss1, finalboss3
from map import Goblin, Monster, foe, Boss1, Boss2, Final_Boss, Master_Roshi
global hp, hpmonster, playerdead, monsterdead, monster_name
# Stats du joueur
hp_max = 2500
hp = 2500
exp = 0
niveau = 10
lvlgain = 100
atk = 25
dfs = 5
agi = 5
strike = 1
playerdead = False
monster_name = None

# Fonction pour calculer les chances de coup critique ainsi que les chances d'esquive


def attack(atk, agi, agimonster, strike):
    chancecrit = randint(0, 10)
    if chancecrit <= agi:
        crit = 1
    else:
        crit = 0
    randhit = 1
    if crit == 1:
        strike = (atk*2)*randhit
    else:
        strike = atk*randhit
    dodgechance = randint(1, 20)
    if dodgechance <= agimonster:
        strike = 0
        print("Vous n'êtes pas assez rapide et manquez votre attaque ! ")
        input("Appuyez sur Entrer pour continuer...")
    else:
        strike = strike
    return strike

# Fonction pour calculer les chances de coup critique ainsi que les chances d'esquive pour le monstre


def attackmonster(atkmonster, agi, agimonster, strikemonster):
    chancecrit = randint(0, 10)
    if chancecrit <= agimonster:
        crit = 1
    else:
        crit = 0
    randhit = 1
    if crit == 1:
        strikemonster = (atkmonster*2)*randhit
    else:
        strikemonster = atkmonster*randhit
    dodgechance = randint(1, 20)
    if dodgechance <= agi:
        strikemonster = 0
        print("Vous êtes assez rapide et esquivez l'attaque de peu")
        input("Appuyez sur Entrer pour continuer...")
        system("cls")
    else:
        strikemonster = strikemonster
    return strikemonster


# Décompte des hp et indique si le monstre est mort ou pas


def hpcount(strike, strikemonster, enemy):
    global hp, hpmonster, playerdead, monsterdead, adversary, Boss1dead, Boss2dead, Final_Bossdead, atkmonster, dfsmonster, if_low, master_dead

    if hp > 0 and hpmonster > 0:
        if agi >= agimonster:
            armormonster = dfsmonster
            strike = strike - armormonster
            if strike < 0:
                strike = 0
            hpmonster = hpmonster - strike
            sleep(1)
            print("Vous avez infligé", strike,
                  "Pts de dégâts au", monster_name, " ! ")
            armor = dfs
            strikemonster = strikemonster - armor
            if strikemonster < 0:
                strikemonster = 0
            hp = hp - strikemonster
            sleep(1)
            print("Le", monster_name, "Vous a infligé",
                  strikemonster, "Pts de dégats ! ")
            input("Appuyez sur Entrer pour continuer...")
            system("cls")
        else:
            armor = dfs
            strikemonster = strikemonster - armor
            if strikemonster < 0:
                strikemonster = 0
            hp = hp - strikemonster
            sleep(1)
            print("Le", monster_name, "Vous a infligé",
                  strikemonster, "Pts de dégats ! ")
            input("Appuyez sur Entrer pour continuer...")
            system("cls")
            armormonster = dfsmonster
            strike = strike - armormonster
            if strike < 0:
                strike = 0
            hpmonster = hpmonster - strike
            sleep(1)
            print("Vous avez infligé", strike,
                  "Pts de dégâts au", monster_name, " ! ")
    if hp <= 0:
        hp = 0
        playerdead = True
        return (hp, hpmonster, playerdead, monsterdead)
    # Pour le boss final si il passe sous les 400 pv
    elif hpmonster < 400 and if_low == 0:
        if monster_name == "Horreur mystique":
            finalboss3()  # Boite de dialogue qui s'exécute quand le boss final est en dessous de 400 pv
            # Buff des stats du boss final
            atkmonster += 15
            dfsmonster += 15
        if_low += 1  # Variable permettant de répeter la boucle qu'une seule fois
    # Tout les return en fonction du type de monstre (return des valeurs différentes en fonction du monstre)
    elif hpmonster < 0:
        if monster_name == "Lézard géant":
            hpmonster = 0
            Boss1dead = True
            return (hp, hpmonster, playerdead, Boss1dead)
        if monster_name == "Paladin fantôme":
            hpmonster = 0
            Boss2dead = True
            return (hp, hpmonster, playerdead, Boss2dead)

        if monster_name == "Master Roshi":
            hpmonster = 0
            master_dead = True
            return (hp, hpmonster, playerdead, master_dead)

        if monster_name == "Horreur mystique":
            hpmonster = 0
            Final_Bossdead = True
            return (hp, hpmonster, playerdead, Final_Bossdead)
        else:
            hpmonster = 0
            monsterdead = True
            return (hp, hpmonster, playerdead, monsterdead)

    return (hp, hpmonster, playerdead, monsterdead)

# Fonction d'attaque pour un round


def attaquer(strike, strikemonster, atk, agi, agimonster, enemy):
    strike = attack(atk, agi, agimonster, strike)
    strikemonster = attackmonster(atkmonster, agi, agimonster, strikemonster)
    hp, hpmonster, playerdead, monsterdead = hpcount(
        strike, strikemonster, enemy)

# Fonction de combat


def fight(enemy, strike, strikemonster, atk, agi, agimonster):
    global hp
    global hpmonster, if_low
    if_low = 0
    print("Vous faîtes face au", monster_name, "sauvage !")

    # Boucle de combat

    while hp > 0 and hpmonster > 0:
        print("PV du ", monster_name, "sauvage : ", hpmonster, "PV")
        print("Il vous reste actuellement", hp, "Points de vie.")
        title2 = f"Vous affrontez {monster_name} \n Il vous reste {hp} HP \n Que voulez-vous faire ?"
        options2 = ["Attaquer", "Inventaire", "Fuir"]

        # Menu de selection d'action

        fight1, index = pick(options2, title2, indicator='=>', default_index=0)
        # Si on veut attaquer
        if fight1 == "attaquer" or index == 0:
            attaquer(strike, strikemonster, atk, agi, agimonster, enemy)
        # Si on veut ouvrir l'inventaire
        elif fight1 == "inventaire" or index == 1:

            # Ouverture de l'inventaire

            used, hp, hpmonster = fonction_inventory(
                inventaire, hp, hp_max, atk, hpmonster)
            if used == True:
                strikemonster = attackmonster(
                    atkmonster, agi, agimonster, strikemonster)
                hp, hpmonster, playerdead, monsterdead = hpcount(
                    strike, strikemonster, enemy)

            pass
        # Si on veut fuir
        elif fight1 == "fuir" or index == 2:
            # On empêche la fuite pour les boss
            if enemy != (Goblin, Monster, Boss1, Boss2, Final_Boss, Master_Roshi):
                chance_fly = randint(0, 4)
                # Sur les monstres normaux on a un % de chance que la fuite ne marche pas
                if chance_fly < 2:
                    title2 = f"Vous affrontez {monster_name} \n Il vous reste {hp} HP \n Que voulez-vous faire ? Vous n'avez pas réussi à fuir! 😹"
                    strikemonster = attackmonster(
                        atkmonster, agi, agimonster, strikemonster)
                    hp, hpmonster, playerdead, monsterdead = hpcount(
                        strike, strikemonster, enemy)
                else:
                    # Si la fuite est réussie
                    system('cls')
                    print(f"Vous parvenez a fuir {monster_name} ")
                    sleep(1.5)
                    break
            else:
                # Si on essaye de fuire un boss (l'affichage se réinitialise d'elle même ligne 190 on ne voit le texte qu'un cours instant)
                chance_fly = 0
                if chance_fly < 2:
                    title2 = f"Vous affrontez {monster_name} \n Il vous reste {hp} HP \n Que voulez-vous faire ? Vous ne pouvez pas fuir un boss! 😹"
                else:
                    break
# Fonction qui gère le gain d'exp et le lvlup


def exp_gain(hp, hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain):
    global gain
    if adversary == foe:
        if lvl == 1:
            gain = randint(40, 50)
        if lvl == 2:
            gain = randint(50, 110)
        if lvl == 3:
            gain = randint(150, 210)
    elif adversary == Goblin:
        gain = randint(25, 45)
    elif adversary == Monster:
        gain = randint(500, 800)
    elif adversary == Boss1:
        gain = randint(250, 300)
    elif adversary == Boss2:
        gain = randint(500, 800)
    elif adversary == Master_Roshi:
        gain = randint(1000, 1001)
    elif adversary == Final_Boss:
        gain = randint(1, 2)

    exp += gain
    # Tant que l'exp est supérieure au nombre d'exp nécessaire pour monter de niveau la boucle continue
    while exp >= lvlgain:
        niveau += 1
        exp -= lvlgain
        lvlgain = round(lvlgain * 1.5)
        title = f"Vous avez gagné un niveau, vous êtes niveau {niveau} quelle statistique souhaitez vous augmenter ?"
        options = ["Vie", "Attaque", "Défense"]
        # Menu pour choisir quelle stat augmenter
        choix_up, index = pick(options, title, indicator='=>', default_index=0)
        if index == 0:
            hp_max += 10
        elif index == 1:
            atk += 4
        elif index == 2:
            dfs += 4
        hp_max += 10  # On augemente les hp max a chaque montée de niveau
        hp = hp_max  # On soigne le joueur apres une montée de niveau
    return hp, hp_max, exp, niveau, atk, dfs, lvlgain

# Fonction pour rencontrer un monstre


def encounter(adversary, lvl):
    global hp, hpmonster, playerdead, monsterdead, atkmonster, dfsmonster, agimonster, monster_name, atk, agi, dfs, exp, niveau, hp_max, Boss1dead, Boss2dead, Final_Bossdead, lvlgain, master_dead, argent_mob
    Boss1dead = False
    Boss2dead = False
    master_dead = False
    Final_Bossdead = False
    # On définit les stats de chaque monstre
    # La variable lvl correspond a la zone (lvl=1 ---> zone1)
    if adversary == foe:
        if lvl == 1:
            foes_name = ['Lutin', 'Fungus',
                         'Gluant', 'Rapace']
            monster_name = foes_name[randint(0, 3)]
            hpmonster = 50
            atkmonster = 10
            dfsmonster = 2
            agimonster = 5
            strikemonster = 1
            monsterdead = False
            argent_mob = randint(5, 10)
        if lvl == 2:
            foes_name2 = ['Chimère', 'Troll',
                          ' Mort-vivant', 'Spectre']
            monster_name = foes_name2[randint(0, 3)]
            hpmonster = 150
            atkmonster = 15
            dfsmonster = 3
            agimonster = 5
            strikemonster = 1
            monsterdead = False
            argent_mob = randint(10, 20)
        if lvl == 3:
            foes_name3 = ['Golem', 'Vampire',
                          'Dragon', 'Executeur']
            monster_name = foes_name3[randint(0, 3)]
            hpmonster = 250
            atkmonster = 20
            dfsmonster = 5
            agimonster = 5
            strikemonster = 1
            monsterdead = False
            argent_mob = randint(20, 30)

    if adversary == Goblin:
        monster_name = "Goblin"
        hpmonster = 100
        atkmonster = 10
        dfsmonster = 2
        agimonster = 10
        strikemonster = 1
        monsterdead = False

    if adversary == Monster:
        monster_name = "Monster"
        hpmonster = 400
        atkmonster = 25
        dfsmonster = 10
        agimonster = 5
        strikemonster = 1
        monsterdead = False
        argent_mob = randint(40, 50)

    if adversary == Boss1:
        monster_name = "Lézard géant"
        hpmonster = 250
        atkmonster = 20
        dfsmonster = 10
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        argent_mob = randint(20, 30)

    if adversary == Boss2:
        monster_name = "Paladin fantôme"
        hpmonster = 500
        atkmonster = 30
        dfsmonster = 15
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        argent_mob = randint(50, 60)

    if adversary == Master_Roshi:
        monster_name = "Master Roshi"
        hpmonster = 650
        atkmonster = 30
        dfsmonster = 15
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        argent_mob = 0

    if adversary == Final_Boss:
        monster_name = "Horreur mystique"
        hpmonster = 800
        atkmonster = 35
        dfsmonster = 15
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        argent_mob = 0
    # Menu d'option quand on rencontre un monstre
    title = f"Vous rencontrez un {monster_name} 🙀 \n Que voulez-vous faire ?"
    options = ["Attaquer", "Fuir"]
    choix, index = pick(options, title, indicator='=>', default_index=0)

    system("cls")
    # 2eme boucle de combat
    while playerdead != True or monsterdead != True:
        # Si on attaque
        if choix == "attaquer" or index == 0:
            fight(adversary, strike, strikemonster, atk, agi, agimonster)
            # Si le monstre est mort (conditions différentes en fonction du monstre)
            if monsterdead == True:
                system("cls")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp, hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp, hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)

                print(f"Vous avez gagné {exp}/{lvlgain}xp")
                print(f"Vous êtes niveau {niveau}")
                print(f"Le monstre vous a donné {argent_mob} or")
                print(atk)
                waiting = input("Appuyez sur Entrer pour continuer...")
                if waiting == "":
                    system("cls")
                return monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk
            if Boss1dead == True:
                system("cls")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp, hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp, hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)
                print(f"Vous avez gagné {exp}/{lvlgain}xp")
                print(f"Vous êtes niveau {niveau}")
                waiting = input("Appuyez sur Entrer pour continuer...")
                if waiting == "":
                    system("cls")
                return Boss1dead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk
            if Boss2dead == True:
                system("cls")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp, hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp, hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)
                print(f"Vous avez gagné {exp}/{lvlgain}xp")
                print(f"Vous êtes niveau {niveau}")
                waiting = input("Appuyez sur Entrer pour continuer...")
                if waiting == "":
                    system("cls")
                return Boss2dead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk

            if master_dead == True:
                system("cls")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp, hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp, hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)
                print(f"Vous avez gagné {exp}/{lvlgain}xp")
                print(f"Vous êtes niveau {niveau}")
                waiting = input("Appuyez sur Entrer pour continuer...")
                if waiting == "":
                    system("cls")
                return master_dead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk

            if Final_Bossdead == True:
                system("cls")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp, hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp, hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)
                print(f"Vous avez gagné {exp}/{lvlgain}xp")
                print(f"Vous êtes niveau {niveau}")
                waiting = input("Appuyez sur Entrer pour continuer...")
                if waiting == "":
                    system("cls")
                return Final_Bossdead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk
            # Si le joueur est mort
            if playerdead == True:
                system("cls")
                # Ascii game over
                print(""" .88888. \nd8'   `88 \n88        .d8888b. 88d8b.d8b. .d8888b.    .d8888b. dP   .dP .d8888b. 88d888b. \n88   YP88 88'  `88 88'`88'`88 88ooood8    88'  `88 88   d8' 88ooood8 88'  `88 \nY8.   .88 88.  .88 88  88  88 88.  ...    88.  .88 88 .88'  88.  ... 88\n `88888'  `88888P8 dP  dP  dP `88888P'    `88888P' 8888P'   `88888P' dP   \n\n\n""")

                print("Vous avez été vaincu par le ",
                      monster_name, "sauvage !")
                waiting = input("Appuyez sur Entrer pour continuer...")
                if waiting == "":
                    system("cls")
                return playerdead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk
        if choix == "fuir" or index == 0:
            monsterdead == False
            argent_mob == 0
            return monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk
        else:
            # Si on fuit le monstre
            system("cls")
            print("Il vous reste", hp, "Points de vie")
            print(f"Vous avez fui {monster_name}")
            waiting = input("Appuyez sur Entrer pour continuer...")
            if waiting == "":
                system("cls")
            return monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain, atk
