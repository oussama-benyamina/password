import hashlib
import re
import json
import random
import string


def generate_random_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
   
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    return passwords

def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file, indent=2)

def add_password():
    passwords = load_passwords()

def display_passwords():
    passwords = load_passwords()

    if not passwords:
        print("Aucun mot de passe enregistré.")
    else:
        print("Mots de passe enregistrés :")
        for hashed_password, original_password in passwords.items():
            print(f"{hashed_password}: {original_password}")

def check_password_strength(password):
    
    if len(password) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caractères."
    
   
    
    if not any(char.isdigit() for char in password):
        return False, "Le mot de passe doit contenir au moins un chiffre."

    
    
    
   
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False, "Le mot de passe doit contenir des lettres majuscules et minuscules."
    
    
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Le mot de passe doit contenir au moins un caractère spécial."

    return True, "Le mot de passe est suffisamment fort."

def hash_password(password):
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest() 
    return hashed_password

def main():
    
    while True:

        print("Menu:")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")

        choice = input("Choisissez une option (1, 2 ou 3) : ")

        if choice == '1':
            password = input("Veuillez entrer votre mot de passe : ")
            if password.lower() == 'q':
                break
            
       
            is_strong, message = check_password_strength(password)
           
            if is_strong:
                
                hashed_password = hash_password(password)
                print("Mot de passe accepté. Mot de passe haché (SHA-256) :", hashed_password)
            
                
                # Ajouter le mot de passe seulement s'il est fort
                passwords = load_passwords()
                passwords[hashed_password] = password
                save_passwords(passwords)
                print("Mot de passe ajouté avec succès.")
                
            else:
                print("Mot de passe faible. ", message)
                
            add_password()
        elif choice == '2':
            display_passwords()
        elif choice == '3':
            print("Le programme à été quitté.")
             
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
            
if __name__ == "__main__":
    main()