
taches = []


def afficher_menu():
    print("\n=== GESTION DES TACHES ===")
    print("1. Ajouter une tache   2. Afficher   3. Rechercher   0. Quitter")


def ajouter_tache():
    titre = input("Titre de la tache : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas etre vide.")
    else:
        taches.append(titre)
        print("Tache ajoutee avec succes.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tache pour le moment.")
    else:
        for i in range(len(taches)):
            print(f"{i + 1}. {taches[i]}")


def main():
    choix = ""
    while choix != "0":
        afficher_menu()
        choix = input("Votre choix : ").strip()
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            print("Fonction pas encore disponible.")
        elif choix == "0":
            print("Au revoir !")
        else:
            print("Erreur : option invalide.")



main()