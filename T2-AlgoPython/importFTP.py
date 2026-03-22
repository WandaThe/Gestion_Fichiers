from ftplib import FTP
### import ftplib
import os
### import sys

### Les parametresde connexion au serveur FTP

ftp_host = '127.0.0.1'
ftp_login = 'Marseille'
ftp_password = '123'

ftp_host = '127.0.0.1'
ftp_login = 'Grenoble'
ftp_password = '123'

ftp_host = '127.0.0.1'
ftp_login = 'Paris'
ftp_password = '123'

connexion = FTP(ftp_host, ftp_login, ftp_password)
print(connexion.getwelcome())

##connexion.set_pasv(True)
print(connexion.pwd())
print(connexion.nlst())

file=open('test.txt', 'rb')
ftp.storbinary('STOR test.txt', file)
ftp.quit()
print('apres le storbinary')
print(ftp.nlst())