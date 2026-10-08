
from partie_c import mots, choisir_mot, masque

def jouer_pendu(mot):
    """
    Lance une partie du Pendu avec un maximum de 7 erreurs.

    Paramètres :
        mot (str) : Mot que le joueur doit deviner.

    Retour :
        str : Message de victoire ou de défaite.
    """
    mot = mot.upper()  # Conversion en majuscules
    mot_masque = masque(mot)  # Création du masque
    erreurs = 0  # Compteur d'erreurs
    lettres_proposees = []  # Historique des lettres

    dessins = [
        "",
        " O",
        " O\n |",
        " O\n/|",
        " O\n/|\\",
        " O\n/|\\\n/",
        " O\n/|\\\n/ \\",
        " |----\n O\n/|\\\n/ \\"
    ]  # Dessins correspondant aux 0 à 7 erreurs

    print("\nBienvenue dans le jeu du Pendu !")

    while erreurs < 7 and "_" in mot_masque:  # Conditions de fin du jeu
        print("\nMot :", " ".join(mot_masque))  # Affichage du mot masqué
        print(f"Erreurs : {erreurs}/7")  # Affichage des erreurs
        print("Lettres proposées :", ", ".join(lettres_proposees))
        print(dessins[erreurs])  # Affichage du pendu

        lettre = input("Proposez une lettre : ").strip().upper()

        if len(lettre) != 1 or not lettre.isalpha():  # Vérification de la saisie
            print("Erreur : entrez une seule lettre.")
            continue

        if lettre in lettres_proposees:  # Vérification des doublons
            print("Cette lettre a déjà été proposée.")
            continue

        lettres_proposees.append(lettre)  # Enregistrement de la lettre

        if lettre in mot:  # Vérification de la présence dans le mot
            for i in range(len(mot)):  # Parcours des positions
                if mot[i] == lettre:
                    mot_masque[i] = lettre  # Révélation de la lettre

            print("Bonne lettre !")
        else:
            erreurs += 1  # Incrémentation des erreurs
            print("Mauvaise lettre !")

    print("\nMot :", " ".join(mot_masque))
    print(f"Erreurs : {erreurs}/7")
    print(dessins[erreurs])

    if "_" not in mot_masque:  # Vérification de la victoire
        return f"Gagné ! Le mot était {mot}."

    return f"Perdu ! Le mot était {mot}."


def choisir_mode():
    """
    Permet de choisir entre le mode solo et le mode deux joueurs.

    Retour :
        str : Mot à deviner en majuscules.
    """
    while True:
        print("\n1 - Jouer seul")
        print("2 - Jouer à deux")

        choix = input("Choisissez un mode (1/2) : ")

        if choix == "1":
            return choisir_mot(mots)  # Mot aléatoire de la partie C

        elif choix == "2":
            while True:
                mot = input("Joueur 1, entrez un mot : ").strip().upper()

                if mot.isalpha():  # Vérification du mot
                    print("\n" * 40)  # Masquage visuel du mot saisi
                    return mot

                print("Erreur : entrez un mot contenant uniquement des lettres.")

        else:
            print("Erreur : choisissez 1 ou 2.")


if __name__ == "__main__":
    mot = choisir_mode()  # Sélection du mode de jeu

    if mot is not None:  # Vérification de la liste de mots
        print(jouer_pendu(mot))  # Lancement du pendu
    else:
        print("Erreur : aucun mot disponible.")
