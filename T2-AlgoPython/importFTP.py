from ftplib import FTP, error_perm
### import ftplib
import os
### import sys
from outils import version

FTP_HOST = '127.0.0.1'

def backup_ponctuel(compte_admin, mdp_admin, chemin_backup):
    ftp_host = '127.0.0.1'
    connexion = FTP(ftp_host)
    connexion.login(compte_admin, mdp_admin)

    print(connexion.getwelcome())

    

    if os.path.isfile(chemin_backup):
        nom_fichier = os.path.basename(chemin_backup)
        file = open(chemin_backup, 'rb')
        connexion.storbinary(f'STOR {nom_fichier}', file)
        file.close()
        print("Backup fichier effectué")

    else:
        print("Le backup dossier n'est pas encore géré")

    connexion.quit()

# ### Les parametresde connexion au serveur FTP

# ftp_host = '127.0.0.1'
# ftp_login = 'Marseille'
# ftp_password = '123'

# ftp_host = '127.0.0.1'
# ftp_login = 'Grenoble'
# ftp_password = '123'

# ftp_host = '127.0.0.1'
# ftp_login = 'Paris'
# ftp_password = '123'

# connexion = FTP(ftp_host, ftp_login, ftp_password)
# print(connexion.getwelcome())

# ##connexion.set_pasv(True)
# print(connexion.pwd())
# print(connexion.nlst())

# file=open('test.txt', 'rb')
# ftp.storbinary('STOR test.txt', file)
# ftp.quit()
# print('apres le storbinary')
# print(ftp.nlst())