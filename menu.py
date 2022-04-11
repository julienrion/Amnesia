# Permet d'executer une commande systeme
from os import system
# Permet de choisir avec une flèche plutôt que de devoir écrire le mot de l'item /l'action voulue
from time import sleep
# Permet d'utiliser les fonctions systeme
import sys
# Permet d'effectuer un temps d'arrêt dans le code
from pick import pick
from save import load
global filename, want_load

# Le menu principal


def main_menu():
    want_load = False
    # Titre du jeu
    title = script_title(" ▄▄▄       ███▄ ▄███▓ ███▄    █ ▓█████   ██████  ██▓ ▄▄▄      \n▒████▄    ▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒████▄    \n▒██  ▀█▄  ▓██    ▓██░▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒▒██  ▀█▄  \n░██▄▄▄▄██ ▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░░██▄▄▄▄██ \n ▓█   ▓██▒▒██▒   ░██▒▒██░   ▓██░░▒████▒▒██████▒▒░██░ ▓█   ▓██▒\n ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░\n▒   ▒▒ ░░  ░      ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░\n ░   ▒   ░      ░      ░   ░ ░    ░   ░  ░  ░   ▒ ░  ░   ▒   \n░  ░       ░            ░    ░  ░      ░   ░        ░  ░\n\n")
    sleep(2)
    options = ["Nouvelle partie", "Charger une partie",
               "Règles", "Credits", "quitter"]
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    # Si on commence une nouvelle partie
    if index == 0:
        print("Le jeu va commencer ! \n")
        sleep(1)
        create_character()  # Creation du personnage
        input("\nAppuyez sur Entrer pour continuer")
        system('cls')  # Clear de terminal
        game_start()  # Départ du dialogue qui nous raconte l'histoire
        input("\nAppuyez sur Entrer pour continuer")
        system('cls')
        zone1()  # Description de la zone 1
        input("\nAppuyez sur Entrer pour continuer")
        system('cls')
        sleep(2)
        return "pass", want_load
    # Si on charge une nouvelle partie
    elif index == 1:
        filename, want_load = new_game()
        print(f"Votre partie {filename} est en cours de chargement")
        return filename, want_load
    # Si on veut voir les règles
    elif index == 2:
        print("\n Règles : \n \n Le jeu prendra place dans la première des trois zones de l'univers. \n Il s'agit d'un tour par tour classique dans lequel vous devrez vous confronter à différents monstres dans le but de vous frayer \n un chemin jusqu'à l'antagoniste. \n \n Avant d'y parvenir, vous trouverez sur votre route différents objets et personnages qui vous aideront à poursuivre votre quête. \n  \n Bon courage, aventurier!")
        sleep(15)
        main_menu()
    # Si on veut afficher les credits
    elif index == 3:
        print("Credits : Jeu créé par Baptiste Verdier , Fabien Renoir , Julien Rion , Sandie Ouallet et Thierry Maignan.")
        sleep(10)
        main_menu()
    # Si on veut directement quitter le programme
    elif index == 4:
        system('cls')
        sys.exit()

    return index

# Fonction qui permet de charger une ancienne partie


def new_game():
    global filename, want_load
    print("Quelle partie souhaitez-vous charger? (filename)")
    filename = input()
    want_load = True  # Si on charge la partie la variable devient True
    return filename, want_load

# Fonction qui permet de créer son personnage


def create_character():
    global player_name
    print("Bienvenue aventurier, comment vous appelez-vous?\n")
    player_name = input()
    print("\nFort bien", player_name,
          ", que les cieux vous donnent la force de faire face à votre destin...")
    return player_name

# script permettant d'afficher un texte lettre par lettre


def script(str):

    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == ".":
            sleep(0.5)
        else:
            sleep(0.04)

# script permettant d'afficher un texte lettre par lettre mais pour le titre en ascii


def script_title(str):

    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.005)

# Toutes les boites de dialogue du jeu !


def shopkeeper1():

    script("\nBonjour, je suis un modeste marchand égaré. Si vous veniez à m'acheter quoi que ce soit, cela pourrait probablement m'aider à repartir... Ce coin est trop étrange pour moi.\n \nBienvenue.\n")


def shopkeeper2():

    script("\nAh, vous revoilà... J'ai bien peur que s'enfoncer dans cet endroit ne soit pas le meilleur moyen pour tenter de m'extraire de mes problèmes. Malheureusement, je n'ai pas vu une quelconque autre sortie dans les parages...\n \nQue puis-je faire pour vous?\n")


def shopkeeper3():

    script("\nBonjour, jeune aventurier.\nJe me rends compte que vous êtes probablement ma meilleure chance de partir d'ici.\nJe compte sur vous.\n \nDites-moi comment je peux vous aider.\n")


