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
    return random.choice(liste).upper() if liste else None # Choix et conversion du mot

def masque(mot):
    """
    Crée un masque contenant autant de "_" que de lettres dans le mot.

    Paramètres :
        mot (str) : Mot à masquer.

    Retour :
        list : Liste contenant les caractères "_".
    """
    return ["_"] * len(mot)  # Création du masque

# Tests du programme
if __name__ == "__main__":
    mot_choisi = choisir_mot(mots)  # Sélection d'un mot

    print("Mot choisi :", mot_choisi)
    print("Masque :", masque(mot_choisi))