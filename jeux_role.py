"""
Jeux de rôle :

- Un joueur
- PNJ

Joueur :
- Dispose de 3 potions (récupération aleatoire entre 15 et 50 pdv)
- Attaque aléatoire entre 5 et 10 pdv
- Dispose de 50 pdv
- 2 choix : potion ou attaque (action unique par tour)

Enemie :
- Aucune potion
- Attaque aleatoire entre 5 et 15 pdv
- Dispose de 50 pdv

Général :
- Le joueur attaque toujours en premier
- A la fin du tour affiche les pdv & potions du joueur pdv et de l'enemie
- Le jeu s'arrete lorsque le joueur ou l'enemie n'a plus de pdv
"""

import random

player = 50
player_potion = 3
pnj = 50
# player_attack = random.randint(5, 10)
# pnj_attack = random.randint(5, 10)
# potion_pdv = random.randint(15, 50)

print("Bienvenue dans le jeu de role")

while True:
    print("Choississez une option :")
    print("1. Attaquer")
    print("2. Prendre un potion")

    user_choice = input("Votre choix d'option : ")

    if player <= 0 :
        print("Vous êtres MORT !")
        break

    elif pnj <= 0 :
        print("Vous avez gagné me combat ! L'enemie est MORT !!!")
        break

    if user_choice == "1":
        player_attack = random.randint(5, 10)
        print(f"Vous attaquez !!! L'enemie perd {player_attack} points de vie")
        pnj = pnj - player_attack
        print(f"Il reste {pnj} points de vie à l'enemie")
        pnj_attack = random.randint(5, 15)
        print(f"L'enemie attaque !!! Vous perdez {pnj_attack} points de vie")
        player = player - pnj_attack
        print(f"il vous reste {player} points de vie")

    elif user_choice == "2":
        if player_potion <= 0 :
            print("Désolé, vous n'avez plus de potion")
        else:
            potion_pdv = random.randint(15, 50)
            print(f"Vous prenez une potion qui régénére {potion_pdv} points de vie")
            player = player + potion_pdv
            if player > 50:
                player = 50
            print(f"Vous avez maintenant {player} point de vie")
            pnj_attack = random.randint(5, 15)
            print(f"L'enemie attaque !!! Vous perdez {pnj_attack} points de vie")
            player = player - pnj_attack
            print(f"Il vous reste {player} points de vie")
            player_potion = player_potion - 1
            print(f"Il vous reste {player_potion} potion(s)")

