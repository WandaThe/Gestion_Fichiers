import os #outils qui va permettre d'utiliser les fonction dun os tel que la lecture ou l'écriture 
import shutil # bibliotheque qui permet de suprimmer,copierdéplacer des fichier 

def List_Dossier(chemin):
    try:
        return os.listdir(chemin)      #cette fonction permet de lister le contenu d'un dossier 
    except FileNotFoundError:
        raise Exception("Dossier introuvable")
    

def Dossier(chemin):
    if not os.path.exists(chemin):          # Si le dossier n'existe pas
        os.makedirs(chemin)
        return chemin               # On crée le dossier
    else:                                   # Sinon (le dossier existe déjà)
        i = 1                               # Compteur pour numéroter les dossiers
        nouveau_chemin = f"{chemin}_{i}"    # Nouveau nom avec _1

            # Tant que le dossier avec ce nom existe déjà
        while os.path.exists(nouveau_chemin):
            i += 1                          # On augmente le numéro
            nouveau_chemin = f"{chemin}_{i}"# On met à jour le nom du dossier

        os.makedirs(nouveau_chemin)
        return nouveau_chemin       # On crée le dossier avec le nom disponible
                                    # On crée le dossier avec le nom disponible
                                    # On retourne le nom du dossier créé

def Fichier(chemin):
    with open(chemin, "w") as f:          #creer un fichier, il faut juste mettre le nom et sans extenson.
         f.write("Fichier créé par le script")         

def Copier(src, dest):   
    if os.path.isdir(src):              #cette fonction permet de copier , elle verifie d'abord si la source est un dossier 
        shutil.copytree(src, dest)                  #dossier = copie les fichier a l'interieru et les sosus dossier                                                       
    else:                                           #fichier = copie le fichier ainsi que ses methadonné 
        shutil.copy2(src, dest)

def Deplacer(src, dest):    #deplacer un fichier ou un dossier 
    shutil.move(src, dest)

def Supprimer(chemin):        #la foncrion regarde comme dhab si c'est un fichier ou un dossier pour le supprime differement 
    if os.path.isdir(chemin):
        shutil.rmtree(chemin)
    else:
        os.remove(chemin)

def Modifier(chemin, nouveau_nom=None, nouveau_contenu=None):
    if not os.path.exists(chemin):
        raise Exception("Fichier ou dossier introuvable")

    # Modifier le nom d'un fichier ou d'un dossier
    if nouveau_nom:
        dossier_parent = os.path.dirname(chemin)
        nouveau_chemin = os.path.join(dossier_parent, nouveau_nom)
        os.rename(chemin, nouveau_chemin)
        chemin = nouveau_chemin

    # Modifier le contenu d'un fichier
    if nouveau_contenu is not None:
        if os.path.isdir(chemin):
            raise Exception("Impossible de modifier le contenu d'un dossier")
        with open(chemin, "w") as f:
            f.write(nouveau_contenu)

    return chemin

def Chemin_Courant():
    return os.getcwd()

def Entrer_Dossier(chemin):
    if not os.path.isdir(chemin):
        raise Exception("Dossier introuvable")
    os.chdir(chemin)
    return os.getcwd()

def Retour_Dossier():
    os.chdir("..")
    return os.getcwd()