def game_start():

    script("\nVous vous réveillez dans un paysage inconnu.\nUn visage étranger vous demande : \n \n- Vous allez bien ? Ca fait un moment que vous êtes là.\nConscient de la nature étrange de la situation, vous frottez vos paupières pour découvrir la lumière blafarde du paysage vous entourant, qui se trouve être une brume épaisse. \n \nVous cherchez autour de vous, mais impossible de retrouver la personne qui vous parlait. \n \nCe paysage inhabituel vous intrigue et quelque chose semble briller au loin... \n \nEt si vous alliez y jeter un coup d'oeil?\n")


def zone1():

    script("\nVous vous approchez de la lueur suspecte en vous enfonçant dans l'épaisse brume, et celle-ci se ternit au fur et à mesure que vous avancez.\nVous vous baissez pour voir de quoi il s'agit...\n \nVous voilà l'heureux propriétaire d'une potion!\n \nEn vous relevant, vous constatez que la brume est désormais presque palpable et vous empêche de voir même à moyenne distance. \n \nFrayez-vous un chemin pour en apprendre plus sur cet endroit.\n")


def zone2():

    script("\nAprès cette dure épreuve, vous voyez le paysage en face de vous se dégager.\nToujours à la recherche de l'homme qui vous a parlé plus tôt, la brume laisse petit à petit place aux arbres. \nPoursuivez votre chemin, et vos questions trouveront éventuellement des réponses...\n")


def zone3():

    script("\nVous vous frayez un chemin en laissant derrière vous la dépouille de l’atroce bête.\n \nEn avançant, vous avez l'impression d'apercevoir au loin une silhouette humaine voire amicale...\n \nSerait-ce enfin là la personne que vous recherchiez?\n")


def scriptroshi1():

    script("\nVous êtes donc parvenu jusqu'ici, félicitations. \nVous méritez des explications sur ce qui vous arrive et je m'excuse de ne pas vous en avoir offert plus tôt. \nCependant, il en va de ma responsabilité de ne pas vous laisser aller plus loin...\n \nCe qui se cache là-bas n'est en rien comparable avec ce que vous avez connu auparavant.\n \nRevenez me voir lorsque vous serez plus fort.\n")


def scriptroshi2():

    script(
        f"\nVous revoilà...\n \nJe préfèrerais directement vous sommer de mettre un terme à votre entreprise.\n \nMalheureusement, je connais la soif inextinguible de l'esprit et la faiblesse de l'Homme. \nSi je ne vous arrêterai pas, je souhaiterais au moins m'assurer que vous avez les épaules assez larges pour faire face à ce qui vous attend..\n \nEn garde,{player_name}, prouvez-moi votre valeur!")


def scriptroshi3():

    script(
        f"\nAlors c'est ainsi...\n \nVous dépassez de loin tout ce que j'ai pu imaginer. \nJ'ai été victime de mon ignorance alors même que je souhaitais vous protéger du haut de mon illusoire sagesse, quelle arrogance, quelle ironie!\n \n{player_name},vous avez toutes mes excuses et ma sympathie. \nJe vous en prie, prenez ceci...\n \n - Vous avez obtenu l'Epée légendaire.\n \nCela devrait vous permettre de voir le bout de cet affreux rêve. Allez la ou je n'ai jamais pu, brisez le sort... Bon courage.\n")


def finalboss2():

    script("\nPauvre fou... Ton orgueil te mènera à ta perte. Je suis le maître de ce rêve et personne n'en sortira jamais. Au moins, tâche de me divertir, maintenant que tu es la.\n")


def finalboss3():
    script("\nTu te débrouilles bien pour un cafard, mais personne ne sortira jamais d'ici. \nNous avons assez joué. \nTa stupide épée ne te mènera nulle part. \nTu vas retrouver le sommeil pour l'éternité.\n")


def finalboss4():

    script("\nTout ça à cause d'une misérable épée... \nTu peux brûler en enfer misérable insecte... \nJ'irai même jusque là-bas pour te retrouver.\n \nLe jour ou je te mettrai à nouveau la main dessus, tu auras l'impression que ce que tu as vécu aujourd'hui n’était qu’un doux rêve à côté...\n")


def boss1():

    script("\nVous apercevez quelque chose approcher rapidement de vous en zigzaguant et tout d’un coup s’élève: \n \n- Vous avancez et abattez vos problèmes, qui sont également mes amis...\n Je vais faire de vous le repas que vous auriez du être depuis déjà longtemps.\n ")


def boss2():

    script("\nVous voyez une masse humanoïde s'approcher de vous dans un corps en armure mais... Sans tête?\n \n- Je n'éprouve personnellement aucune rancune au vu de toutes les créatures que vous avez tuées pour vous rendre jusqu'ici.\n \nCependant, je dois vous arrêter ici pour protéger celui qui m'a offert ma rédemption.\n")


def postgame():

    script("\nPour la première fois depuis longtemps, vous semblez vous sentir bien. Epuisé, mais en paix.\nVous ouvrez les yeux et faites enfin face à un paysage familier...\n \n- . . .\n \nIl s'agit bien de votre plafond. Ou aviez-vous la tête?\n \n7h30 affiche le réveil à votre chevet. . . \n\nIl faut se dépêcher, vous avez cours à Hetic!\n")