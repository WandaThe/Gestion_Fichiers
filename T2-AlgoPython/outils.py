from datetime import datetime

def heure():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def version(nom_fichier):
    return f"{nom_fichier}_{heure()}"