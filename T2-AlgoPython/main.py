import getpass ## pour la saisie sécurisée du mot de passe
## import des fichiers local.py et importFTP.py
import local   
import importFTP


def authentifier_admin():
    print("Connexion administrateur obligatoire")
    compte_admin = input("Compte admin : ").strip()
    mdp_admin = getpass.getpass("Mot de passe admin : ")

    if not compte_admin:
        raise Exception("Le compte admin ne peut pas être vide")
    if not mdp_admin:
        raise Exception("Le mot de passe admin ne peut pas être vide")

    return compte_admin, mdp_admin


COMPTE_ADMIN, MDP_ADMIN = authentifier_admin()


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
B - Backup ponctuel vers le FTP
0 - Quitter
""")

while True:                                            
    menu()
    choix = input("Votre choix : ")

    try:
        match choix:
            case "1":
                chemin = input("Nom du dossier : ")
                for e in local.List_Dossier(chemin):
                    print(e)

            case "2":
                chemin = input("Nom du dossier : ")
                local.Dossier(chemin)
                print("Dossier créé")

            case "3":
                chemin = input("Nom du fichier : ")
                local.Fichier(chemin)
                print("Fichier créé")

            case "4":
                src = input("Source : ")
                dest = input("Destination : ")
                local.Copier(src, dest)
                print("Copie effectuée")

            case "5":
                src = input("Source : ")
                dest = input("Destination : ")
                local.Deplacer(src, dest)
                print("Déplacement effectué")

            case "6":
                chemin = input("Nom : ")
                local.Supprimer(chemin)
                print("Suppression effectuée")

            case "7":
                chemin = input("Nom du fichier ou dossier à modifier : ")
                print("1 - Renommer")
                print("2 - Modifier le contenu d'un fichier")
                type_modif = input("Votre choix : ")

                match type_modif:
                    case "1":
                        nouveau_nom = input("Nouveau nom : ")
                        local.Modifier(chemin, nouveau_nom=nouveau_nom)
                        print("Nom modifié")

                    case "2":
                        nouveau_contenu = input("Nouveau contenu : ")
                        local.Modifier(chemin, nouveau_contenu=nouveau_contenu)
                        print("Contenu modifié")

                    case _:
                        print("Choix invalide")
            
            case "8":
                print("Dossier courant :", local.Chemin_Courant())
            
            case "9":
                chemin = input("Nom du dossier à ouvrir : ")
                nouveau = local.Entrer_Dossier(chemin)
                print("Vous etes dans le dossier :", nouveau)

            case "10":
                nouveau = local.Retour_Dossier()
                print("Retour au dossier parent :", nouveau)
                
            case "B" | "b":
                chemin_source = input("Chemin du fichier ou dossier à sauvegarder : ").strip()
                resultat = importFTP.backup_ponctuel(COMPTE_ADMIN, MDP_ADMIN, chemin_source)
                print(resultat)

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
