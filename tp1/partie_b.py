import random

def deviner_nombre(borne_min=1, borne_max=100):
    """
    Génère un nombre aléatoire et demande au joueur de le deviner.
    Le joueur dispose de 10 essais maximum.

    Paramètres :
        borne_min (int) : Valeur minimale (1 par défaut).
        borne_max (int) : Valeur maximale (100 par défaut).

    Retour :
        str : Message de victoire, de défaite ou d'erreur.
    """
    if borne_min >= borne_max:  # Vérification des bornes
        return "Erreur : les bornes sont invalides."

    nb_random = random.randint(borne_min, borne_max)  # Nombre aléatoire
    essai = 1  # Initialisation du compteur

    while essai <= 10:  # Maximum 10 essais
        print(f"\nEssai numéro : {essai}/10")

        try:
            nb_joueur = int(input("Entrez un entier : "))  # Saisie du joueur

        except ValueError:  # Gestion des saisies invalides
            print("Erreur : vous devez entrer un entier.")
            continue

        if not borne_min <= nb_joueur <= borne_max:  # Vérification des bornes
            print(f"Erreur : entrez un nombre entre {borne_min} et {borne_max}.")
            continue

        if nb_joueur < nb_random:
            print("Trop petit")

        elif nb_joueur > nb_random:
            print("Trop grand")

        else:
            return f"Gagné en {essai} essai(s) !"

        essai += 1  # Incrémentation du compteur

    return f"Nombre non trouvé, c'était {nb_random}"

def jouer(borne_min=1, borne_max=100):
    """
    Permet au joueur de recommencer une partie après chaque jeu.

    Paramètres :
        borne_min (int) : Borne minimale du jeu.
        borne_max (int) : Borne maximale du jeu.

    Retour :
        None : La fonction ne retourne aucune valeur.
    """
    while True:  # Boucle de rejouabilité
        print(deviner_nombre(borne_min, borne_max))  # Lancement d'une partie

        while True:
            reponse = input("\nRejouer ? (o/n) : ").strip().lower()

            if reponse in ("o", "n"):  # Vérification de la réponse
                break

            print("Erreur : entrez o ou n.")

        if reponse == "n":  # Arrêt du jeu
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    while True:
        try:
            borne_min = int(input("Entrez la borne minimale : "))
            borne_max = int(input("Entrez la borne maximale : "))

            if borne_min >= borne_max:  # Vérification des bornes
                print("Erreur : la borne minimale doit être inférieure à la maximale.")
                continue  # Redemande les bornes

            break  # Sort de la boucle si les bornes sont valides

        except ValueError:  # Gestion des saisies non numériques
            print("Erreur : les bornes doivent être des entiers.")

    jouer(borne_min, borne_max)  # Lance le jeu