# Permet de choisir avec une flèche plutôt que de devoir écrire le mot de l'item /l'action voulu
from pick import pick


inventaire = ['Potion +']

# On vérifie si l'objet choisi est un objet de soin (potion) en comparant avec la liste des objets de soin du jeu


def objet_soin_verif(choice, L_objet_soin):
    j = 0
    while j < len(L_objet_soin):
        if choice == L_objet_soin[j]:
            return j
        else:
            j += 1
    return "non"

# On vérifie si l'objet choisi est un objet offensif (bombe) en comparant avec la liste des objets offensifs du jeu


def objet_arme_verif(choice, L_objet_arme):
    l = 0
    while l < len(L_objet_arme):
        if choice == L_objet_arme[l]:
            return l
        else:
            l += 1
    return "non"

# Fonction qui servait à vérifier si l'objet écrit par l'utilisateur fait bien partie de l'inventaire


def objet_inventaire_verif(choice, inventory):
    index = 0
    while index < len(inventory):
        if choice == inventory[index]:
            return True, index
        else:
            index += 1
    return False


def fonction_inventory(inventory, hp, hp_max, atk, hpmonster):
    # Liste de tous les objets de soin du jeu
    L_objet_soin = ["Potion", "Potion +", "Potion X"]
    L_heal_value = [50, 70, 150]
    # Liste de tous les objets offensifs du jeu
    L_objet_arme = ["Bombe", "Explo-bombe"]
    L_arme_value = [80, 150]
    used = False  # Permet d'indiquer que rien n'est utilisé pour pouvoir quitter l'inventaire sans passer un tour lors d'un combat
    title = f"Choisissez un objet ou quittez l'inventaire en choisissant 'quitter': \n Vous avez {hp}hp/{hp_max}hp"
    options = []
    for i in range(len(inventory)):
        options.append(inventory[i])
    options.append("quitter")
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    while choice != "quitter":  # Permet de rester dans l'inventaire tant que l'option "quitter" n'est pas sélectionnée
        i, position = objet_inventaire_verif(choice, inventory)
        if i == True:
            # Vérifie si l'objet est un objet de soin ou non
            j = objet_soin_verif(choice, L_objet_soin)
            if j != "non":  # Si la réponse est différente de "non", alors l'objet est bien un objet de soin
                if hp == hp_max:  # On vérifie si le niveau des hp est déjà au maximum pour ne pas gacher de potion par erreur
                    title = f"Choisissez un objet ou quittez l'inventaire en choisissant 'quitter': \nVous avez {hp}hp/{hp_max}hp \nVous ne pouvez pas utiliser cet item, vos hp sont déjà au maximum."
                    pass
                else:  # On s'assure du choix du joueur
                    print("Voulez-vous utiliser l'objet de soin '",
                          inventory[position], "' ?")
                    print("Vous avez", hp, "/", hp_max, "hp.")
                    print("cet objet heal",
                          L_heal_value[j], "hp, voulez-vous l'utiliser ?")
                    title2 = f"Voulez-vous utiliser l'objet de soin {inventory[position]} ?"
                    options2 = ["oui", "non"]
                    choice2, index = pick(
                        options2, title2, indicator='=>', default_index=0)
                    # Si le joueur accepte d'utiliser la potion, on ajoute à sa vie les hp selon la potion utilisée grâce à j qui sera égal à 0, 1 ou 2, ce qui correspond à 50, 70 ou 150 dans la liste l_heal_value ( heal par chaque potion)
                    if choice2 == "oui":
                        hp_heal = L_heal_value[j]
                        hp += hp_heal
                        inventory.remove(choice)
                        options.remove(choice)
                        # Permet de ne pas dépasser nos hp maximum, si la potion heal plus que ce qu'il manque de vie, nos hp sont juste mis au maximum (ex:100/100 au lieu de 120/100)
                        if hp_max < hp:
                            hp = hp_max
                        title = f"Choisissez un objet ou quittez l'inventaire en choisissant 'quitter': \nVous avez {hp}/{hp_max}hp \n-> {choice} utilisée"
                        used = True
                        return used, hp, hpmonster
                    else:
                        pass
            # Vérifie si l'objet est un objet offensif ou non
            l = objet_arme_verif(choice, L_objet_arme)
            if l != "non":  # Si la réponse est différente de "non", alors l'objet est bien un objet offensif. Puis on vérifie si le joueur est sûr de vouloir utiliser l'objet choisi
                print("Vos dégâts sont de", atk, ".")
                title2 = f"Voulez utiliser l'objet {choice} qui infligera {L_arme_value[l]} dégats?"
                options2 = ["oui", "non"]
                choice_arme, index = pick(
                    options2, title2, indicator='=>', default_index=0)
                if choice_arme == "non":
                    pass
                if choice_arme == "oui":  # Si le joueur choisit d'utiliser l'objet offensif, les dégâts de l'objet seront déduits de la vie du monstre
                    hpmonster -= L_arme_value[l]
                    inventory.remove(choice)
                    options.remove(choice)
                    used = True  # Permet d'indiquer qu'un objet a été utilisé et fait passer notre tour lors d'un combat
                    return used, hp, hpmonster

            if j == "non" and l == "non":  # Permettait d'indiquer si un objet n'était ni un objet de soin ni un objet offensif, donc inutilisable en combat
                print("Objet", choice, "non utilisable.")

        if used == True:  # Si un objet est utilisé, on quitte l'inventaire sans avoir besoin de choisir "quitter" ce qui fait sortir de la fonction et permet de continuer le combat
            break
        choice, index = pick(
            options, title, indicator='=>', default_index=0)
    return used, hp, hpmonster
