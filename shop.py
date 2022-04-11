# Permet de choisir avec une flèche plutôt que de devoir écrire le mot de l'item /l'action voulue
from pick import pick


def fonction_shop(inventaire, argent, liste_item, liste_prix):
    global result

    title = f"\n Bienvenue dans le magasin, que souhaitez vous faire ? \n Vous avez {argent} or"
    print("Inventaire:", inventaire)
    print("Argent:", argent, "\n")
    options = ["Acheter", "Vendre", "Quitter"]

    choice_action, index = pick(
        options, title, indicator='=>', default_index=0)
    # Permet de rester dans le shop jusqu'à ce qu'on ait effectué nos achats/ventes
    while choice_action != "quitter" or index == 2:
        # Lance le mode achat du shop si le joueur souhaite acheter des items
        if choice_action == "acheter" or index == 0:
            result = fonction_achat(inventaire, argent, liste_item, liste_prix)
            title = f"\n Bienvenue dans le magasin, que souhaitez vous faire ? \n Vous avez {result[1]} or"
            argent = result[1]
        # Lance le mode achat du shop si le joueur souhaite vendre des items
        elif choice_action == "vendre" or index == 1:
            result = fonction_vente(inventaire, argent, result[2])
            title = f"\n Bienvenue dans le magasin, que souhaitez vous faire ? \n Vous avez {result[1]} or"
            argent = result[1]
        # Permet de sortir du shop
        if choice_action == "quitter" or index == 2:
            break
        choice_action, index = pick(
            options, title, indicator='=>', default_index=0)

    return inventaire, argent


# Fonction qui servait à vérifier que l'item écrit par l'utilisateur faisait bien partie des objets en vente / des objets dans son inventaire
def verif_item(choice, liste):
    i = 0
    while i < len(liste):
        if choice == liste[i]:
            return i
        else:
            i += 1
    return "non"


def fonction_achat(inventaire, argent, liste_item, liste_prix):
    credit = []
    title = f"Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' : \n Vous avez {argent} or"
    options = []
    for i in range(len(liste_item)):
        options.append(liste_item[i])
    options.append("quitter")
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    # Permet de rester dans le mode achat et donc d'effectuer plusieurs achats à la suite
    while choice != "quitter":
        # Vérifie si l'item choisi est bien en vente dans le shop (servait sans la librairy 'pick')
        i = verif_item(choice, liste_item)
        # Si réponse est différente de non, alors l'item est bien dans le shop on peut l'acheter (servait sans la librairy 'pick')
        if i != "non":
            # On vérifie si le joueur a assez d'argent pour acheter l'objet, si oui on demande au joueur si il est sur
            if argent >= liste_prix[i]:
                title2 = f"Vous avez {argent}  or. \n L'objet {liste_item[i]} coûte {liste_prix[i]}  or \n voulez-vous l'acheter ?"
                options2 = ["oui", "non"]
                choice2, index = pick(
                    options2, title2, indicator='=>', default_index=0)
                # Si le joueur veut acheter l'objet, on lui enlève de l'argent en fonction du prix de l'objet et on l'ajoute à son inventaire
                if choice2 == "oui":
                    inventaire.append(liste_item[i])
                    argent -= liste_prix[i]
                    credit.append(liste_prix[i])
                    title = f"Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' :\n --> paiement effectué, merci de votre achat ! \n Vous avez {argent} or"
                if choice2 == "non":
                    pass
            else:
                # Si le joueur n'a pas assez d'argent :
                title = f"Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' :\n Vous avez {argent} or \n L'objet {liste_item[i]} coûte {liste_prix[i]}  or \n Vous n'avez pas assez d'argent pour acheter cet objet."
        choice, index = pick(
            options, title, indicator='=>', default_index=0)

    return inventaire, argent, credit


def fonction_vente(inventaire, argent, credit):
    title = f"Quel objet souhaitez-vous vendre ? Choisissez 'quitter' pour quitter le mode vente: \n Vous avez {argent} or"
    options = []
    for i in range(len(inventaire)):
        options.append(inventaire[i])
    options.append("quitter")
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    # Permet de rester dans le mode vente et donc d'effectuer plusieurs ventes à la suite
    while choice != "quitter":
        # Vérifie si l'item choisi est bien dans notre inventaire (servait sans la librairy 'pick')
        i = verif_item(choice, inventaire)
        # Si réponse est différente de non, alors l'item est bien dans notre inventaire, on peut le vendre (servait sans la librairy 'pick') puis on vérifie si le joueur est sûr de vouloir vendre l'objet
        if i != "non":
            title2 = "Êtes-vous sûr de vouloir vendre cet objet, oui ou non ?"
            options2 = ["oui", "non"]
            choice_answer, index = pick(
                options2, title2, indicator='=>', default_index=0)
            # Si le joueur veut vendre l'objet choisi, on l'enlève de son inventaire et on lui donne de l'argent
            if choice_answer == "oui":
                argent += credit[i]
                credit.remove(credit[i])
                inventaire.remove(inventaire[i])
                options.remove(options[i])
                title = f"Quel objet souhaitez-vous vendre ? Choisissez 'quitter' pour quitter le mode vente: \n Vous avez {argent} or"
            if choice_answer == "non":
                pass
        choice, index = pick(
            options, title, indicator='=>', default_index=0)

    return inventaire, argent
