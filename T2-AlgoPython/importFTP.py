from ftplib import FTP, error_perm
import os

# --- import des fonctions de cryptographie ---
from func_cryptho import generate_and_load_key, encrypt_file

def backup_ponctuel(compte_admin, mdp_admin, chemin_backup):
    ftp_host = '127.0.0.1' # Laisser cette IP si exeuté sur la même machine que le serveur FTP, sinon adapter à l'IP du serveur FTP

    # Si le chemin correspond à un fichier, on procède au chiffrement et à l'upload
    if os.path.isfile(chemin_backup):
        
        # Chiffrement du fichier à sauvegarder
        cle = generate_and_load_key()
        if not cle:
            return "/!\ Erreur : Impossible de charger la clé de chiffrement."
            
        print("[*] Chiffrement du fichier en cours...")
        fichier_chiffre = encrypt_file(chemin_backup, cle)
        
        if not fichier_chiffre:
            return "/!\ Erreur lors du chiffrement du fichier."

        # Upload vers le FTP
        try:
            print(f"Connexion au serveur FTP {ftp_host}...")
            connexion = FTP(ftp_host)
            connexion.login(compte_admin, mdp_admin)
            
            # Navigation vers le dossier des bacups ponctuels 
            nom_dossier_cible = "backup_ponctuel"
            try:
                connexion.cwd(nom_dossier_cible)
            except error_perm:
                # Si le dossier n'existe pas encore sur le serveur, on le crée proprement
                print(f"Le dossier '{nom_dossier_cible}' n'existe pas. Création en cours...")
                connexion.mkd(nom_dossier_cible)
                connexion.cwd(nom_dossier_cible)
            # ----------------------------------------

            # Upload du fichier chiffré
            nom_fichier_distant = os.path.basename(fichier_chiffre)
            with open(fichier_chiffre, 'rb') as file:
                connexion.storbinary(f'STOR {nom_fichier_distant}', file)

            connexion.quit()

            # Nettoyage : suppressions de la copie locale chiffrée
            os.remove(fichier_chiffre)
            
            return f"OK: Backup ponctuel chiffré effectué avec succès dans '/{nom_dossier_cible}/{nom_fichier_distant}'"

        except Exception as e:
            # En cas d'erreur FTP, on supprime quand même le fichier temporaire chiffré s'il a été créé
            if os.path.exists(fichier_chiffre):
                os.remove(fichier_chiffre)
            return f"/!\ Erreur lors de la communication FTP : {e}"

    else: ## Si le chemin n'est pas un fichier ou encore qu'il n'existe pas, on retourne ce message d'erreur.
        return "/!\ Le fichier source n'existe pas ou la sauvegarde de dossiers complets n'est pas encore gérée."