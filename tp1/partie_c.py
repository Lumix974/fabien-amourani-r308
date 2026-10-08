import random

mots = ["python", "reseau", "ordinateur", "internet", "serveur", "routeur"]  # Liste des mots

def choisir_mot(liste):
    """
    Choisit un mot aléatoire dans une liste et le convertit en majuscules.

    Paramètres :
        liste (list) : Liste contenant les mots.

    Retour :
        str : Mot choisi en majuscules.
        None : Si la liste est vide.
    """
    if len(liste) == 0:  # Vérification de la liste vide
        return None

    mot = random.choice(liste)  # Choix d'un mot aléatoire
    return mot.upper()  # Conversion en majuscules

def masque(mot):
    """
    Crée un masque contenant autant de "_" que de lettres dans le mot.

    Paramètres :
        mot (str) : Mot à masquer.

    Retour :
        list : Liste contenant les caractères "_".
    """
    liste_masque = []  # Initialisation du masque

    for lettre in mot:  # Parcours des lettres du mot
        liste_masque.append("_")  # Ajout d'un caractère "_"

    return liste_masque

# Tests du programme
if __name__ == "__main__":
    mot_choisi = choisir_mot(mots)  # Sélection d'un mot

    print("Mot choisi :", mot_choisi)
    print("Masque :", masque(mot_choisi))