## Script de sauvegarde sécurisée avec chiffrement et transfert FTP
## Ce script permet de chiffrer un fichier localement, de le sauvegarder avec un horodatage pour l'archivage, puis de le transférer vers un serveur FTP distant.
## ATTENTION : Le script doit être modifié à la reception, aller ligne 88
import os
import datetime
from ftplib import FTP
from cryptography.fernet import Fernet

def generate_and_load_key(key_path="conf.key"):
    """
    Génère une clé Fernet si elle n'existe pas, et la charge.
    """
    try:
        if not os.path.exists(key_path):
            key = Fernet.generate_key()
            with open(key_path, "wb") as key_file:
                key_file.write(key)
            print(f"OK: Nouvelle clé générée et sauvegardée dans {key_path}")
        
        with open(key_path, "rb") as key_file:
            return key_file.read()
    except Exception as e:
        print(f"/!\\ Erreur lors de la gestion de la clé : {e}")
        return None

def encrypt_file(file_path, key):
    """
    Chiffre un fichier et le sauvegarde avec un horodatage pour l'archivage.
    """
    try:
        fernet = Fernet(key)
        
        # Lecture du fichier local
        with open(file_path, "rb") as file:
            original = file.read()
        
        # Chiffrement du contenu du fichier
        encrypted = fernet.encrypt(original)
        
        # Création du nom de fichier horodaté (Ex: document_HEBDO/QUOTIDIEN_20260321_052810.enc)
        timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
        base_name = os.path.basename(file_path)
        # On vérifie si on est vendredi (jour 4)
        if datetime.datetime.now().weekday() == 4:
            type_backup = "HEBDO"
        else:
            type_backup = "QUOTIDIEN"         

        encrypted_file_path = f"{base_name}_{type_backup}_{timestamp}.enc"

        # Sauvegarde locale du fichier chiffré
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
            
        print(f"[+] Fichier chiffré avec succès : {encrypted_file_path}")
        return encrypted_file_path
        
    except FileNotFoundError:
        print(f"/!\\ Erreur : Le fichier {file_path} est introuvable.")
        return None
    except Exception as e:
        print(f"/!\\ Erreur lors du chiffrement : {e}")
        return None

def upload_to_ftp(file_path, ftp_host, ftp_user, ftp_pass):
    """
    Envoie le fichier chiffré sur le serveur FTP distant de Paris dans le répertoire du site.
    """
    try:
        # Connexion au serveur FTP
        print(f"Connexion au serveur FTP {ftp_host}...")
        ftp = FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_pass)
        

        
        # Upload sécurisé du fichier
        with open(file_path, 'rb') as file_to_upload:
            ftp.storbinary(f"STOR {os.path.basename(file_path)}", file_to_upload)
            
        print(f"OK: Upload réussi pour {os.path.basename(file_path)} dans le répertoire FTP de {ftp_user}.")
        ftp.quit()
        
    except Exception as e:
        print(f"/!\\ Erreur lors du transfert FTP : {e}")

# --- Bloc d'exécution principal ---
if __name__ == "__main__":
    # Paramètres de configuration (à adapter selon votre environnement)
    FICHIER_A_SAUVEGARDER = "Données_patients.txt" # fichier à sauvegarder chaque jour à 20h.
    FTP_HOST = "127.0.0.1" # Remplacer par l'IP du serveur FTP de votre site si différent de localhost
    FTP_USER = "Marseille"
    FTP_PASS = "Marseille"
    
    print("--- DÉBUT DE LA PROCÉDURE DE SAUVEGARDE SÉCURISÉE ---")
    
    # Gestion de la clé de chiffrement
    cle = generate_and_load_key()
    
    if cle:
        # Chiffrement et archivage horodaté (ou versionné) du fichier
        fichier_chiffre = encrypt_file(FICHIER_A_SAUVEGARDER, cle)
        
        # 3. Transfert FTP si le chiffrement a réussi
        if fichier_chiffre:
            upload_to_ftp(fichier_chiffre, FTP_HOST, FTP_USER, FTP_PASS)
            
            #Nettoyage : supprimer le fichier chiffré local si l'upload a réussi
            os.remove(fichier_chiffre)
            
    print("--- FIN DE LA PROCÉDURE ---")