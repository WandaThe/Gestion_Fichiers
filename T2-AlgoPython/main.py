from local import *   #j'intégre le fichier local,ftp et outils
#from ftp import *
from outils import *

def menu():
    print("""
1 - Lister un dossier
2 - Créer un dossier
3 - Créer un Fichier 
4 - Copier
5 - Déplacer
6 - Supprimer
7 - Modifier
8 - Afficher le dossier courant
9 - Entrer dans un dossier
10 - Revenir au dossier parent
0 - Quitter
""")

while True:                                            
    menu()
    choix = input("Votre choix : ")

    try:
        match choix:
            case "1":
                chemin = input("Nom du dossier : ")
                for e in List_Dossier(chemin):
                    print(e)

            case "2":
                chemin = input("Nom du dossier : ")
                Dossier(chemin)
                print("Dossier créé")

            case "3":
                chemin = input("Nom du fichier : ")
                Fichier(chemin)
                print("Fichier créé")

            case "4":
                src = input("Source : ")
                dest = input("Destination : ")
                Copier(src, dest)
                print("Copie effectuée")

            case "5":
                src = input("Source : ")
                dest = input("Destination : ")
                Deplacer(src, dest)
                print("Déplacement effectué")

            case "6":
                chemin = input("Nom : ")
                Supprimer(chemin)
                print("Suppression effectuée")

            case "7":
                chemin = input("Nom du fichier ou dossier à modifier : ")
                print("1 - Renommer")
                print("2 - Modifier le contenu d'un fichier")
                type_modif = input("Votre choix : ")

                match type_modif:
                    case "1":
                        nouveau_nom = input("Nouveau nom : ")
                        Modifier(chemin, nouveau_nom=nouveau_nom)
                        print("Nom modifié")

                    case "2":
                        nouveau_contenu = input("Nouveau contenu : ")
                        Modifier(chemin, nouveau_contenu=nouveau_contenu)
                        print("Contenu modifié")

                    case _:
                        print("Choix invalide")
            
            case "8":
                print("Dossier courant :", Chemin_Courant())
            
            case "9":
                chemin = input("Nom du dossier à ouvrir : ")
                nouveau = Entrer_Dossier(chemin)
                print("Vous etes dans le dossier :", nouveau)

            case "10":
                nouveau = Retour_Dossier()
                print("Retour au dossier parent :", nouveau)

            case "0":
                print("Fin du programme")
                break

            case _: 
                print("Choix invalide")

    except Exception as e:
        print("Erreur :", e)



# def menu(): #affichage du menu avec print
#     print("""
# 1 - Lister un dossier
# 2 - Créer un dossier
# 3 - Créer un Fichier 
# 4 - Copier
# 5 - Déplacer
# 6 - Supprimer
# 0 - Quitter
# """)

# while True:                                            
#     menu()
#     choix = input("Votre choix : ")

#     try:
#         if choix == "1":
#             chemin = input("Nom du dossier : ")
#             for e in List_Dossier(chemin):
#                 print(e)

#         elif choix == "2":
#             chemin = input("Nom du dossier : ")
#             Dossier(chemin)
#             print("Dossier créé")

#         elif choix == "3":
#             chemin = input("Nom du fichier : ")
#             Fichier(chemin)
#             print("Fichier créé")

#         elif choix == "4":
#             src = input("Source : ")
#             dest = input("Destination : ")
#             Copier(src, dest)
#             print("Copie effectuée")

#         elif choix == "5":
#             src = input("Source : ")
#             dest = input("Destination : ")
#             Deplacer(src, dest)
#             print("Déplacement effectué")

#         elif choix == "6":
#             chemin = input("Nom : ")
#             Supprimer(chemin)
#             print("Suppression effectuée")

#         elif choix == "0":
#             print("Fin du programme")
#             break

#         else:
#             print("Choix invalide")

#     except Exception as e:
#         print("Erreur :", e)
