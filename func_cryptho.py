from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    print(key)

    with open("conf.txt", "wb") as key_file:
        key_file.write(key)

def encrypt_file():
    with open("conf.txt", "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    with open(input("Entrer le chemin du fichier a chiffrer : "), "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open("fich.txt.enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file():
    with open("conf.txt", "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    with open(input("Entrer le chemin du fichier a dechiffrer : "), "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open("fich.txt.enc", "wb") as dec_file:
        dec_file.write(decrypted)

generate_key()
encrypt_file()
decrypt_file()