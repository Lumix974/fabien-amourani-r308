
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

        if lettre in mot:
            for i, caractere in enumerate(mot):  # Parcours du mot
                if caractere == lettre:
                    mot_masque[i] = lettre  # Révélation de la lettre

            print("Bonne lettre !")
        else:
            erreurs += 1  # Incrémentation des erreurs
            print("Mauvaise lettre !")

    print("\nMot :", " ".join(mot_masque))
    print(f"Erreurs : {erreurs}/7")
    print(dessins[erreurs])

    resultat = "Gagné" if "_" not in mot_masque else "Perdu"
    return f"{resultat} ! Le mot était {mot}."

def choisir_mode():
    """
    Permet de choisir entre le mode solo et le mode deux joueurs.

    Retour :
        str : Mot à deviner en majuscules.
        None : Si aucun mot n'est disponible.
    """
    while True:
        print("\n1 - Jouer seul\n2 - Jouer à deux")

        choix = input("Choisissez un mode (1/2) : ").strip()

        if choix == "1": return choisir_mot(mots)  # Mode solo, Mot aléatoire de la partie C

        if choix == "2":
            while True:
                mot = input("Joueur 1, entrez un mot : ").strip().upper()

                if mot.isalpha():  # Vérification du mot
                    print("\n" * 40)  # Masquage visuel du mot saisi
                    return mot

                print("Erreur : entrez un mot contenant uniquement des lettres.")
        else:
            print("Erreur : choisissez 1 ou 2.")

def jouer():
    """
    Permet de rejouer au Pendu après chaque partie.

    Retour :
        None
    """
    while True:  # Boucle de rejouabilité
        mot = choisir_mode()  # Choix du mode et du mot

        print(jouer_pendu(mot)) if mot else print("Erreur : aucun mot disponible.")

        while True:
            reponse = input("\nRejouer ? (o/n) : ").strip().lower()

            if reponse in ("o", "n"): break
            print("Erreur : entrez o ou n.")

        if reponse == "n":
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    jouer()  # Lancement du jeu avec rejouabilité